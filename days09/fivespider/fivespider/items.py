# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from sched import scheduler

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst,Join


class FivespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FiveItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    quality = scrapy.Field()
    area = scrapy.Field()
    UrlofPage = scrapy.Field()

class FiveLoader(ItemLoader):
    default_item_class = FiveItem
    default_input_processor = MapCompose(lambda s:s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()


