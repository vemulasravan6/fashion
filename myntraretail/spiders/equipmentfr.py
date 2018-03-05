# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import equipmentfr_config as conf

class EquipmentfrSpider(scrapy.Spider):
    name = "equipmentfr"
    allowed_domains = ["equipmentfr.com"]

    def start_requests(self):
        priority = 5000
        for category in  conf.CATEGORIES:
            priority = priority - 1
            request = Request(url=conf.CATEGORIES[category], callback=self.parse, priority=priority)
            request.meta['category'] = category
            yield request

    def parse(self, response):
        per_page_count = len(response.xpath(conf.PER_PAGE_COUNT_XPATH))
        item_count = int(re.findall("(\d+)",response.xpath(conf.ITEM_COUNT_XPATH).extract()[0])[0])
        page_count = item_count/per_page_count
        page_no = 0
        priority = 5000
        for i in range(1,page_count+2):
            priority = priority-1
            url = response.url+'?p='+str(i)
            print('Raising request : '+ url +' # '+ str(page_no))
            request = Request(url, callback=self.parsePaginated, priority=priority)
            request.meta['category'] = response.meta['category']
            request.meta['PageNo'] = page_no
            request.meta['PerPageCount'] = per_page_count
            page_no = page_no + 1
            yield request

    def parsePaginated(self,response):
        blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH) #[:2]
        priority = 5000
        input_rank = response.meta['PageNo'] * response.meta['PerPageCount']
        print(response.url + ' #pageno : ' + str(response.meta['PageNo'])+ ' #rankstart : '+str(input_rank))
        for block in blocks:
            priority = priority - 1
            input_rank = input_rank + 1
            pdpUrl  = block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
            request.meta['category'] = response.meta['category']
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url

            '''
            #can be used later for list page crawling
            print(block.xpath(".//a/@href").extract()[0]                            #pdpUrl
            print(block.xpath(".//a/span/img/@src").extract()[0]                    #img
            print(block.xpath(".//a/h2[@itemprop='name']/text()").extract()[0])     #title
            print(block.xpath(".//*[@itemprop='color']/text()").extract()[0])       #color
            print(block.xpath(".//*[@itemprop='price']/@content").extract()[0])     #price
            print("="*100)
            '''
            #time.sleep(0.5)
            yield request

    def parsePdpPage(self,response):

        print(' Crawling pdp # '+response.url+' '+str(response.meta['rank'])+ ' '+' # '+response.meta['paginatedUrl'])

        fdi = FashionDbItem()

        fdi['paginatedUrl'] = response.meta['paginatedUrl']

        fdi['rank'] =  response.meta['rank']

        fdi['url'] = response.url

        fdi['currency'] = conf.CURRENCY_XPATH

        fdi['gender'] = conf.GENDER_XPATH

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        fdi['source'] = 'EquipmentFR'

        fdi['brand'] = 'EquipmentFR'

        fdi['category'] = response.meta['category']

        try:
            fdi['styleName'] = response.xpath(conf.STYLENAME_XPATH).extract()[0]
        except:
            fdi['styleName'] = ''
            pass

        try:
            fdi['articleType'] = response.xpath(conf.ARTICLETYPE_XPATH).extract()[0].split()[-1]
        except:
            fdi['articleType'] = ''
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

        yield fdi
