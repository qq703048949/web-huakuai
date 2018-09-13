# !/usr/bin/env python3
# encoding: utf-8 
# Date  : 2018/9/12 9:55
# @Author : Rainflower 
# @Site : 
# @File : t.py
# @Software: PyCharm Community Edition
import base64

import requests
from bs4 import BeautifulSoup
import json

cookies = {"TYCID": "ae37ff10f74c11e78229a383e5ef9cae",
"undefined": "ae37ff10f74c11e78229a383e5ef9cae",
"Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1515831444,1515987784,1516013782,1516089171",
"ssuid": "9064375458",
"RTYCID": "3b40b231b5e046bebe7943f20977fdc5",
"tyc-user-info": "%7B%22token%22%3A%22eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODU2Njc5MzA4NSIsImlhdCI6MTUxNjA5Mjg5OSwiZXhwIjoxNTMxNjQ0ODk5fQ.GSLBJNbfoBBaT2DcazevzGboKM8Jq3VdPxw8SrRDAqJ9mLciBroR8r1E8wLFfDhLDx-Q15H58Z4KAqsJ5jPufg%22%2C%22integrity%22%3A%220%25%22%2C%22state%22%3A%220%22%2C%22vipManager%22%3A%220%22%2C%22vnum%22%3A%220%22%2C%22onum%22%3A%220%22%2C%22mobile%22%3A%2218566793085%22%7D",
"auth_token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODU2Njc5MzA4NSIsImlhdCI6MTUxNjA5Mjg5OSwiZXhwIjoxNTMxNjQ0ODk5fQ.GSLBJNbfoBBaT2DcazevzGboKM8Jq3VdPxw8SrRDAqJ9mLciBroR8r1E8wLFfDhLDx-Q15H58Z4KAqsJ5jPufg",
"aliyungf_tc": "AQAAAAzlxkeq7wIACjaJd4F2MmjG7syM",
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Host': 'www.tianyancha.com',
'Referer': 'https://www.tianyancha.com'
}
url = 'http://antirobot.tianyancha.com/captcha/getCaptcha.json'
for i in range(1):
    try:
        resp = requests.get(url)
        print(resp.status_code)
        print(resp.text)
        bgImage = json.loads(resp.text)['data']['bgImage']
        targetImage = json.loads(resp.text)['data']['targetImage']
        print(targetImage)
        with open(r'E:\get_img\bgImage\{}.jpg'.format(i), 'wb') as f:
            b = base64.b64decode(bgImage)
            f.write(b)
        with open(r'E:\get_img\targetImage\{}.jpg'.format(i), 'wb') as f:
            t = base64.b64decode(targetImage)
            f.write(t)

    except Exception as e:
        print(e)

print(json.loads('{"code":"100003","msg":"\u53c2\u6570\u9519\u8bef"}'))