# -*- coding: utf-8 -*-
import scrapy
from ..items import CaymanchemItem
import re


class CaySpider(scrapy.Spider):
    name = 'cay_2'
    allowed_domains = ['www.caymanchem.com']
    start_urls = ['https://www.caymanchem.com/Home']

    def parse(self, response):

        links=set(response.xpath("//a/@href").getall())
        for link in links:
            if re.search("^/product/.+",link):
                url ='https://www.caymanchem.com'+link
                yield scrapy.Request(url ,self.parse_data)
            elif re.search("^https://www\.caymanchem\.com/product/.+",link):
                url = link
                yield scrapy.Request(url,self.parse_data)
            elif re.search("^https://www\.caymanchem\.com.+",link):
                url = link
                yield scrapy.Request(url, self.parse)
            else:
                url='https://www.caymanchem.com'+link
                yield scrapy.Request(url, self.parse)

    def parse_data(self, response):
        items=CaymanchemItem()

        product_number = response.xpath('//div[@class="productTemplate" and @id="chemicalProduct"]/div[@id="productHeader"]/div/div/em/text()').get()
        product_no = product_number.strip().split(' ')[2]
        product_name = response.xpath('//div[@class="productTemplate" and @id="chemicalProduct"]/div/h1/text()').getall()

        product_description = response.xpath('//div[@class="productGroup vertical-borders row"]/div/div/p[contains(@class,"text-justify")]/text()').getall()
        product_descr = ''.join(product_description).replace("\n","")

        product_formal_name = response.xpath('//div[@class="productGroup vertical-borders row" ]/div[@id="techInfo"]/div/div[@class="formalName col-9"]/text()').getall()
        product_formal = ''.join(product_formal_name)

        product_alternative_name = response.xpath('//div[@class="productGroup vertical-borders row" ]/div[@id="techInfo"]/div/div[@class="col-9"]/ul/li/text()').getall()
        product_alt = ','.join(product_alternative_name)

        product_addtionalinfo = response.xpath('//div[@class="productGroup vertical-borders row" ]/div[@id="techInfo"]/div/div[@class="col-9"]/text()').getall()
        if product_addtionalinfo is None:
            product_addtionalinfo = response.xpath('//div[@class="productGroup vertical-borders row" ]/div[@class="col-12"]/div[@id="techInfo"]/div/div[@class="col-9"]/text()').getall()
        product_addn = ','.join(product_addtionalinfo)

        product_url = response.url


        items['Catalog'] = product_no
        items['Name'] = product_name
        items['Description'] = product_descr
        if product_formal is None:
            pass
        else:
            items['Formal_name'] = product_formal
        if product_alt is None:
            pass
        else:
            items['Alternative_name'] = product_alt
        if product_addn is None:
            pass
        else:
            items['Additional_info'] = product_addn
        items['Url'] = response.url
        yield items
