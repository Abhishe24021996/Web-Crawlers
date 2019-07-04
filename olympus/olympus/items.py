# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OlympusItem(scrapy.Item):
    Product_name=scrapy.Field()
    Product_model=scrapy.Field()
    Product_categ=scrapy.Field()
    Product_descr=scrapy.Field()
    Product_url=scrapy.Field()
    Product_imgsrc=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
