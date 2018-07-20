import pymongo
import time


client = pymongo.MongoClient('209.182.233.211', 27000)
db = client['PornHub']
item_list = db["PhResHot"]

while True:
    # 实时监测URL条数
    # print(url_list.find().count())
    # 实时监测信息条数
    print(item_list.find().count())
    time.sleep(3)
