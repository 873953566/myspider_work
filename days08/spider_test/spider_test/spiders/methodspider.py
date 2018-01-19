# -*- coding:utf-8 -*-

import scrapy

class GetSpider(scrapy.Spider):

    name = 'getspider'
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://www.baidu.com"

    ]
    def parse(self, response):
        pass

class PostSpider(scrapy.Spider):
    name = 'postspider'
    allowed_domains = ['reren.com']
    start_urls = [
        "http://www.renren.com/login"
    ]
    def start_requests(self):
        # return scrapy.Request(self.start_urls[0],method="POST")
        return scrapy.FormRequest(
            self.start_urls[0],
            formdata={"username":"admin","password":"123"},
            callback = self.parse_response()
        )
    def parse_response(self,response):
        pass

















