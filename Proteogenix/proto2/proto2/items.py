# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Proto2Item(scrapy.Item):
    Product_brand=scrapy.Field()
    Product_name=scrapy.Field()
    Product_type=scrapy.Field()
    Product_info = scrapy.Field()
    Product_price=scrapy.Field()
    Product_url=scrapy.Field()
    pass
