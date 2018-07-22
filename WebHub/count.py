# -*- coding:utf-8 -*-
import pymongo
import time


client = pymongo.MongoClient('209.182.233.211', 27000)
db = client['PornHub']
item_list = db["PhResHot"]
# for item in item_list.find({'link_url':"https://www.pornhub.com/view_video.php?viewkey=ph5b1872a48fa12"}):
for item in item_list.find({"issave":1}):
    print(item['quality_480p'])
    # item_list.update({"quality_480p": item['quality_480p']}, {'$set': {"issave": 0}})
    print("\n")
    # print(item['image_url'])
    # print(item['quality_480p'])


# while True:
    # 实时监测URL条数
    # print(url_list.find().count())
    # 实时监测信息条数
    # print(item_list.find())
    # time.sleep(3)
