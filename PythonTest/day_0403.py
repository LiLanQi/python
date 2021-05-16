import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url = 'https://www.1688.com/'
    headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    print(r.text)
    soup = BeautifulSoup(r.text,'lxml')
    source_list = soup.find_all('div',class_="grid rec-offer")
    for source in source_list:
        # goods_href = BeautifulSoup(source, 'lxml').a['href']
        goods_src = BeautifulSoup(source, 'lxml').find('img', class_="custom offer-image")["src"]
        print(goods_src)

