import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"strPriceMoney\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title1 = eval(tlt[i].split(':')[1])
            title = re.sub(r'<.*?>', '', title1)
            ilt.append([price, title])
    except:
        print('error')


def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for i in ilt:
        count += 1
        print(tplt.format(count, i[0], i[1]))


def main():
    goods = '电脑'
    start_url = 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?spm=a2609.11209760.it2i6j8a.6.50832de1NZAXIF&cosite=qqdaohang&keywords=' + goods
    infoList = []
    try:
        url = start_url
        html = getHTMLText(url)
        parsePage(infoList, html)
        printGoodsList(infoList)
    except:
        print('error')
main()


