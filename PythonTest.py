import requests
from lxml import etree
import json

url = 'https://china.nba.com/scripts/locales/zh_CN/translation.json'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
response = requests.get(url, headers=headers)
rawData = json.loads(response.content)
print(rawData)
oppTeam = rawData['whosHot']['title']
print(oppTeam)

