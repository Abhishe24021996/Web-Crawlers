# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovusbioItem(scrapy.Item):
    # define the fields for your item here like:

    # name = scrapy.Field()
#dor novu
    #Product_item_no = scrapy.Field()
    #Product_name = scrapy.Field()
    #Product_qauntity = scrapy.Field()
    #Product_url = scrapy.Field()
#for novu_s1
    Item_no = scrapy.Field()
    Name = scrapy.Field()
    Quantity = scrapy.Field()
    Description =scrapy.Field()
    Alt_names = scrapy.Field()
    Papers = scrapy.Field()
    Url = scrapy.Field()
    Immunogen = scrapy.Field()
    Specificity =scrapy.Field()
    Source =scrapy.Field()
    Clonality =scrapy.Field()
    Host =scrapy.Field()
    Dilutions =scrapy.Field()
    Application_Notes = scrapy.Field()
    pass
