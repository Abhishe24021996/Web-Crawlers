# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReageconItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Product_item_no = scrapy.Field()
    Product_name= scrapy.Field()
    Product_price = scrapy.Field()
    Product_wght = scrapy.Field()
    Product_packsize = scrapy.Field()
    Product_value = scrapy.Field()
    Product_mfr_no = scrapy.Field()
    Product_url = scrapy.Field()
    pass
