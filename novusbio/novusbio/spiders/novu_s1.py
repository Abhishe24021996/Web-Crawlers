# -*- coding: utf-8 -*-
import scrapy
from ..items import NovusbioItem
import pandas as pd
import re


class NovuSpider(scrapy.Spider):
    name = 'novu_s1'
    #allowed_domains = ['https://www.novusbio.com/']
    product_pages = pd.read_csv('novu.csv')
    product_urls = product_pages.iloc[:,3].tolist()
    #for url in product_urls:
    #    start_urls = [url]
    start_urls = [url for url in product_urls]

    def parse(self, response):
        items = NovusbioItem()
        product_item_no = response.xpath('//div[contains(@class,"atc_catnum")]/text()').get()
        product_name =response.xpath('//div[contains(@class,"main grid_16")]/h1/text()').get()
        #product_quantity =response.xpath('//div[contains(@class,"atc_catnum")]/text()').get().split('-')[1]

        product_description = response.xpath('//div[contains(@class,"ds_info")]/div/p/text()').getall()
        product_descr = ','.join(product_description)

        product_alternate_names = response.xpath('//div[contains(@class,"ds_info")]/div[contains(@class,"information-list")]/ul/li/text()').getall()
        product_alt = ','.join(product_alternate_names)

        product_papers = response.xpath('//div[contains(@class,"ds_info")]/div/div[contains(@class,"backref")]/ol/li/text()').getall()
        product_pap = ','.join(product_papers)

        furthurinfo = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/strong/text()').getall()
        for i in range(0,len(furthurinfo)):
            for item in furthurinfo:
                if re.search('^Immunogen$',item):
                    product_immunogen = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Immunogen'] = product_immunogen
                elif re.search('^Specificity$',item):
                    product_specificity = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Specificity'] =product_specificity
                elif re.search('^Source$',item):
                    product_source = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Source'] =product_source
                #elif re.search('^Isotype$',item):
                #    product_isotype = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()

                elif re.search('^Clonality$',item):
                    product_clonality = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Clonality'] =product_clonality
                elif re.search('^Host$',item):
                    product_host = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Host'] =product_host

                elif re.search('^Gene$',item):
                    product_gene = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                elif re.search('^Dilutions$',item):
                    product_dilutions = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Dilutions'] =product_dilutions
                elif re.search('^Application Notes$',item):
                    product_application = response.xpath('//table[contains(@class,"ds_list wide")]/tr/td/div/text()')[i].get()
                    items['Application_Notes'] = product_application

            
        product_url = response.url

        items['Item_no'] = product_item_no
        items['Name'] = product_name
        #items['Quantity'] = product_quantity
        items['Description'] =product_descr
        items['Alt_names'] = product_alt
        items['Papers'] = product_pap
        items['Url'] = response.url
        #if product_immunogen:
        #    items['Immunogen'] = product_immunogen
        #if product_specificity:
        #    items['Specificity'] =product_specificity
        #if product_source:
        #    items['Source'] =product_source
        #f product_clonality:
        #    items['Clonality'] =product_clonality
        #if product_host:
        #    items['Host'] =product_host
        #if product_dilutions:
        #    items['Dilutions'] =product_dilutions
        #if product_application:
        #    items['Application_Notes'] = product_application
        yield items
