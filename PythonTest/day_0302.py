import requests
from bs4 import BeautifulSoup
import json

#使用BeautifulSoup抓取第一页所有的标题
url='http://www.santostang.com/'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text,'lxml')
first_title = soup.find("h1", class_="post-title").a.text.strip()
print("第一篇文章的标题是：", first_title)

title_list = soup.find_all("h1", class_="post-title")
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print("第%s篇文章的标题是：%s" %(i+1, title))

print(soup.header.div.contents)