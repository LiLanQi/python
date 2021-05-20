import requests
from selenium import webdriver
import scrapy
import os
import selectorlib
driver = webdriver.Firefox(executable_path = r'C:\Users\Administrator\Desktop\geckodriver.exe')
driver.implicitly_wait(20) # 隐性等待，最长等20秒
#把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=headphones&viewtype=G")


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
image = driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/img').get_attribute('src')
print(image)
comments = driver.find_elements_by_css_selector('div._display_row_cost_1fkm9_35')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('h2')
    price = content.text
    print(price)

name = driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/p[1]').text
print(name)

# stock = driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div[2]').text
# stock = stock[0:str(stock).find('in')]
# print(stock)

product_page_extractor = selectorlib.Extractor.from_yaml_file(
        os.path.join(os.path.dirname(__file__), '../selectorlib_yaml/dropShippingProductPage.yml'))
response = requests.get("https://dropshipping-products.automizely.com/products/a77f5f97be20449bb62aae430f55b98b")
product = product_page_extractor.extract(response.text)
print(product)

