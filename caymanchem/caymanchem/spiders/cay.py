# -*- coding: utf-8 -*-
import scrapy
from ..items import CaymanchemItem
import re


class CaySpider(scrapy.Spider):
    name = 'cay'
    allowed_domains = ['www.caymanchem.com']
    start_urls = ['https://www.caymanchem.com/SiteMap/']

    def parse(self, response):
        items=CaymanchemItem()
        links=set(response.xpath("//a/@href").getall())
        for link in links:
            if re.search("^(/product/).+",link):
                url='https://www.caymanchem.com'+ link
                items['Product_url'] = url
                yield items
            elif re.search('^(https://www.caymanchem.com/product/).+'):
                items['Product_url'] = url
                yield items

            yield scrapy.Request(url, self.parse)
