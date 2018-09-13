# !/usr/bin/env python3
# encoding: utf-8 
# Date  : 2018/9/12 9:50
# @Author : Rainflower 
# @Site : 
# @File : captcha_check.py
# @Software: PyCharm Community Edition
import base64
import json
import re
from io import StringIO
import requests
import js2py
import PIL.Image as image



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

session =requests.session()


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
resp = session.post('https://passport.weibo.cn/sso/login', data=data, headers=headers)
jdata = json.loads(resp.text)
print(jdata)
        # if jdata['retcode'] == 20000000:


# print(json.loads('{"code":"100003","msg":"\u53c2\u6570\u9519\u8bef"}'))

captcha_url = 'https://captcha.weibo.com/api/pattern/get?ver=daf139fb2696a4540b298756bd06266a&source=ssologin&usrname=zibi69117shaokui@163.com&line=160&side=100&radius=30&_rnd=0.30777878904566836&callback=pl_cb'
resp = session.get(captcha_url)
data = re.compile('\((.*?)\)').findall(resp.text)[0]
path_enc = json.loads(data)['path_enc']
print(path_enc)
# path_enc = 'data:image/gif;base64,R0lGODdhoACgAIQAAJSSlNTS1KyurOzq7KSipMTCxOTi5Pz6/JyanLS2tNza3PTy9KyqrJSWlNTW1LSytOzu7KSmpMTGxOTm5Pz+/JyenLy6vAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAoACgAAAF/iClABZlnmiqrmzrvnAsz3SNjomt73zv/65RCUgsGo88HHLJbC4VjaFzSq3GlNasNivcer9PQA5MLiej5rT6Kl673zcSfL7G0u9gqBTP57b7gFVdeA4AgVR2dwyHU3p9BoxOiZGUP4OVmD2TmZwzjp2gnn+hpEFypagrm6mon6yvq6+hl7Kto7WlrriksbuYtL4+DmW9wTMTDIbGyzMLCQ0ADWQK1NXW19jZ1kza3d7f2QkIAOQA4ApMDdDq0evu7fDs8u7p7/Px9vn4+9Dl5Pr3pC2xkICgwYIIDypMyJAgk4UQG0qMSDGBAAT9yCVAyJEgQmZ0HFRYBzLTAQnQ/kpycqaypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcp0isGnBaFakEo16pimJ/xp3cq1KzmsN86J3QaWBrsEEMoeARBhglokAd7KnUu3rt27ePPq3cu3r9+/gAMLHky4sOHDiBMrXsy4sWOXAQzGXWyhXIXJiQdQK4DGpa6Sn+8AY6agwKk+xXZBuxxo9DKCmFHfUhwacerBrg/fFlxb9+zEuQ3vDtxb+G/bpxcPB1y88PK/wZ0f192Z8XO/0Qlf79tc+/S5FhbUyK42moQDoq7itYzuSvWlU63Gn/8sGjkED+RLFfG9qNf/AH5FnlBirRNNAg58fsOferS9t4xmlGwXSmURJrdMAAwCIuFe3eHWn3d70PYhbg4CNyJvFpqYoW0lHlbOOisOllE04iVmHzQSLJaAZegptgA7wzC2o0CMOdDAA45tqNeAxKWIXIzCtegblNKFqGKSUgYzX1Vb6uflVE0oCUqAZHIVppPGjKVme0iEAAA7|NV81XzExXzIzXzE5XzVfMTJfMjRfMjFfMTBfMTZfMF83XzE3XzJfMV8yMF8xM180XzNfMTRfMTVfMjJfNl85XzhfMTg='

with open(r'{}.jpg'.format('bs64'), 'wb') as f:
    b = base64.b64decode(path_enc.replace('data:image/gif;base64,', ''))
    f.write(b)

print(path_enc.split("|")[1])


def read_js(path):
    with open(path, 'r') as f:
        stri = ''
        for line in f:
            stri += line
    return js2py.eval_js(stri)


base_64 = read_js(r'js_broke\base64decode.js')
getPostion = read_js(r'js_broke\getPostion.js')

c = base_64(path_enc.split("|")[1])
print(c)
print('--------------------')
print(path_enc, c.split('_'))
print(getPostion(path_enc, c.split('_')))
print(len(getPostion(path_enc, c.split('_'))))


def get_merge_image(filename, location_list):
    im = image.open(filename)
    im_list_upper = []
    im_list_down = []

    for location in location_list:
        if location['y'] == -58:
            im_list_upper.append(im.crop((
                abs(location['x']), 58,
                abs(location['x']) + 10, 58 + 58)))
        if location['y'] == 0:
            im_list_down.append(im.crop((
                abs(location['x']), 0,
                abs(location['x']) + 10, 0 + 58)))

    # 通过小图片合成新的图片
    new_im = image.new('RGB', (260, 116))

    # 图片左上角(0,0)
    # 上部分拼接
    x_offset = 0
    for im in im_list_upper:
        new_im.paste(im, (x_offset, 0))  # 将im 粘贴到new_im 位置(x_offset,0)
        x_offset += im.size[0]

    # new_im.save(pic_path+os.sep+'new_%s_upper.jpg' %flag)
    # 下部分拼接
    x_offset = 0
    for im in im_list_down:
        new_im.paste(im, (x_offset, 58))  # 将im 粘贴到new_im 位置(x_offset,58)
        x_offset += im.size[0]


    return new_im


def get_merge_image2(filename, location_list):
    im = image.open(filename)
    im_list = []


    for location in location_list:
        location_x, location_y =  map(int, location.split())

        im_list.append(im.crop((
            abs(location_x), abs(location_y),
            abs(location_x) + 32, abs(location_y) + 32)))

    # 通过小图片合成新的图片
    new_im = image.new('RGB', (160, 160))

    # 图片左上角(0,0)
    # 上部分拼接

    for index, im in enumerate(im_list):
        print((index%5*32, int(index/5) *32))
        new_im.paste(im, (index%5*32, int(index/5) *32))  # 将im 粘贴到new_im 位置(x_offset,0)


    # new_im.save(pic_path+os.sep+'new_%s_upper.jpg' %flag)
    # 下部分拼接

    new_im.save('new.jpg')
    return new_im

get_merge_image2('bs64.jpg', getPostion(path_enc, c.split('_')))

# -*- coding: utf-8 -*-

import os


def file_name(file_dir):
    pfiles = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            pfiles.append(os.path.join(root, file) ) # 当前目录路径
    print(pfiles)
    return pfiles
file_name('imgs')


im = image.open('new.jpg').convert('L')
width = im.size[0]
height = im.size[1]
ttype =''
for file_dir in file_name('imgs'):
    # print(file_dir)
# for png in ims.keys():
    png = image.open(file_dir).convert('L')
    isGoingOn = True
    for i in range(width):
        for j in range(height):
            if ((im.load()[i, j] >= 245 and png.load()[i, j] < 245) or (
                    im.load()[i, j] < 245 and png.load()[i, j] >= 245)) and abs(
                    png.load()[i, j] - im.load()[i, j]) > 50:  # 以245为临界值，大约245为空白，小于245为线条；两个像素之间的差大约10，是为了去除245边界上的误差
                isGoingOn = False
                break
        if isGoingOn is False:
            ttype = ''
            break
        else:
            ttype = file_dir
    else:
        break
print(ttype)