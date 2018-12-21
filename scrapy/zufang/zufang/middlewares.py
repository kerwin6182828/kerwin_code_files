# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

print("!"*200)
print("!"*200)

# class ZufangSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#     print("("*200)
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         print("!"*200)
#         print(crawler)
#         print(dir(crawler))
#         print(crawler.settings)
#         print(crawler.stats)
#         print(crawler.signals)
#         print(crawler.spider)
#         print("!"*200)
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         print("U"*200)
#         print(self)
#         print(dir(self))
#         print("U"*200)
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         print("H"*200)
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     # def spider_opened(self, spider):
#     #     print("我要open啦1！！")
#     #     spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class ZufangDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#     print("f"*200)
#
#     def __init__(self):
#         print("我的天啊！！！！！！！！！！！！！！！！！！")
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         print("F"*200)
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         print("h"*200)
#         print(dir(request))
#         print(request.cookies)
#         print("h"*200)
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     # def spider_opened(self, spider):
#     #     print("我要open啦2！！")
#     #     spider.logger.info('Spider opened: %s' % spider.name)



class RandomUserAgentMiddleware():
    print("T"*200)
    def __init__(self):
        self.user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        ]
        print("!"*200)

    def process_request(self, request, spider):
        # print("@"*100, "\n\n")
        # print(request, "---", dir(request),"\n\n")
        request.headers["User-Agent"] = random.choice(self.user_agents)
        request.headers["Host"] = "hz.lianjia.com"
        print("\n\n已获取 ua、host \n\n")



class CookiesMiddleware():

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(cookies_url=settings.get("COOKIES_URL"))

    def __init__(self, cookies_url):
        self.logger = logging.getLogger(__name__)
        # self.logger = logging.LoggerAdapter
        self.cookies_url = cookies_url
        cookies = {}
        # 此处为“链家”的cookies
        # cook = "TY_SESSION_ID=60da3186-be47-41c9-a7a2-24ce9ffbf180; select_city=330100; all-lj=979909237fcf62bcb16b5a6dbd3b060f; lianjia_ssid=bd5e3199-c976-410d-b1d2-0b4a18f49739; lianjia_uuid=cc1cdd06-d680-49d4-a41f-f388862cc74a; _smt_uid=5c04f1d0.20252aa8; UM_distinctid=16773509840604-0cfa6fc01bcdb4-594d2a16-100200-167735098411b0; CNZZDATA1253492436=1496893322-1543827870-https%253A%252F%252Fhz.lianjia.com%252F%7C1543827870; CNZZDATA1255633284=641207234-1543826277-https%253A%252F%252Fhz.lianjia.com%252F%7C1543826277; CNZZDATA1255604082=1476813366-1543826557-https%253A%252F%252Fhz.lianjia.com%252F%7C1543826557; _qzjc=1; _jzqa=1.1892224079188652000.1543827921.1543827921.1543827921.1; _jzqc=1; _jzqx=1.1543827921.1543827921.1.jzqsr=hz%2Elianjia%2Ecom|jzqct=/zufang/xihu/.-; _jzqckmp=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1541923285,1541923676,1542015724,1543758078; _ga=GA1.2.970605415.1543827924; _gid=GA1.2.125349423.1543827924; CNZZDATA1254525948=2116521402-1543822625-https%253A%252F%252Fhz.lianjia.com%252F%7C1543828025; _qzja=1.358922240.1543827921187.1543827921187.1543827921187.1543828028854.1543828141851.0.0.0.5.1; _qzjb=1.1543827921187.5.0.0.0; _qzjto=5.1.0; _jzqb=1.5.10.1543827921.1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1543828142; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1"
        # 此处为“我爱我家”的cookies
        cook = "_Jo0OQK=699568B43362FE544E1653A6ECBEAB69BE6AAC84E2CC7DF59A742843BA8D329CD3E0FDFF18143DD3165041DB345E0D93418D6F9BA753E6F03B65B6E28007E2A4B2F9FC0DF34BBE505AF02631C467319B15B02631C467319B15B869297F6895F5D91GJ1Z1OA==; PHPSESSID=renrc3k1o36tjfmau8ii57ive4; domain=hz; _ga=GA1.2.1378246401.1544003780; _gid=GA1.2.1786591736.1544003780; _gat=1; yfx_c_g_u_id_10000001=_ck18120517561918115191323121654; yfx_f_l_v_t_10000001=f_t_1544003779804__r_t_1544003779804__v_t_1544003779804__r_c_0; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1541923995,1543898127,1543991915; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544003781"
        for cookie in cook.split(";"):
            key, value = cookie.split("=", 1)
            cookies.update({key:value})
        self.fixed_cookies = cookies

    def process_request(self, request, spider):
        print("正在获取cookies")
        if self.cookies_url:
            try:
                response = requests.get(self.cookies_url)
                if response.status_code == 200:
                    cookies = json.loads(response.text)
                    request.cookies = cookies
                    print("使用远程随机cookies")
            except Exception:
                print("访问远程随机cookies失败。。。")
        else:
            request.cookies = self.fixed_cookies

        print("头部：", request.headers, "\n\n")
        print("曲奇:", request.cookies, "\n\n")
        print("\n\n请求已经发送。。。\n\n")









import logging
import requests
class ProxyMiddleware():

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(proxy_url=settings.get("PROXY_URL"), abuyun_proxies=settings.get("ABUYUN_PROXIES"))

    def __init__(self, proxy_url, abuyun_proxies):
        self.logger = logging.getLogger(__name__)
        # self.logger = logging.LoggerAdapter
        # 这个url是自己搭建的服务器的url，不是指阿布云！！
        self.proxy_url = proxy_url
        self.fixed_proxy = "http://127.0.0.1:1080"
        self.abuyun_proxies = abuyun_proxies

    def process_request(self, request, spider):
        print("正在获取proxy")
        if self.proxy_url:
            try:
                response = requests.get(self.proxy_url)
                if response.status_code == 200:
                    proxy = json.loads(response.text)
                    request.meta["proxy"] = proxy
                    print("使用远程随机proxy")
            except Exception:
                print("访问远程随机proxy失败。。。")
        elif self.abuyun_proxies:
            # scrapy 中添加代理的方式和requests库又不一样！！！！
            # scrapy只需要一个str即可，eg:"http://127.0.0.1:1080"
            # 而requests中是字典形式， eg：{"http":"http://127.0.0.1:1080"}
            request.meta["proxy"] = self.abuyun_proxies
            print("已使用阿布云代理ip")
        else:
            request.meta["proxy"] = self.fixed_proxies
