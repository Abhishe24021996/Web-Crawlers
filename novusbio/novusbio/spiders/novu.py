# -*- coding: utf-8 -*-
import scrapy
from ..items import NovusbioItem


class NovuSpider(scrapy.Spider):
    name = 'novu'
    #allowed_domains = ['https://www.novusbio.com/']
    start_urls = ['https://www.novusbio.com/search?keywords=novus&page=11100']

    def parse(self, response):
        items = NovusbioItem()
        product_box=response.xpath('//div[contains(@class,"new-search-result search-result-wrapper")]').getall()
        if product_box:
            product_item_no = response.xpath('//div[contains(@class,"new-search-result search-result-wrapper")]/div[contains(@class,"name")]/span/div/a/text()').getall()
            product_name =response.xpath('//div[contains(@class,"new-search-result search-result-wrapper")]/div[contains(@class,"name")]/span/h2/a/span/text()').getall()
            product_quantity =response.xpath('//div[contains(@class,"new-search-result search-result-wrapper")]/div[contains(@class,"sub-header")]/div/div[contains(@class,"segment")]/strong/text()').getall()
        #    product_reactivity =response.xpath('//div[contains(@class,"new-search-result search-result-wrapper")]/div[contains(@class,"product-attributes")]/div/div[contains(@class,"value")]/span/text()').getall()
        #    product_applications =
        #    product_host =
        #    product_conjugate =
            product_url = response.xpath('//div[contains(@class,"new-search-result search-result-wrapper")]/div[contains(@class,"name")]/span/h2/a/@href').getall()

            for item, name, qaunt, url in zip(product_item_no, product_name, product_quantity, product_url):
                items['Product_item_no'] = item
                items['Product_name'] = name
                items['Product_qauntity'] = qaunt
                items['Product_url'] = 'https://www.novusbio.com' + url
                yield items

        if response.xpath('//div[contains(@class,"search_pager")]/div[contains(@class,"search_page forward")]/a/@href'):
            next_button = response.xpath('//div[contains(@class,"search_pager")]/div[contains(@class,"search_page forward")]/a/@href').get()
            next = 'https://www.novusbio.com' + next_button
            yield scrapy.Request(next, self.parse)
