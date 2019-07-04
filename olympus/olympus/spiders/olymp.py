# -*- coding: utf-8 -*-
import scrapy
from ..items import OlympusItem


class OlymSpider(scrapy.Spider):
    name = 'olymp'
    #allowed_domains = ['https://www.olympus-lifescience.com/en/']
    start_urls = ['https://www.olympus-lifescience.com/en/products']

    def parse(self, response):
        links=set(response.xpath('//div[contains(@class,"row")]/div/h2/a/@href').getall())
        for link in links:
            abs_url= 'https://www.olympus-lifescience.com' + link
            yield scrapy.Request(abs_url, self.parse_cat_data_page)

    def parse_cat_data_page(self, response):
        #product_page= response.xpath('//div/a[contains(@class,"more")]/@href').getall()
        items=OlympusItem()

        subcat_page=response.xpath('//div[contains(@class,"row")]/div/h2/a/@href').getall()
        if subcat_page:
            for url in subcat_page:
                urli= 'https://www.olympus-lifescience.com' + url
                yield scrapy.Request(urli,self.parse_cat_data_page)


        else:
            products=response.xpath('//div[contains(@class,"col-sm-6 col-xs-6 col-product")]').getall()
            for product in products:
                product_name=response.xpath('//div[contains(@class,"row")]/div/div[contains(@class,"sub-title")]/text()').getall()
                product_model=response.xpath('//div[contains(@class,"row")]/div/h3/a/text()').getall()
                product_categ=response.xpath('//div[contains(@class,"container")]/div/h1/span/text()').getall()
                product_descr=response.xpath('//div[contains(@class,"shortdesc")]/ul/li/text()').getall()
                product_url=response.xpath('//div/a[contains(@class,"more")]/@href').getall()
                product_imgsrc=response.xpath('//picture/img/@src').getall()
            for name, model, categ, descr, url, imgsrc in zip(product_name, product_model, product_categ*(len(product_name)-1), product_descr, product_url, product_imgsrc):
                items['Product_name'] = name
                items['Product_model'] = model
                items['Product_categ'] = categ
                items['Product_descr'] = descr
                items['Product_url'] = 'https://www.olympus-lifescience.com' + url
                items['Product_imgsrc'] = imgsrc
                yield items
