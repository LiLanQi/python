import requests
import scrapy
import os
import selectorlib
from bs4 import BeautifulSoup



def readFile():
    data = ""
    for line in open("data.txt", "r"):
        data += line


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    response = requests.get("https://dropshipping-products.automizely.com/products/81bd71b276a44aecb77f90e075b23fe6",headers=headers)
    with open("123456.txt", 'w', encoding='utf-8') as file:
        file.write(response.text)