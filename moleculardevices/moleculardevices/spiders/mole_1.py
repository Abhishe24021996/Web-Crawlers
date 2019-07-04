# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import MoleculardevicesItem


class MoleSpider(scrapy.Spider):
    name = 'mole_1'
    allowed_domains = ['www.moleculardevices.com']
    start_urls = ['https://www.moleculardevices.com/sitemap#gref/']

    def parse(self, response):
        product_links = set(response.xpath('//div[contains(@class,"col-sm-4")]/ul/li/a/@href').getall())
        for link in product_links:
            if re.search('^(/products/).+',link):
                link = 'https://www.moleculardevices.com' + link
                yield scrapy.Request(link, self.parse_product)

    def parse_product(self, response):
        items = MoleculardevicesItem()
        pro_name = response.xpath('//div[contains(@class,"col-md-12 col-xs-12")]/h1/span/text()').getall()
        product_url = response.url
        for name , url in zip(pro_name, product_url):
            items['Pro_name'] = name
            items['Product_url'] = product_url
            yield items
