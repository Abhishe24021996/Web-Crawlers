# -*- coding: utf-8 -*-
import scrapy
from ..items import ReageconItem


class ReagSpider(scrapy.Spider):
    name = 'reag'
    #allowed_domains = ['https://www.reagecon.com/']
    start_urls = ['https://www.reagecon.com']

    def parse(self, response):
        links=set( response.xpath('//a/@href').getall())
        for link in links:
            link=response.urljoin(link)
            yield scrapy.Request(link, self.parse_sub_cat)

    def parse_sub_cat(self,response):
        pro_links=response.xpath('//div[contains(@class,"product-title-extended")]/a/@href').getall()
        for pro_link in pro_links:
            pro_link=response.urljoin(pro_link)
            yield scrapy.Request(pro_link,self.parse_data)

    def parse_data(self,response):
        items=ReageconItem()

        product_item_no = response.xpath('//div[contains(@class,"details-info")]/div/div/div[contains(@class,"product-id font-lighter")]/span[contains(@class,"value")]/text()').getall()
        product_name = response.xpath('//div[contains(@class,"details-info")]/div/div/h1/text()').getall()
        product_price =response.xpath('//div[contains(@class,"form-row")]/div/div/div/div/span/span[contains(@class,"lbl-price")]/text()').getall()
        #product_descr =response.xpath('//div[contains(@class,"specifications clearfix")]/table/tbody/tr[contains(@class,"")]/td[contains(@class,"value")]/text()').getall()
        product_wght = response.xpath('//div[contains(@class,"specifications clearfix")]/table/tbody/tr[contains(@class,"")]/td[contains(@class,"value")]/text()')[0].getall()
        product_packsize = response.xpath('//div[contains(@class,"specifications clearfix")]/table/tbody/tr[contains(@class,"")]/td[contains(@class,"value")]/text()')[2].getall()
        product_value = response.xpath('//div[contains(@class,"specifications clearfix")]/table/tbody/tr[contains(@class,"")]/td[contains(@class,"value")]/text()')[3].getall()
        product_mfr_no=response.xpath('//div[contains(@class,"specifications clearfix")]/table/tbody/tr[contains(@class,"")]/td[contains(@class,"value")]/text()')[4].getall()
        #product_url =response.url
        #product_imgsrc =
        for item, name, price, wght, size, value, mfr in zip(product_item_no, product_name, product_price, product_wght, product_packsize,product_value,product_mfr_no):
            items['Product_item_no'] = item
            items['Product_name'] = name
            items['Product_price'] = price
            items['Product_wght'] = wght
            items['Product_packsize'] = size
            items['Product_value'] = value
            items['Product_mfr_no'] = mfr
            items['Product_url'] = response.url
            yield items
