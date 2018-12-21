# -*- coding: utf-8 -*-
import scrapy
print("M"*200)
print("M"*200)
import logging
print(logging)
import gevent
import time
import asyncio

from twisted.internet import reactor, defer

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']
    print("7777777777777777777")

    def __init__(self):
        print("bbbbbbbbbbbb")

    def start_requests(self):
        """
            hahahhahah
        """
        print("fucked up")
        print("time:  ..........")
        time.sleep(1)
        # print("gevent:  ..........")
        # gevent.sleep(1)


        yield scrapy.Request(self.start_urls[0], self.parse)





    def parse(self, response):
        """
            hahahhahah
        """
        #此处可以用self.logger是因为继承了父类，父类已经定义了self.logger = logging.LoggerAdapter
        print(dir(self))
        self.logger.debug("===============================")
        print(type(self.logger))
        print("xxxxxxxx")
        self.logger.debug(response.text)
        self.logger.debug("*"*80 + "\n\n\n")
        print(dir(response))
        print(response.url)
        print(response.headers)
        print(response.meta)
