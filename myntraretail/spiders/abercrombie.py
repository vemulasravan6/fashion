# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import abercrombie_config as conf

class AbercrombieSpider(scrapy.Spider):
    name = "abercrombie"
    #allowed_domains = ["abercrombie.com"]
    start_urls = ['https://www.abercrombie.com/']

    def parse(self, response):
        priority = 5000
        for url in response.xpath(".//section[@role='region']//a[@role='menuitem']/@href").extract():
            url = 'https://www.abercrombie.com'+url
            priority = priority - 1
            request = scrapy.Request(url=url, callback=self.parseCategoryPage, priority=priority)
            #for key in response.meta.keys():
            #    request.meta[key] = response.meta[key]
            yield request

    def parseCategoryPage(self,response):
        per_page_count = int(re.findall("(\d+)", response.xpath(conf.PER_PAGE_COUNT_XPATH).extract()[0])[0])
        item_count = int(re.findall("(\d+)", response.xpath(conf.ITEM_COUNT_XPATH).extract()[0])[0])
        #print(per_page_count,item_count)
        page_count = item_count / per_page_count
        page_no = 0
        priority = 5000
        for i in range(0, page_count+1):
            start_from = i*per_page_count
            priority = priority - 1
            url = response.url+'/?filtered=true&rows='+str(per_page_count)+'&search-field=&sort=bestmatch&start='+str(start_from)
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
        print(response.url + ' #pageno : ' + str(response.meta['PageNo'])+ ' #rankstart : '+str(input_rank))
        for block in blocks:
            priority = priority - 1
            input_rank = input_rank + 1
            pdpUrl  = 'https://www.abercrombie.com'+block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
            #request.meta['category'] = response.meta['category']
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url
            yield request

    def parsePdpPage(self,response):

        print(' Crawling pdp # '+response.url+' '+str(response.meta['rank'])+ ' '+' # '+response.meta['paginatedUrl'])

        fdi = FashionDbItem()

        fdi['paginatedUrl'] = response.meta['paginatedUrl']

        fdi['rank'] =  response.meta['rank']

        fdi['url'] = response.url

        fdi['currency'] = conf.CURRENCY_XPATH

        fdi['source'] = 'abercrombie'

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        fdi['brand'] = ''

        try:
            fdi['gender'] = response.xpath(conf.GENDER_XPATH).extract()[0]
        except:
            fdi['gender'] = ""
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
            fdi['defaultImage'] = response.xpath(conf.DEFAULTIMAGE_XPATH).extract()[0]
        except:
            fdi['defaultImage'] = ''
            pass

        try:
            fdi['imageUrlList'] = response.xpath(conf.IMAGEURLLIST_XPATH).extract()
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
            fdi['sizes'] = response.xpath(conf.SIZES_XPATH).extract()
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
