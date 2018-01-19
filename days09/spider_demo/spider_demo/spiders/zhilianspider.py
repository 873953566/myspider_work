# -*- coding:utf-8 -*-


"""
深度爬虫scrapy.spider.CrawlSpider
"""
import scrapy
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor



class ZhilianSpider(CrawlSpider):

    """
    基于CrawlSpider的爬虫程序
    """
    name = "zl"
    allowed_domains = ["zhaopin.com"]
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2b%E4%B8%8A%E6%B5%B7%2b%E5%B9%BF%E5%B7%9E%2b%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=7cd76e75888443e6b906df8f5cf121c1&p=1"
    ]
    #连接的提取规则
    link_extractor = LinkExtractor(allow="121c1&p=\d+")
    rules = [
        Rule(link_extractor,follow=True,callback='parse_response'),

    ]

    #注意 ： 不能重写parse函数
    #因为在父类中已经重写过了parse函数，如果再写，就会失效
    def parse_response(self,response):
        #处理相应数据
        #提取当前页的所有工作列表
        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")
        # 循环获取采集的字段信息
        for job in job_list:
            # 岗位名称
            job_name = job.xpath("td[@class='zwmc']/div/a").xpath("string(.)").extract()[0]
            # 公司名称
            company = job.xpath("td[@class='gsmc']/a").xpath("string(.)").extract()[0]
            # 薪水
            salary = job.xpath("td[@class='zwyx']").xpath("string(.)").extract()[0]
            print job_name



