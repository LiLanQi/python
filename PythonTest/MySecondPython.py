class getNBAData():

    def __init__(self, start_url='https://china.nba.com/static/data/player/stats_klay_thompson.json'):
        self.start_url = start_url

    # 从start_url得到每场比赛的id
    def get_gameid(self, start_url):
        import requests
        import json
        r = requests.get(start_url)
        data = json.loads(r.content)
        game_id = []
        for each in data['payload']['player']['stats']['seasonGames']:
            game_id.append(each['profile']['gameId'])
        print(game_id)
        return game_id

    # 把列表解析成数据框
    def resol_dataLs(self, dataLs, team):
        import pandas as pd
        playerData = dataLs[team]['gamePlayers']
        teamName = dataLs[team]['profile']['displayAbbr']
        for i in range(len(playerData)):
            playerData[i]['statTotal'].update(player=playerData[i]['profile']['displayName'])
            playerData[i] = playerData[i]['statTotal']
        df = pd.DataFrame(playerData, columns=list(playerData[0].keys()))
        df['teamName'] = teamName
        df['atHome'] = team
        print(df)
        return df

    # 数据框直接写入mysql数据库，我的密码用*代替了
    # self.storeData2MySql(tot_df, 'nba', 'worriorsgame')
    def storeData2MySql(self, data, schema, table):
        import sqlalchemy
        import pandas as pd
        conn = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/nba?charset=utf8mb4')
        pd.io.sql.to_sql(data, table, con=conn, schema=schema, if_exists='replace', index=False)
        print("-----data had stored:%d rows" % len(data))
        return None

    # 主函数
    def get_gameprofile(self):
        import datetime
        import pytz
        import requests
        import json
        import pandas as pd
        game_id = self.get_gameid(self.start_url)
        url = 'https://china.nba.com/static/data/game/snapshot_%s.json     '
        for each in game_id:
            r = requests.get(url % each)
            rawdata = json.loads(r.content)
            homeTeam = self.resol_dataLs(rawdata['payload'], 'homeTeam')
            awayTeam = self.resol_dataLs(rawdata['payload'], 'awayTeam')
            gameTime = datetime.datetime.fromtimestamp(int(rawdata['timestamp']) / 1000,
                                                       pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
            tot_df = pd.concat([homeTeam, awayTeam])
            tot_df['gameDate'] = gameTime
            tot_df['gameDesc'] = '%s(%d)@%s(%d)' % (
            tot_df[tot_df['atHome'] == 'awayTeam']['teamName'][0], rawdata['payload']['boxscore']['awayScore'],
            tot_df[tot_df['atHome'] == 'homeTeam']['teamName'][0], rawdata['payload']['boxscore']['homeScore'])
            print(tot_df['gameDesc'])
            self.storeData2MySql(tot_df, 'nba', 'worriorsgame')


if __name__ == '__main__':
    getNBAData().get_gameprofile()