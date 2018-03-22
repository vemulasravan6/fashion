# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import criminaldamage_config as conf

class criminaldamageUkSpider(scrapy.Spider):
    name = conf.SOURCE
    start_urls = ['https://www.criminaldamage.co.uk/']
    base_url = conf.URL

    def parse(self, response):
        priority = 5000
        #print(response.url)
        for category in  conf.CATEGORIES_GENDER_XPATHS:
            for url in response.xpath(category['XPATH']).extract():
                print(url)
                priority = priority - 1
                #url = self.base_url+url
                request = scrapy.Request(url=url, callback=self.parseCategoryPage, priority=priority)
                request.meta['category'] = category['CATEGORY']
                request.meta['gender'] = category['GENDER']
                yield request


    def parseCategoryPage(self,response):
        print(response.url)
        page_count = int(re.findall("(\d+)", response.xpath(".//*[@class='pager-box']/text()").extract()[0])[1])
        #page_count = 3
        page_no = 0
        priority = 5000
        for i in range(1, page_count+1):
            #print(i,page_count)
            #start_from = i*per_page_count
            priority = priority - 1

            #https://www.criminaldamage.co.uk/mens/all.html?is_ajax=1&p=3&is_scroll=1

            url = response.url+'?is_ajax=1&is_scroll=1&p='+str(i)

            print(url)
            '''
            request = scrapy.Request(url=url, callback=self.parsePaginated, priority=priority)
            request.meta['PageNo'] = page_no
            #request.meta['PerPageCount'] = per_page_count
            request.meta['category'] = response.meta['category']
            request.meta['gender'] = response.meta['gender']
            page_no = page_no + 1
            # for key in response.meta.keys():
            #    request.meta[key] = response.meta[key]
            yield request
            '''


    def parsePaginated(self,response):
        blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH)
        priority = 5000
        input_rank = response.meta['PageNo'] * response.meta['PerPageCount']

        for block in blocks[:50]:
            priority = priority - 1
            input_rank = input_rank + 1
            pdpUrl  = self.base_url+block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
            request.meta['category'] = response.meta['category']
            request.meta['gender'] = response.meta['gender']
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url
            yield request

    def parsePdpPage(self,response):

        #print(' Crawling pdp # '+response.url+' '+str(response.meta['rank'])+ ' '+' # '+response.meta['paginatedUrl'])

        fdi = FashionDbItem()

        fdi['paginatedUrl'] = response.meta['paginatedUrl']

        fdi['gender'] = response.meta['gender']

        fdi['rank'] =  response.meta['rank']

        fdi['category'] = response.meta['category']

        fdi['url'] = response.url

        fdi['source'] = self.name

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        try:
            fdi['brand'] = response.xpath(conf.BRAND_XPATH).extract()[0]
        except:
            fdi['brand'] = ''
            pass

        try:
            fdi['currency'] = response.xpath(conf.CURRENCY_XPATH).extract()[0]#conf.CURRENCY_XPATH
        except:
            fdi['currency'] = ''#'GBP'
            pass

        try:
            fdi['articleType'] = response.xpath(conf.ARTICLETYPE_XPATH).extract()[0]
        except:
            fdi['articleType'] = ''
            pass

        try:
            fdi['styleName'] = response.xpath(conf.STYLENAME_XPATH).extract()[0]
        except:
            fdi['styleName'] = ''
            pass

        try:
            fdi['defaultImage'] = response.xpath(conf.DEFAULTIMAGE_XPATH).extract()[0].split('//')[-1]
        except:
            fdi['defaultImage'] = ''
            pass

        try:
            image_list = response.xpath(conf.IMAGEURLLIST_XPATH).extract()
            image_url_list = []
            for il in image_list:
                image_url_list.append(il.split('//')[-1])
            fdi['imageUrlList'] = image_url_list
        except:
            fdi['imageUrlList'] = ''
            pass

        try:
            fdi['description'] = "".join(response.xpath(conf.DESCRIPTION_XPATH).extract()).strip()
        except:
            fdi['description'] = ''
            pass

        try:
            fdi['colour'] = response.xpath(conf.COLOUR_XPATH).extract()[0]
        except:
            fdi['colour'] = ''
            pass

        try:
            fdi['sizes'] =  list(map(lambda x:x.strip(),response.xpath(conf.SIZES_XPATH).extract()))
        except:
            fdi['sizes'] = ''
            pass

        try:
            fdi['selling_price'] = float(response.xpath(conf.SELLING_PRICE_XPATH).extract()[0])
        except:
            fdi['selling_price'] = ''
            pass

        try:
            fdi['mrp'] = float(response.xpath(conf.MRP_XPATH).extract()[0])
        except:
            fdi['mrp'] = ''
            pass

        try:
            fdi['styleId'] = response.xpath(conf.STYLEID_XPATH).extract()[0]
        except:
            fdi['styleId'] = ''
            pass


        print(fdi)

        yield fdi
