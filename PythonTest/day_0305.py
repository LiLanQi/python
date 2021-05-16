import  MySQLdb
import requests
from bs4 import BeautifulSoup
url = 'http://www.santostang.com/'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='nba', charset='utf8')
cur = conn.cursor()
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text,'lxml')
title_list = soup.find_all('h1', class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    sql = "insert into urls(url, content) values(" + str(url) + ',' + str(title) + ')'
    print(sql)
    cur.execute("insert into urls(url,content) values(%s,%s)",(url,title))
    #cur.execute(sql)
cur.close()
conn.commit()
conn.close()