# -*- coding:utf-8 -*-
import pymongo
import time
import os

client = pymongo.MongoClient('209.182.233.211', 27000)
db = client['PornHub']
item_list = db["PhResHot"]


# for item in item_list.find({'link_url':"https://www.pornhub.com/view_video.php?viewkey=ph5b1872a48fa12"}):


def downmp4(url):
    p = os.popen("./sh.sh \"" + url + "\" ")
    x = p.readlines()
    for line in x:
        line = line.strip().replace("\n", "")  # 去空格去换行
        host = "ty2050"
        print line
        if line == 'success':
            print("----成功抓取一条----")
        if host in line:
            return host


for item in item_list.find():
    print(item['quality_480p'])
    print("----new 开始抓取----")
    url = item['quality_480p']
    host = downmp4(url)
    item_list.update({"quality_480p": url}, {'$set': {"age": 20}})