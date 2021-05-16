import requests
from lxml import etree

url = 'https://www.aliexpress.com/wholesale?initiative_id=SB_20190514011143&site=glo&SearchText=phone&page='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}

def geturl():
	#分析url，写一个for循环进行拼接url，获取到1-100页url地址，下面的i一定要进行str字符串格式转换。
    for i in range(1,101):
        start_url = 'https://www.aliexpress.com/wholesale?initiative_id=SB_20190514011143&site=glo&SearchText=phone&page='+(str(i))
        # print(start_url)
        getdata(start_url)   #调用这个函数将获取到的url传给getdata函数

def getdata(start_url):
	#接收传递来的url发起请求，这里是get请求
    response = requests.get(start_url,headers=headers)
    if response.status_code == 200:
        # print('请求成功')
        html = response.content
        html1 = html.decode('utf-8')
        #print(html1)
        #保存页面源码
        # for i in range(1,101):
        #     with open(str(i) + '.html', 'a', encoding='utf-8') as file:
        #         file.write(str(html1))
        #         print('保存成功')
        c_data = etree.HTML(html1)
        list_data = c_data.xpath('//*[@id="root"]/div/div')
        print(list_data)
        for l_data in list_data:
            print(1)
            print(l_data)



if __name__ == '__main__':
    geturl()
