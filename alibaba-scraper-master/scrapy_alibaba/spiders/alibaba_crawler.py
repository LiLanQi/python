# -*- coding: utf-8 -*-
import json
import uuid
import os
import requests
import scrapy
from scrapy.http import Request
import csv
from selectorlib import Extractor
from urllib.request import urlretrieve
import re
import time
from selenium import webdriver
from square.client import Client
import time
from selenium import webdriver




class AlibabaCrawlerSpider(scrapy.Spider):
    name = 'alibaba_crawler'
    allowed_domains = ['alibaba.com']
    start_urls = ['http://alibaba.com/']
    extractor = Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__), "../resources/search_results.yml"))
    max_pages = 3

    def start_requests(self):
        """Read keywords from keywords file amd construct the search URL"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        with open(os.path.join(os.path.dirname(__file__), "../resources/keywords.csv")) as search_keywords:
            for keyword in csv.DictReader(search_keywords):
                search_text=keyword["keyword"]
                url="https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={0}&viewtype=G".format(search_text)
                # The meta is used to send our search text into the parser as metadata
                yield scrapy.Request(url, callback = self.parse, meta = {"search_text": search_text}, headers=headers)


    def parse(self, response):
        data = self.extractor.extract(response.text,base_url=response.url)
        for product in data['products']:
            yield product
        # Try paginating if there is data
        if data['products']:
            if '&page=' not in response.url and self.max_pages>=2:
                yield Request(response.request.url+"&page=2")
            else:
                url = response.request.url
                current_page_no = re.findall('page=(\d+)',url)[0]
                next_page_no = int(current_page_no)+1
                url = re.sub('(^.*?&page\=)(\d+)(.*$)',rf"\g<1>{next_page_no}\g<3>",url)
                if next_page_no <= self.max_pages:
                    yield Request(url,callback=self.parse)


def create_my_catalog_img(image_url, index):
    r = requests.get(image_url, stream=True)
    with open('./image/img{0}.png'.format(index), 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
    file_to_upload_path = "./image/img{0}.png".format(index)
    f_stream = open(file_to_upload_path, "rb")

    result = client.catalog.create_catalog_image(
        request={
            "idempotency_key": str(uuid.uuid4()),
            "image": {
                "type": "IMAGE",
                "id": "#1042520531",
                "image_data": {
                    "name": "the picture of " + name,
                }
            }
        },
        image_file=f_stream
    )
    if result.is_success():
        print(result.body)
        return result.body
    elif result.is_error():
        print(result.errors)

def create_my_catalog_item(name, price, index, image_version, image_id):
    price = str(price)
    lastIndex = price.find('-')
    price = int(float(price[1:lastIndex]) * 100)
    result = client.catalog.upsert_catalog_object(
        body={
            "idempotency_key": str(uuid.uuid4()),
            "object": {
                "type": "ITEM",
                "id": "#hhhh",
                "version": image_version,
                "image_id": image_id,
                "present_at_all_locations": True,
                "item_data": {
                    "name": str(name),
                    "description": "hhyhhhhh",
                    "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "id": "#fgggg111",
                            "item_variation_data": {
                                "item_id": "#hhhh",
                                "name": "gdfgfdgdfg",
                                "pricing_type": "FIXED_PRICING",
                                "price_money": {
                                    "amount": price,
                                    "currency": "USD"
                                }
                            }
                        }
                    ],
                    "product_type": "REGULAR"
                }
            }
        }
    )
    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

if __name__ == '__main__':
    '''
    使用命令行scrapy crawl alibaba_crawler -o out.json -t json
    '''
    client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
    os.makedirs('./image/', exist_ok=True)
    with open('out.json', 'r') as f:
        tempList = json.loads(f.read())
        index = 0
        for temp in tempList:
            name = temp['name']
            price = temp['price']
            image_url = temp['image']
            result = create_my_catalog_img(image_url, index)
            image_id = result["image"]["id"]
            image_version = result["image"]["version"]
            create_my_catalog_item(name, price, index, image_version, image_id)
            index = index + 1



