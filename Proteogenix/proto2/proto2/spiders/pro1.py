# -*- coding: utf-8 -*-
import scrapy
from ..items import Proto2Item


class Pro1Spider(scrapy.Spider):
    name = 'pro1'
    allowed_domains = ['proteogenix-products.com']
    start_urls = ['https://www.proteogenix-products.com/sitemap']

    def parse(self, response):
        links=set(response.xpath('//ul/li/a/@href').getall())
        for link in links:
            yield scrapy.Request(link, self.parse_data)


    #def parse_product_page(self, response):
    #    product_page_links=response.xpath('//a[@class="product-name"]/@href')
    #    for link in product_page_links:
    #        yield scrapy.Request(link, self.parse_data)

    def parse_data(self, response):
        items= Proto2Item()

        if response.xpath('//div[contains(@class, "product-container")]'):
            container=response.xpath('//div[contains(@class, "product-container")]').getall()
            for contain in container:
                pro_brand=response.xpath("//div[@class='product-container']/div[@class='right-block']/table[@class='table-data-sheet']/tr/td[2]/text()").getall()
                pro_name=response.xpath('//div[contains(@class,"product-container")]/div[contains(@class,"right-block")]/h3[contains(@class,"h5")]/a/text()').getall()
                pro_type=response.xpath("//div[@class='product-container']/div[@class='right-block']/table[@class='table-data-sheet']/tr[2]/td[2]/text()").getall()
                pro_price=response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "product-price", " " ))]/text()').getall()

                pro_url=response.xpath('//div[contains(@class,"product-container")]/div[contains(@class,"right-block")]/h3[contains(@class,"h5")]/a/@href').getall()




            for brand, name, type, price, url in zip(pro_brand, pro_name, pro_type, pro_price, pro_url):
                items['Product_brand'] = brand
                items['Product_name']  = name
                items['Product_type'] = type
                items['Product_price'] = price
                items['Product_url'] = url

                yield items


        next_page=int(response.xpath("//div[contains(@class,'top-pagination-content clearfix')]/div/ul/li/a/span/text()")[-1].get())
        start=2
        last=next_page+1
        for n in range(start,last):
            plink=response.request.url+"?p="+str(n)
            yield scrapy.Request(plink, self.parse_pagination)
        #if next_page is None:
        #    pass

        #else:
        #    n=next_page+1
        #    for page in range(2,n):
        #        plink=response.request.url + "?p=" + str(page)
        #        yield response.Request(plink, self.parse_pagination)



#        if next_page is None:
##
#        else:
#            last=next_page-1
#            start=1
#            for page in range(last):
#                start += 1
#                link_p= response.request.url + "?p=" + str(start)
#                yield response.Request(link_p, self.parse_pagination)

    def parse_pagination(self, response):
        items= Proto2Item()

        if response.xpath('//div[contains(@class, "product-container")]'):
            container=response.xpath('//div[contains(@class, "product-container")]').getall()
            for contain in container:
                pro_brand=response.xpath("//div[@class='product-container']/div[@class='right-block']/table[@class='table-data-sheet']/tr/td[2]/text()").getall()
                pro_name=response.xpath('//div[contains(@class,"product-container")]/div[contains(@class,"right-block")]/h3[contains(@class,"h5")]/a/text()').getall()
                pro_type=response.xpath("//div[@class='product-container']/div[@class='right-block']/table[@class='table-data-sheet']/tr[2]/td[2]/text()").getall()
                pro_price=response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "product-price", " " ))]/text()').getall()

                pro_url=response.xpath('//div[contains(@class,"product-container")]/div[contains(@class,"right-block")]/h3[contains(@class,"h5")]/a/@href').getall()




            for brand, name, type, price, url in zip(pro_brand, pro_name, pro_type, pro_price, pro_url):
                items['Product_brand'] = brand
                items['Product_name']  = name
                items['Product_type'] = type
                items['Product_price'] = price
                items['Product_url'] = url

                yield items
