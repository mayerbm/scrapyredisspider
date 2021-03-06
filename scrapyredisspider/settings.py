# -*- coding: utf-8 -*-

# Scrapy settings for scrapyredisspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapyredisspider'

SPIDER_MODULES = ['scrapyredisspider.spiders']
NEWSPIDER_MODULE = 'scrapyredisspider.spiders'

# 使用scrapy-redis去重组件(使用redis的set存储请求的指纹数据),取代scrapy默认去重方法
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis调度器组件(将请求对象存储到redis),取代scrapy默认调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置调度器持久化：redis请求记录不丢失,就是当爬虫结束了,要不要清空Redis中请求队列和去重指纹的set,True表示不清空
SCHEDULER_PERSIST = True
# 默认的scrapy-redis请求队列形式(按优先级)
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列形式，请求先进先出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈形式，请求先进后出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyredisspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3  # 下载延迟：下载下一个页面时需要等待的时间
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 有些网站会追踪cookie值做反爬虫,通常可以禁掉,必须登录才能访问的网站可以在**spider类中添加custom_settings = {"COOKIES_ENABLED": True}
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapyredisspider.middlewares.scrapyredisspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scrapyredisspider.middlewares.scrapyredisspiderDownloaderMiddleware': 543,
   'scrapyredisspider.middlewares.RandomUserAgent': 100,
   'scrapyredisspider.middlewares.RandomProxy': 200,
   # 'scrapyredisspider.middlewares.SeleniumMiddleware': 300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 将数据存储到本地文件/mysql
   # 'scrapyredisspider.pipelines.ItcastPipeline': 300,
   # 'scrapyredisspider.pipelines.TencentspiderPipeline': 300,
   # 'scrapyredisspider.pipelines.SunwzspiderPipeline': 300,
   # 'scrapyredisspider.pipelines.JianshuspiderPipeline': 300,
   # 'scrapyredisspider.pipelines.JianshuTwistedspiderPipline': 300,
   # 'scrapyredisspider.pipelines.SoyoungspiderPipeline': 300,
   # 'scrapyredisspider.pipelines.SoufangspiderPipeline': 300,

   # 将数据存储到redis
   'scrapy_redis.pipelines.RedisPipeline': 301
}

# 指定redis连接信息
# REDIS_URL = "redis://root:redis666@192.168.19.11:6379"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
