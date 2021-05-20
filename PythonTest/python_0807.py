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


os.makedirs('./image/', exist_ok=True)
for index in range(1,10):
    r = requests.get("https://s.alicdn.com/@sc01/kf/H1a3e0a3f57b94d00abfa59b853781ee8O.jpg_300x300.jpg", stream=True)
    with open('./image/img{0}.png'.format(index), 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
    print('ok')