# -*- coding:utf-8 -*-
import scrapy

#
class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = [
        "https://passport.csdn.net/account/login?ref=toolbar"
    ]

    def parse(self, response):
        #得到请求中需要的登录流水号
        lt = response.xpath("//input[@name='lt']/@value").extract()[0]
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                "username":"15682808270",
                "password":'DAMUpython2016',
                'lt':lt
            },
            callback = self.parse_response
        )
    def parse_response(self,response):
        with open("csdn.html",'w') as f:
            f.write(response.body)

