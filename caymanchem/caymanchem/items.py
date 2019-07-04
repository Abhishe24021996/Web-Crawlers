# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaymanchemItem(scrapy.Item):
    #Product_url = scrapy.Field()
    Catalog = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()
    Formal_name = scrapy.Field()
    Alternative_name = scrapy.Field()
    Additional_info = scrapy.Field()
    Url = scrapy.Field()
    pass
