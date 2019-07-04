# -*- coding: utf-8 -*-
import scrapy
from ..items import Proto2Item


class Pro1Spider(scrapy.Spider):
    name = 'pro_2'
    allowed_domains = ['proteogenix-products.com']
    start_urls = ['https://www.proteogenix-products.com/sitemap']

    def parse(self, response):
        links=set(response.xpath('//ul/li/a/@href').getall())
        for link in links:
            yield scrapy.Request(link, self.parse_data)



    def parse_data(self, response):

        if response.xpath('//div[contains(@class, "product-container")]'):
            pro_url=response.xpath('//div[contains(@class,"product-container")]/div[contains(@class,"right-block")]/h3[contains(@class,"h5")]/a/@href').getall()
            for url in pro_url:
                yield scrapy.Request(url, self.parse_info)



        next_page=int(response.xpath("//div[contains(@class,'top-pagination-content clearfix')]/div/ul/li/a/span/text()")[-1].get())
        start=2
        last=next_page+1
        for n in range(start,last):
            plink=response.request.url+"?p="+str(n)
            yield scrapy.Request(plink, self.parse_pagination)

    def parse_pagination(self, response):

        if response.xpath('//div[contains(@class, "product-container")]'):
            pro_url=response.xpath('//div[contains(@class,"product-container")]/div[contains(@class,"right-block")]/h3[contains(@class,"h5")]/a/@href').getall()
            for url in pro_url:
                yield scrapy.Request(url, self.parse_info)

    def parse_info(self, response):
        items= Proto2Item()
        pro_brand=response.xpath('//section[contains(@class,"page-product-box")]/table/tr[@class="odd"]/td[2]/text()').get()
        pro_name=response.xpath('//div[contains(@class,"pb-center-column col-xs-12 col-sm-4")]/h1/text()').get()
        pro_type=response.xpath('//section[contains(@class,"page-product-box")]/table/tr[@class="even"]/td[2]/text()').get()

        pro_price=response.xpath('//div[contains(@class,"content_prices clearfix")]/div/p/span/text()').get().split(' ')[0]

        product_info = response.xpath('//section[contains(@class,"page-product-box")]/div/table/tr/td/text()').getall()
        pro_info = ','.join(product_info)

        items['Product_brand'] = pro_brand
        items['Product_name']  = pro_name
        items['Product_info'] = pro_info
        items['Product_type'] = pro_type
        items['Product_price'] = pro_price
        items['Product_url'] = response.url
        yield items
