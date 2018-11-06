# -*- coding: utf-8 -*-

"""Scrapy settings for makeupalley project"""

BOT_NAME = 'makeupalley'

SPIDER_MODULES = ['makeupalley.spiders']
NEWSPIDER_MODULE = 'makeupalley.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
#CONCURRENT_REQUESTS_PER_IP = 16

# Cookies
COOKIES_ENABLED = True

# Telnet Console
TELNETCONSOLE_ENABLED = True

# Item pipelines
ITEM_PIPELINES = {
    'makeupalley.pipelines.StarReviewsCounterPipeline': 300,
}

# Retry configuration
RETRY_TIMES = 50

HTTP_RETRY_CODES = [500, 502, 503, 504, 400, 403, 408]

# Enable and configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 5
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
