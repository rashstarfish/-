# Scrapy settings for xiecheng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiecheng'

SPIDER_MODULES = ['xiecheng.spiders']
NEWSPIDER_MODULE = 'xiecheng.spiders'
LOG_FILE = 'log.txt'
LOG_LEVEL_SCRAPY = 'ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiecheng (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
AUTOTHROTTLE_ENABLED = True

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
   'Accept': '*/*',
   'Connection': 'keep-alive',
   'Cookie':'_RGUID=17dccfa5-6d66-4019-83e1-94a939bbe159; _RSG=P0aPjLwpSV1P5.kvaAbXF8; _RDG=28789c7a7099a32a3c139d741e205c2f7e; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; librauuid=; UBT_VID=1731870872391.7982GbltiNh1; GUID=09031022110432428463; MKT_CKID=1731870872558.7a9el.71dr; cticket=4CEF402A0ADCBFE8C54978C7F388EB00E7690F6EA93BA34CAC5356F5674B31D8; login_type=0; login_uid=9C1E14FEB47C16D1689CA018AC289F50C40D403AA481726BA97CCB35FE9DBC54F71F3B9C37186641CF0E12A395AFFBFA; DUID=u=EC1294F6558871976B6641E099F6CD72&v=0; IsNonUser=F; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; nfes_isSupportWebP=1; Hm_lvt_a8d6737197d542432f4ff4abc6e06384=1731751878,1731815897,1731872587,1731877826; HMACCOUNT=11C5B93F89CAEC7F; _ga=GA1.1.78898264.1731877827; _RF1=240e%3A478%3A4228%3A1839%3A355e%3Aa2f6%3Ad03e%3A8854; _ga_9BZF483VNQ=GS1.1.1731877826.1.0.1731877827.0.0.0; _ga_5DVRDQD429=GS1.1.1731877826.1.0.1731877827.0.0.0; _ga_B77BES1Z8Z=GS1.1.1731877826.1.0.1731877827.59.0.0; MKT_Pagesource=PC; Hm_lpvt_a8d6737197d542432f4ff4abc6e06384=1731880548; _jzqco=%7C%7C%7C%7C1731870872672%7C1.649184718.1731870872560.1731880599269.1731881519037.1731880599269.1731881519037.0.0.0.25.25; intl_ht1=h4=7_118852849,7_119017405,21916_113012257,3_117931184,3_1316004,2_72789489; _bfa=1.1731870872391.7982GbltiNh1.1.1731881518586.1731881813277.2.13.102003'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xiecheng.middlewares.XiechengSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xiecheng.middlewares.XiechengDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiecheng.pipelines.XiechengPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
