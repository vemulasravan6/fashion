# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import ae_config as conf

class AeSpider(scrapy.Spider):
    name = "ae"
    base_url = 'https://www.ae.com'
    start_urls = ['https://www.ae.com/international?cm=sIN-cINR']

    def parse(self, response):
        priority = 5000
        print(response.url)
        for category in  conf.CATEGORIES_GENDER_XPATHS[:5]:
            for url in response.xpath(category['XPATH']).extract()[:5]:
                priority = priority - 1
                url = self.base_url+url
                request = scrapy.Request(url=url, callback=self.parsePaginated, priority=priority)
                request.meta['category'] = category['CATEGORY']
                request.meta['gender'] = category['GENDER']
                yield request

    def parseCategoryPage(self,response):
        print(response.url)
        per_page_count = 80
        page_count = 1  #int(re.findall("(\d+)", response.xpath(conf.PAGE_COUNT_XPATH).extract()[0])[0])
        page_no = 0
        priority = 5000
        for i in range(0, page_count+1):
            #print(i,page_count)
            start_from = i*per_page_count
            priority = priority - 1
            url = 'http://www.boohoo.com/womens/tops?sz='+str(per_page_count)+'&start='+str(start_from)
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
        input_rank = 0
        #print(response.url + ' #pageno : ' + str(response.meta['PageNo'])+ ' #rankstart : '+str(input_rank))
        for block in blocks[:100]:
            priority = priority - 1
            input_rank = input_rank + 1
            pdpUrl  = self.base_url+block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
            request.meta['gender'] = response.meta['gender']
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url
            request.meta['category'] = response.meta['category']
            yield request

    def parsePdpPage(self,response):

        print(' Crawling pdp # '+response.url+' '+str(response.meta['rank'])+ ' '+' # '+response.meta['paginatedUrl'])

        fdi = FashionDbItem()

        fdi['paginatedUrl'] = response.meta['paginatedUrl']

        fdi['gender'] = response.meta['gender']

        fdi['rank'] =  response.meta['rank']

        fdi['url'] = response.url

        fdi['source'] = self.name

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        fdi['category'] = response.meta['category']

        fdi['brand'] = self.name

        try:
            fdi['currency'] = response.xpath(conf.CURRENCY_XPATH).extract()[0]
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
            fdi['defaultImage'] = 'https:'+response.xpath(conf.DEFAULTIMAGE_XPATH).extract()[0]
        except:
            fdi['defaultImage'] = ''
            pass

        try:
            img_list = []
            for img_tag in response.xpath(conf.IMAGEURLLIST_XPATH).extract():
                img_list.append('https:'+img_tag)

            fdi['imageUrlList'] = img_list
        except:
            fdi['imageUrlList'] = ''
            pass

        try:
            fdi['selling_price'] = float(response.xpath(conf.SELLING_PRICE_XPATH).extract()[0].replace(',',''))
        except:
            fdi['selling_price'] = ''
            pass

        try:
            fdi['mrp'] = float(response.xpath(conf.MRP_XPATH).extract()[0].replace(',',''))
        except:
            fdi['mrp'] = ''
            pass


        try:
            desc = response.xpath(conf.DESCRIPTION_XPATH).extract()
            txt = ''
            for str1 in desc:
                txt = str1.strip()+txt
            fdi['description'] = txt
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
            fdi['styleId'] =  response.xpath(conf.STYLEID_XPATH).extract()[0]
        except:
            fdi['styleId'] = ''
            pass


        print(fdi)

        yield fdi
