# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import MoleculardevicesItem


class MoleSpider(scrapy.Spider):
    name = 'mole'
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
        order = response.xpath('//div[@class="tab-pane fade" and @id="Order"]').getall()
        ordering =response.xpath('//div[@class="tab-pane fade orderoptions" and @id="Orderingoptions"]').getall()
        if order:
            #product_name = response.xpath('//div[@class="tab-pane fade" and @id="Order"]/div/div/div[contains(@class,"container")]/div/div/table/tbody/tr/td[contains(@class,"rteleft")]/p/text()').getall()
            product_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "rteleft", " " ))]').getall()
            product_no = response.css('tr~ tr+ tr td+ td div , .rteleft+ td p::text').getall()
            for pro, name , no in zip(pro_name*len(product_name), product_name, product_no):
                items['Pro_name'] = pro
                items['Product_name'] = name
                items['Product_no'] = no
                items['Product_url'] = response.url
                yield items

        if ordering:
            product_name = response.xpath('//div[@class="tab-pane fade orderoptions" and @id="Orderingoptions"]/div/div/div[contains(@class,"container")]/div/div/div[contains(@class,"ordering_wrap")]/div/div[contains(@class,"row")]/div[contains(@class,"ordering-title")]/p/text()').getall()
            product_no = response.xpath('//div[@class="tab-pane fade orderoptions" and @id="Orderingoptions"]/div/div/div[contains(@class,"container")]/div/div/div[contains(@class,"ordering_wrap")]/div/div[contains(@class,"row")]/div[contains(@class,"col-md-2 col-xs-12")]/p/text()').getall()
            for pro, name , no in zip( pro_name*len(product_name), product_name, product_no):
                items['Pro_name'] = pro
                items['Product_name'] = name
                items['Product_no'] = no
                items['Product_url'] = response.url
                yield items

        else:
            items['Pro_name'] = pro_name
            items['Product_url'] = response.url
            yield items
