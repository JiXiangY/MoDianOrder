#https://photo.weibo.com/photos/get_all?uid=6528097052&album_id=4417211515268649&count=32&page=2&type=3&__rnd=1602554516934 微博图片广场 接口
#https://photo.weibo.com/photos/get_all?count=32&page=12&type=3&uid=6528097052
#https://photo.weibo.com/6528097052/wbphotos/large/photo_id/4541938807472179/ 大图接口 不需要
#https://wx1.sinaimg.cn/large/0077NefWgy1gi3fkhmby9j30u015lq73.jpg  图片地址
# -*- coding: utf-8 -*-

import requests
import urllib
import hashlib
import time
import datetime
import os
# import json
# 消去https请求的不安全warning
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

   


def downLoadImage(imageLists,path):
    i = 0
    count = len(imageLists)
    while i < count:
        item      = imageList[i]
        imageID   = item['photo_id']
        imageName = item['created_at'] + " " + imageID
        pic_name  = item['pic_name']
        pic_host  = item['pic_host']
        imageUrl = pic_host + "/large/" + pic_name
        try:
            r = requests.get(imageUrl)
            #保存图片
            with open('{}/{}.jpg'.format(path,imageName),'wb') as f:
                f.write(r.content) 
        except:
            print("已下载图片 {} 失败 重新下载".format(imageName))
            continue
        i += 1
        print("已下载图片 {}".format(imageName))
    print("下载完成")



def save():
    # 判断目录是否存在
    if not os.path.exists(os.path.split(path)[0]):
        # 目录不存在创建，makedirs可以创建多级目录
        os.makedirs(os.path.split(path)[0])
    try:
        # 保存数据到文件
        with open(path, 'wb') as f:
            f.write(html.encode('utf8'))
        print('保存成功')
    except Exception as e:
        print('保存失败', e)




def getImageID(userID,cookie):
    prefix_list_url = "https://photo.weibo.com/photos/get_all?count=32&type=3&uid={}&&page={}"
    list_header = {
        "cookie": cookie,
        "Cookie": cookie,
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    i = 1
    sum_imageList = []
    while(i!=0):
        response = requests.get(prefix_list_url.format(userID,i),headers=list_header)
        response_json = response.json()
        if int(response_json['result']) != True:
            print("下载列表失败")
        data = response_json['data']
        imageList = data["photo_list"]
        if len(imageList) == 0:
            i == 0
            print("下载图片列表第{}页为空".format(i))
            print("图片列表下载完成")
            break
        print("下载图片列表第{}页".format(i))
        sum_imageList = sum_imageList + imageList
        i += 1
    return sum_imageList

    

userID = '5880066726'
cookie =  "SINAGLOBAL=2981512225072.98.1583803257294; _s_tentry=login.sina.com.cn; Apache=2148300458442.729.1601172229290; ULV=1601172229298:25:4:1:2148300458442.729.1601172229290:1601092532038; YF-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; XSRF-TOKEN=Ahcp68lhEagfbrDng8VgLF6f; login_sid_t=9b1e05463a10ce595933f8a8380ba4ce; cross_origin_proto=SSL; wb_view_log_1573330832=1920*10801; SCF=ArdJBzpmCCfiS9auihwRzceLhHQWnFUTWiUoVZ8Fc2TRZ9jNbH0_CMAdfp0ykcrzZx6ERjvGE4Alp-SJoSusXIU.; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFP6a8-DNgmKsm8B3Nl4nvx5JpX5KzhUgL.Fo2fS0e0e05Re0z2dJLoI0qLxK-L1K5L1h.LxKMLBK-LBK-LxKqL1KnLB-qLxKBLBonL1hMLxKnL1heLB.BLxKML1-2L1hBt; SSOLoginState=1602575149; SUB=_2A25ygSsWDeRhGedL7FES8y7EyD6IHXVR9xverDV8PUNbmtCOLRLGkW9NVKzpJTO9Igv3JbnZ5EQrdklF_MVZw8Y-; SUHB=03oUH8ncSqNWIZ; ALF=1634111175; wvr=6; UOR=,,www.baidu.com; webim_unReadCount=%7B%22time%22%3A1602575924935%2C%22dm_pub_total%22%3A7%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A41%2C%22msgbox%22%3A0%7D"
imageList = getImageID(userID,cookie)
print(len(imageList))
path = os.getcwd()
print('path = ' + path)
have_book = os.path.exists(userID)
if have_book == False:
    os.mkdir(userID)
path = path + "/" + userID
downLoadImage(imageList,path)