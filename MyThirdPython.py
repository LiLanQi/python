from lxml import etree
import requests


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents",headers=headers)
etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/article/a/div[2]/text()')
for each in content:
    print(each + '\n')
