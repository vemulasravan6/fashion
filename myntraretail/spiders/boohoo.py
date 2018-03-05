# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import boohoo_config as conf

class BoohooSpider(scrapy.Spider):
    name = conf.SOURCE
    start_urls = ['https://www.boohoo.com/']
    base_url = conf.URL

    def parse(self, response):

        '''
        #debugging single product
        request = scrapy.Request(url='http://www.boohoo.com/rachel-wrap-tie-front-shorts/DZZ27922.html?color=135', callback=self.parsePdpPage, priority=1)
        # for key in response.meta.keys():
        #    request.meta[key] = response.meta[key]
        yield request
        '''

        priority = 5000
        for url in response.xpath(conf.CATEGORIES_XPATH).extract():
            if self.name in url and 'sale' not in url and 'http' in url:
                priority = priority - 1
                request = scrapy.Request(url=url, callback=self.parseCategoryPage, priority=priority)
                yield request


    def parseCategoryPage(self,response):
        print(response.url)
        per_page_count = conf.PER_PAGE_COUNT_XPATH
        page_count = int(re.findall("(\d+)", response.xpath(conf.PAGE_COUNT_XPATH).extract()[0])[0])
        page_no = 0
        priority = 5000
        for i in range(0, page_count+1):
            #print(i,page_count)
            start_from = i*per_page_count
            priority = priority - 1
            url = response.url+'?sz='+str(per_page_count)+'&start='+str(start_from)
            request = scrapy.Request(url=url, callback=self.parsePaginated, priority=priority)
            request.meta['PageNo'] = page_no
            request.meta['PerPageCount'] = per_page_count
            page_no = page_no + 1
            # for key in response.meta.keys():
            #    request.meta[key] = response.meta[key]
            yield request


    def parsePaginated(self,response):
        blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH)
        priority = 5000
        input_rank = response.meta['PageNo'] * response.meta['PerPageCount']
        #print(response.url + ' #pageno : ' + str(response.meta['PageNo'])+ ' #rankstart : '+str(input_rank))
        if "womens" in response.url.split('/'):
            gender = "WOMEN"
        else:
            gender = "MEN"

        for block in blocks:
            priority = priority - 1
            input_rank = input_rank + 1
            pdpUrl  = block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
            request.meta['gender'] = gender
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url
            yield request


    def parsePdpPage(self,response):

        #print(' Crawling pdp # '+response.url+' '+str(response.meta['rank'])+ ' '+' # '+response.meta['paginatedUrl'])

        fdi = FashionDbItem()

        fdi['paginatedUrl'] = response.meta['paginatedUrl']

        fdi['gender'] = response.meta['gender']

        fdi['rank'] =  response.meta['rank']

        fdi['url'] = response.url

        fdi['source'] = 'boohoo'

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        try:
            fdi['brand'] = re.findall(conf.BRAND_REGEX,response.body)[0].replace('&quot;','').replace(':','').replace('"','')
        except:
            fdi['brand'] = ''
            pass

        try:
            fdi['currency'] = response.xpath(conf.CURRENCY_XPATH).extract()[0]#conf.CURRENCY_XPATH
        except:
            fdi['currency'] = ''#'GBP'
            pass

        try:
            fdi['category'] = response.xpath(conf.CATEGORY_XPATH).extract()[0]
        except:
            fdi['category'] = ""
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
            fdi['colour'] = re.findall(conf.COLOR_REGEX,response.body)[0]
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
            fdi['styleId'] = re.findall(conf.STYLEID_REGEX, response.body)[0]
        except:
            fdi['styleId'] = ''
            pass


        print(fdi)

        yield fdi
