class jd_comment():

    def __init__(self, url, iniURL, header={}, para={}, cookie={}, maxPage=150, sleeptime=[5, 20]):
        self.url = url
        self.iniURL = iniURL  # 主页面url
        self.maxPage = maxPage
        self.header = header
        self.para = para
        self.cookie = cookie
        self.sleeptime = sleeptime

    # 字符转成字典
    def str2dict(self, txt):
        with open(txt) as f:
            string = f.read()
        dic = {}
        for each in string.split('\n'):
            key, value = each.split(': ', 1)
            dic[key] = value
        return dic

    # 避免频繁访问而引起反爬
    def random_sleep(self):
        import time
        import random
        time.sleep(random.randint(self.sleeptime[0], self.sleeptime[1]))
        return None

    # 避免网络问题造成程序中断
    def multi_requestGet(self, url, header={}, para={}, cookie={}, cnt=5):
        import requests
        while cnt > 0:
            try:
                return requests.get(url, headers=header, cookies=cookie, params=para)
                break
            except ConnectionError as e:
                print(str(e) + ' remain times : %d' % cnt)
                self.random_sleep()
                cnt -= 1

    # 从主页面拿每个产品的id
    def get_productId(self):
        from lxml import etree
        import re
        etree_html = etree.HTML(self.multi_requestGet(self.iniURL, header=self.header).text)
        product_id = []
        for each in etree_html.xpath('//a/@href'):
            if re.match('//item.jd.com/[0-9]{7}.html#crumb-wrap', each):
                product_id.append(str(each).replace(r'//item.jd.com/', '').replace(r'.html#crumb-wrap', ''))
        return product_id

    # 拿产品的所有评论
    def get_productComm(self):
        import pandas as pd
        import json
        for i in range(1, self.maxPage + 1):
            self.para['page'] = str(i)
            print("productID: %s ,starting %d page..." % (self.para['productId'], i))
            r = self.multi_requestGet(url, header=self.header, para=self.para)
            # js返回的数据需要去掉头部才能转json格式
            data = json.loads(r.text.replace("fetchJSON_comment98vv32(", "").replace(");", ""))
            if len(data['comments']) < 1:
                break
            else:
                if i == 1:
                    df = pd.DataFrame(data['comments'])
                else:
                    df = pd.concat([df, pd.DataFrame(data['comments'])])
                self.random_sleep()
        df['productId'] = self.para['productId']
        return df

    # 拿所有产品的评论
    def go_query(self, product_id):
        import pandas as pd
        tot_df = pd.DataFrame()
        for each in product_id:
            self.para['productId'] = each
            df = self.get_productComm()
            tot_df = pd.concat([tot_df, df])
        return tot_df

    # 数据框直接写入mysql数据库
    def storeData2MySql(self, data, schema, table):
        import sqlalchemy
        import pandas as pd
        conn = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/nba?charset=utf8mb4')
        pd.io.sql.to_sql(data, table, con=conn, schema=schema, if_exists='replace', index=False)
        print("-----data had stored:%d rows" % len(data))
        return None

        # 主程序

    def main_process(self, tbname):
        try:
            productId = self.get_productId()
        except Exception as e:
            raise Exception("get_productId Failed : " + str(e))
        try:
            df = self.go_query(productId)
        except Exception as e:
            raise Exception("go_query Failed : " + str(e))
        try:
            self.storeData2MySql(self, df, 'python_spyder', tbname)
        except Exception as e:
            raise Exception("storeData2MySql Failed : " + str(e))
        return None


if __name__ == '__main__':
    url = 'https://sclub.jd.com/comment/productPageComments.action'  # 获取评论的url
    iniURL = 'https://mall.jd.com/index-1000001956.html'  # 店铺主页
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }

    JDsmartisan_comm = jd_comment(url=url, iniURL=iniURL)  # 初始化对象
    JDsmartisan_comm.header = headers # 读取header
    JDsmartisan_comm.para = 'callback=fetchJSON_comment98&productId=100008865903&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1' # 读取参数
    JDsmartisan_comm.main_process('JDsmartisan_comment')