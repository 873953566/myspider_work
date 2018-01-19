# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilianItem(scrapy.Item):
    """
    定义采集数据的内容，该类型中，会封装采集到的数据
      继承scrapy.Item.
    """
    job = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
