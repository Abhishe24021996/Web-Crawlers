# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoleculardevicesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Pro_name = scrapy.Field()
    Product_name = scrapy.Field()
    Product_no = scrapy.Field()
    Product_url = scrapy.Field()
    pass
