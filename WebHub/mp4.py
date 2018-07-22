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
            return line
def get_url():
    starttime = int(time.time()) - 60 * 60
    print starttime
    for item in (item_list.find({'issave': 0, 'createtime': {"$gte": starttime}}).limit(1)):
        if item['quality_480p']:
            return item['quality_480p']
        else:
            return False


while True:
    url = get_url()
    if url:
        print("----new 开始抓取----")
        print(url)
        host = downmp4(url)
        item_list.update({"quality_480p": url},{'$set': {"local_mp4_url": host, "issave": 1, "updatetime": int(time.time())}})
    else:
        print("休息10秒")
        time.sleep(10)