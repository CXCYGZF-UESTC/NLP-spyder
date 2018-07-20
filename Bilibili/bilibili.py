#url：https://www.bilibili.com/
#Description：B站 关注 弹幕 评论 收藏
#Dependencies：urllib.request；requests；ssl；re；time
#Operation：输入参数：av_num，为所需要操作的视频的AV号；发送用户设置：headers、headers1、csrf，通过更改cookie可以修改发送请求的用户
#2018.3.25
#孙小柒
#Var：1.0（这个还有很多可以改进的东西的呦）
#构建请求头文件（记得删除encoding）

import urllib.request
import requests
# import urllib.parse
import ssl
import re
# import json
# import unicodedata
import gzip
import random
from time import sleep

ssl._create_default_https_context = ssl._create_unverified_context

post_url = 'https://api.bilibili.com/x/v2/dm/post'
av_num = '25340825'
sourse_url = 'https://www.bilibili.com/video/av'+av_num

print(sourse_url)

headers = {
    'Accept':'*/*',
    #'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    #'Content-Length':'165',
    #'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',

    #cookie 无法获取
    'Cookie':'fts=1521028517; sid=54ksfb0l; UM_distinctid=162245f17cf19c-03aadf44092d6-c343567-1fa400-162245f17d05e0; buvid3=B471181E-000A-4E0D-8CD3-48625B0A980E13492infoc; rpdid=kmikkoqiomdosiiqswoww; LIVE_BUVID=b3646b181684e94e81ed9d9b823f90fa; LIVE_BUVID__ckMd5=7e031db19d85b75a; finger=edc6ecda; DedeUserID=301118390; DedeUserID__ckMd5=3823c25f37f04b15; SESSDATA=6943b960%2C1532189656%2Cb09c98c1; bili_jct=9cb094853d3f846bddb3fe0040cd55c8; _dfcaptcha=4f8f0b45c4417d71147e3a8e37917931',
    'Host':'api.bilibili.com',
    'Origin':'https://www.bilibili.com',
    'Pragma':'no-cache',
    'Referer':sourse_url,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
}

headers1={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'92',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'fts=1521028517; sid=54ksfb0l; UM_distinctid=162245f17cf19c-03aadf44092d6-c343567-1fa400-162245f17d05e0; buvid3=B471181E-000A-4E0D-8CD3-48625B0A980E13492infoc; rpdid=kmikkoqiomdosiiqswoww; LIVE_BUVID=b3646b181684e94e81ed9d9b823f90fa; LIVE_BUVID__ckMd5=7e031db19d85b75a; finger=edc6ecda; DedeUserID=301118390; DedeUserID__ckMd5=3823c25f37f04b15; SESSDATA=6943b960%2C1532189656%2Cb09c98c1; bili_jct=9cb094853d3f846bddb3fe0040cd55c8; _dfcaptcha=4f8f0b45c4417d71147e3a8e37917931',
    'Host':'api.bilibili.com',
    'Origin':'https://www.bilibili.com',
    'Pragma':'no-cache',
    'Referer':sourse_url,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
}
#获取oid
source_code = urllib.request.urlopen(url=sourse_url).read()
source_code =gzip.decompress(source_code).decode("utf-8")#gzip解码
oid = re.findall(';cid=(.*?)&am',str(source_code))[0]
fid = re.findall('{"mid":(.*?),',str(source_code))[0]#关注up主的id

print(oid)
print(fid)

##构建post请求的postdata
danmu_list=['up辛苦了','up真的很有想法啊','来了','弹幕支持','666666','2333333','QAQ','QWQ','爱你呦up主','等候多时','失踪人口回归','终于更新了','跪着来看up的视频','喵喵喵？？？？','好可爱哈哈',]
for i in range(1):
    post_time = str(random.randint(1,200000))
    post_data = {
        'type':'1',
        'oid':oid,
        'msg':random.choice(danmu_list),
        'aid':av_num,
        'progress':post_time,
        'color':'16777215',
        'fontsize':'25',
        'pool':'0',
        'mode':'1',
        'rnd':'1522917651750137',
        'plat':'1',
        'csrf':'9cb094853d3f846bddb3fe0040cd55c8',#(cookie中的数据)
    }

    response_data = requests.post(url=post_url,data=post_data,headers=headers)
    print(response_data)
    sleep(random.randint(6,10))
# #创建收藏夹

# add_data0 = {
#     'name':av_num,#创建一个和AV号一样的收藏夹
#     'jsonp':'jsonp',
#     'csrf':'9cb094853d3f846bddb3fe0040cd55c8'
# }
# response_data = requests.post(url='https://api.bilibili.com/x/v2/fav/folder/add',data=add_data0,headers=headers1)
# print(response_data.content.decode())
# sc_fid = re.findall('fid":(.*?)}}',response_data.content.decode())#收藏文件夹的fid
# print(sc_fid)
# #自动收藏

add_data1 = {
    'aid':av_num,
    'fid':'1610462',#sc_fid[0],
    'jsonp':'jsonp',
    'csrf':'9cb094853d3f846bddb3fe0040cd55c8',
}
response_data = requests.post(url='https://api.bilibili.com/x/v2/fav/video/add',data=add_data1,headers=headers1)
print(response_data)
#自动评论

add_data2 = {
    'oid':av_num,
    'type':'1',
    'message':'关注啦~~',
    'plat':'1',
    'jsonp':'jsonp',
    'csrf':'9cb094853d3f846bddb3fe0040cd55c8',
}
response_data = requests.post(url='https://api.bilibili.com/x/v2/reply/add',data=add_data2,headers=headers1)
print(response_data)
# #自动关注

modify_data = {
    'fid':fid,
    'act':'1',
    're_src':'14',
    'cross_domain':'true',
    'csrf':'9cb094853d3f846bddb3fe0040cd55c8',
}
response_data = requests.post(url='https://api.bilibili.com/x/relation/modify',data=modify_data,headers=headers1)
print(response_data)
