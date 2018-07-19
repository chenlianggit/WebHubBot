# -*- coding: utf-8 -*-

# pornhub项目的Scrapy设置
#
# 为简单起见，此文件仅包含被视为重要的设置或
# 常用。您可以在咨询文档时找到更多设置：
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WebHub'

SPIDER_MODULES = ['WebHub.spiders']
NEWSPIDER_MODULE = 'WebHub.spiders'

DOWNLOAD_DELAY = 1  # 间隔时间
# LOG_LEVEL = 'INFO'  # 日志级别
CONCURRENT_REQUESTS = 40  # 默认为16
# Twisted模块中Reactor最大线程池数量。
REACTOR_THREADPOOL_MAXSIZE = 40
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pornhub (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    "WebHub.middlewares.UserAgentMiddleware": 401,
    "WebHub.middlewares.CookiesMiddleware": 402,
}
ITEM_PIPELINES = {
    "WebHub.pipelines.PornhubMongoDBPipeline": 403,
}

# FEED_URI=u'/Users/xiyouMc/Documents/pornhub.csv'
# FEED_FORMAT='CSV'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
