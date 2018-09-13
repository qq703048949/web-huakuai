#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 0004 下午 9:37
# @Author  : Lotus
# @Site    : 
# @File    : login_requests.py
# @Software: PyCharm
import os
import requests
import sys
import json




headers = {
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F',
    'Host': 'passport.weibo.cn',
    'User-Agent': "Mozilla/5.0 (PlayStation 4 4.71) AppleWebKit/601.2 (KHTML, like Gecko)",

}
login_url = 'https://passport.weibo.cn/sso/login'


    # try:
data = {
    "client_id": "",
    "code": "",
    "ec": "0",
    "entry": "mweibo",
    "hff": "",
    "hfp": "",
    "loginfrom": "",
    "mainpageflag": "1",
    "pagerefer": "https://m.weibo.cn/",
    "password": 'xx21uc0xdc',
    "qq": "",
    "r": "https://m.weibo.cn/",
    "savestate": "1",
    "username": 'zibi69117shaokui@163.com',
    "wentry": "",
}
resp = requests.post('https://passport.weibo.cn/sso/login', data=data, headers=headers)
jdata = json.loads(resp.text)
print(jdata)
        # if jdata['retcode'] == 20000000:


# print(json.loads('{"code":"100003","msg":"\u53c2\u6570\u9519\u8bef"}'))