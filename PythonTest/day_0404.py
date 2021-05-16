import  requests
import json

def getjson(loc, page_num=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    }
    pa = {'q':'公园',
        'region':loc,
        'scope':'2',
        'page_size':20,
        'page_num':page_num,
        'output':'json',
        'ak':'PImkHrbowPHGrj4s3k2HqHEezXXhn4St'
    }
    r = requests.get("http://api.map.baidu.com/place/v2/search",params=pa,headers=headers)
    decodejson = json.loads(r.text)
    return decodejson

print(getjson('北京市'))