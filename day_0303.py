# 所有数据 div class="property"
# 房屋名称 h3 class="property-content-title-name"
# 总价 span class="property-price-total-num"
# 均价 p class="property-price-average"
# 几室几厅 div class ="property-content-info" p[0]
# 面积 div class ="property-content-info" p[1]
# 层数 div class ="property-content-info" p[3]
# 建造年份 p class="property-content-info" p[4]
# 中介 span class="property-extra-text"
# 地址 p class="property-content-info-comm-address"
# 标签 span class="property-content-info-tag"

#爬取失败
import requests
from bs4 import  BeautifulSoup

url = 'https://beijing.anjuke.com/sale/'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text,'lxml')
house_list = soup.find_all('section',class_="list")
house = house_list[0]
name = house.find('div',class_="property").a.text.strip()
# print(name)
price = house.find('span',class_="property-price-total-num").text.strip()
price_area = house.find('p',class_="property-price-average").text.strip()
# print(price_area)

total = house.find('div',class_="property-content-info")
no_room = total.select('p')[0].text.strip()
area = total.select('p')[1].text.strip()
floor = total.select('p')[3].text.strip()
year = total.select('p')[4].text.strip()
address = house.find('p', class_="property-content-info-comm-address").text.strip()
# print(no_room)
# print(area)
# print(floor)
# print(year)
#print(house)
#print(address)