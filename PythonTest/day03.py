import requests
from bs4 import BeautifulSoup
import json
#获取豆瓣排名前250的电影名称（静态页面抓取)
def get_movies():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    move_list = []
    for i in range(0,10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text,"lxml")
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            move_list.append(movie)
    return move_list

#输出评论数据(解析出json)
def get_comment():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    url = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112403678947982518441_1620637152057&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1620637152059'
    r = requests.get(url, headers=headers)
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = eachone['content']
        print(message)

if __name__ == '__main__':
    # movies = get_movies()
    # print(movies)
    get_comment()



