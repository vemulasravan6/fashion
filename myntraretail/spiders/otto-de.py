# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import ottode_config as conf
import util as util_obj
import time
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class OttoDeSpider(scrapy.Spider):
    name = conf.SOURCE
    base_url = conf.URL
    start_urls = ['https://www.otto.de/']
    driver = None

    def __init__(self):
        #self.driver = util_obj.initiateDriver()
        # register spider_closed signal with beforeClose callback
        #dispatcher.connect(self.beforeClose, signals.spider_closed)
        pass

    def parse(self, response):
        priority = 5000
        #print(response.url)
        for category in  conf.CATEGORIES_GENDER_XPATHS[:1]:
            for url in response.xpath(category['XPATH']).extract()[:2]:
                priority = priority - 1
                url = self.base_url+url
                request = scrapy.Request(url=url, callback=self.parseCategoryPage, priority=priority)
                request.meta['category'] = category['CATEGORY']
                request.meta['gender'] = category['GENDER']
                yield request

    def parseCategoryPage(self,response):

        per_page_count = conf.PER_PAGE_COUNT
        try:
            page_count = int(re.findall("(\d+)", response.xpath(conf.PAGE_COUNT_XPATH).extract()[0])[0])
        except:
            page_count = 0
            pass

        page_count =1

        if page_count>0:
            #print(page_count)
            page_no = 0
            priority = 5000
            for i in range(1, page_count+1):
                priority = priority - 1
                url = response.url+'?p='+str(i)+'&ps='+str(per_page_count)
                request = scrapy.Request(url=url, callback=self.parsePaginated, priority=priority)
                request.meta['PageNo'] = page_no
                request.meta['PerPageCount'] = per_page_count
                request.meta['gender'] = response.meta['gender']
                request.meta['category'] = response.meta['category']
                page_no = page_no + 1
                yield request

    def parsePaginated(self,response):
        blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH)
        priority = 5000
        input_rank = 0
        for block in blocks[:1]:
            priority = priority - 1
            input_rank = input_rank + 1
            try:
                brand = block.xpath(conf.BRAND_XPATH).extract()[0]
            except:
                brand = ''
                pass
            pdpUrl  = self.base_url+block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdp, priority=priority)
            request.meta['gender'] = response.meta['gender']
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url
            request.meta['category'] = response.meta['category']
            yield request
            '''
            resp = util_obj.getScrapyResponse(pdpUrl)

            if resp!='':

                #print(response)

                print('='*100)

                time.sleep(2)

                 
                request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
                request.meta['gender'] = response.meta['gender']
                request.meta['rank'] = input_rank
                request.meta['paginatedUrl'] = response.url
                request.meta['category'] = response.meta['category']
                request.meta['brand'] = brand
                yield request
                 


                print(' Crawling pdp # '+pdpUrl+' '+str(input_rank)+ ' '+' # '+response.url)

                fdi = FashionDbItem()

                fdi['paginatedUrl'] = response.url

                fdi['gender'] = response.meta['gender']

                fdi['rank'] =  input_rank

                fdi['url'] = pdpUrl

                fdi['source'] = self.name

                fdi['run_date'] = str(datetime.datetime.now()).split()[0]

                fdi['category'] = response.meta['category']

                try:
                    fdi['brand'] = resp.xpath(conf.BRAND_XPATH).extract()[0]
                except:
                    fdi['brand'] = self.name
                    pass

                try:
                    fdi['currency'] = resp.xpath(conf.CURRENCY_XPATH).extract()[0]
                except:
                    fdi['currency'] = ''#'GBP'
                    pass

                try:
                    fdi['articleType'] = resp.xpath(conf.ARTICLETYPE_XPATH).extract()[0]
                except:
                    fdi['articleType'] = ''
                    pass

                try:
                    fdi['styleName'] = resp.xpath(conf.STYLENAME_XPATH).extract()[0]
                except:
                    fdi['styleName'] = ''
                    pass


                try:
                    fdi['defaultImage'] = 'https:'+resp.xpath(conf.DEFAULTIMAGE_XPATH).extract()[0]
                except:
                    fdi['defaultImage'] = ''
                    pass

                try:
                    img_list = []

                    img_list.append(fdi['defaultImage'])

                    fdi['imageUrlList'] = img_list
                except:
                    fdi['imageUrlList'] = ''
                    pass

                try:
                    fdi['selling_price'] = float(resp.xpath(conf.SELLING_PRICE_XPATH).extract()[0].replace(',',''))
                except:
                    fdi['selling_price'] = ''
                    pass

                try:
                    fdi['mrp'] = float(resp.xpath(conf.MRP_XPATH).extract()[0].replace(',',''))
                except:
                    fdi['mrp'] = ''
                    pass

                try:
                    desc = resp.xpath(conf.DESCRIPTION_XPATH).extract()
                    txt = ''
                    for str1 in desc:
                        txt = str1.strip()+txt
                    fdi['description'] = txt
                except:
                    fdi['description'] = ''
                    pass


                try:
                    data_json = json.loads(resp.xpath(conf.COLOUR_XPATH).extract()[0])
                    for dimen in data_json['distinctDimensions']:
                        if dimen['type'] == 'color':
                            if len(dimen['values']) > 0:
                                print(dimen['values'][0]['value'])
                    fdi['colour'] = data_json['distinctDimensions'][0]['values'][0]['value']
                except:
                    fdi['colour'] = ''
                    pass

                try:
                    data_json = json.loads(resp.xpath(conf.COLOUR_XPATH).extract()[0])
                    sizes = []
                    for dimen in data_json['distinctDimensions']:
                        if dimen['type'] == 'size':
                            for value in dimen['values']:
                                sizes.append(value['value'])

                    fdi['sizes'] =  sizes
                except:
                    fdi['sizes'] = ''
                    pass


                try:
                    fdi['styleId'] = resp.xpath(conf.STYLEID_XPATH).extract()[0]
                except:
                    fdi['styleId'] = ''
                    pass

                print(fdi)

                yield fdi
            '''


    def parsePdp(self, response):
        data_json = json.loads(response.xpath(conf.COLOUR_XPATH).extract()[0])
        try:
            brand = response.xpath(conf.BRAND_XPATH).extract()[0]
        except:
            brand = self.name
            pass
        for variation_id in data_json['variations']:
            pdpItem = data_json['variations'][variation_id]
            pdpItem['brandXpathItem'] = brand
            pdpItem['gender']         = response.meta['gender']
            pdpItem['rank']           = response.meta['rank']
            pdpItem['paginatedUrl']   = response.meta['paginatedUrl']
            pdpItem['category']   = response.meta['category']
            for key in pdpItem.keys():
                print(key)
            #print(pdpItem.keys())
            print('='*100)
