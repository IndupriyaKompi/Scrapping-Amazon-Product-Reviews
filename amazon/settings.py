# Scrapy settings for amazon project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scraper_helper as sh

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amazon (+http://www.yourdomain.com)'
AUTOTHROTTLE_ENABLED = True
#USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)	'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = sh.get_dict(
    '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cookie: session-id=131-9263253-6738542; ubid-main=135-5881335-3029945; x-main="1wc3mxYwVBXuCmy91QOyNP3N5nA2K0JcbzX2wDQtTb?NKL7cAF5qHbOjdqUg105@"; at-main=Atza|IwEBIGbOnNihZ3awpW9-qqmKXwDqr8rq44TvX1d4NaEPxIbZvNPTuKdvdM0bphEiez5yDHkAkY753yPT0tDaXdxlaV7J6pgKjXIPQMzVjePZKLxhnZZmy2ayHZG2wmobG9rJv8XTYVV7ZMck7nAGT6FHLONjrCngp5NwTKn_020ZkJfqNNMsjyySPneK-DnzdQFTglldGpxr3mUU65skgst16o28; sess-at-main="fmvC+dGP1370T6bcP39k5ivsgS1pInTtKv4Q1p+Oi0k="; sst-main=Sst1|PQEnuFtRnAkFkaKXbDz7r4N9Cfipq9UhKtWO2Gi-srPvMVG0D5Dvd_gn6F0zGZ2TwC2vvp2jyW-fxYmoefOaXPwSnPkACYv_AswFSj6sxnHl4f9R5b7f4MUsYowB5ok1U-gL0IMxSQ_uBHEDnnimQaSIUVPujrdtnU3Zl47D_RFYbr94Zl-v39K4oWOUNQrY6Vz6Tsynd9od7GQsQmczN4-TweS8SGW1ix6-GlxjnVfsNWth2cyhFV9e_RZsv0L-irwR4Y-Zn1NUamqgAxzORi6DXnq7tHQDyLYLu62zXgIle-M; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; session-token=nOR2Pc8Zf0/FoAU9pW/+umRahsu5WGimAWiHDDXJ5UvSVBvGu0HPSN9qF+eHZosG3SPfFHoDskaWe9Kk6O8gJOfM1zzYmtloIhI3QLQQ45Cfjzel2RHNwlS5Du7IeCD1U0KEoMAOrEig+rhJ7AGhLuFg2Gee3puQaeB1Yl/2sfb0dsPA8nb9x1llbWIB7uJiOMR7Qmq5+etEzvPUfha0dZY2bjGTdxzT/trPOu0iDIHe2UbqqDzbOPSMpr2liVblc0ouyvZ85KHEO8Yo+OERQg==; csm-hit=tb:CKDSG13H3RMYVPPW0EMC+s-K8V9SV3NN264SKFD06MS|1614550892414&t:1614550892414&adb:adblk_no
downlink: 5.5
ect: 4g
rtt: 50
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36
''')

