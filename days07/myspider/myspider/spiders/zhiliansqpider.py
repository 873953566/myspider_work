# -*- coding:utf-8 -*-

#引入需要的模块
import scrapy
from .. import items

class ZhilianSpider(scrapy.Spider):
    """
    智联招聘数据采集程序
    """
    #定义爬虫名称，用于在命令中调用
    name = 'zlspider'

    allowed_domains = ['zhaopin.com']
    #起始url地址
    start_urls = [
        # 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&isadv=0&sg=9b23e91bf8d34b89933f2bfbeabef7dd&p=1',
        # 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&isadv=0&sg=9b23e91bf8d34b89933f2bfbeabef7dd&p=2',
        # 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&isadv=0&sg=9b23e91bf8d34b89933f2bfbeabef7dd&p=3',
        # 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&isadv=0&sg=9b23e91bf8d34b89933f2bfbeabef7dd&p=4',
        # 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&isadv=0&sg=9b23e91bf8d34b89933f2bfbeabef7dd&p=5',
        # 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&isadv=0&sg=9b23e91bf8d34b89933f2bfbeabef7dd&p=6',
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=1",
    ]


    def parse(self, response):
        """
        采集到数据后，自动执行的函数进行以下功能
        响应数据解析函数
            用于进行响应数据的筛选，筛选目标数据
        :param response:采集到的数据
        :return:
        """
        # print response
        # filename = response.url.spilt('&')[-1] + '.html'
        # with open(filename,'w') as f:
        #     f.write(response.body)
        # filename = response.url.split("&")[-1] + ".html"
        # with open(filename, "w") as f:
        #     # 爬虫采集到的数据，会封装在response.body属性中，可以直接获取
        #     f.write(response.body)

        job_items = []

        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")

        #循环采集数据
        for select in job_list:
            # print '#' *60
            job = select.xpath("td[@class='zwmc']/div/a").xpath("string(.)").extract()[0]
            company = select.xpath("td[@class='gsmc']/a").xpath("string(.)").extract()[0]
            salary = select.xpath("td[@class='zwyx']").xpath("string(.)").extract()[0]
            # print job
            #将数据复制给item对象
            item = items.ZhilianItem()
            item['job'] = job
            item['company'] = company
            item['salary'] = salary
            # job_items.append(item)

        # return job_items
            yield item


