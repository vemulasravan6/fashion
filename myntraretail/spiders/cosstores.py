# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import cosstores_config as conf
import requests
from scrapy.http import HtmlResponse

'''

Note : Reach out Sravan, if you wanna make changes in this spider

'''

class CosstoresSpider(scrapy.Spider):
    name = "cosstores"
    base_url = 'https://www.cosstores.com'
    start_urls = ['https://www.cosstores.com/gb/']

    def parse(self, response):
        priority = 5000
        for category in  conf.CATEGORIES_GENDER_XPATHS:
            for url in response.xpath(category['XPATH']):
                priority = priority - 1
                category_url = self.base_url+url.xpath('.//@href').extract()[0]
                pageId = url.xpath('.//@data-pageid').extract()[0]
                request = scrapy.Request(url=category_url, callback=self.parseFirstPaginatedPage, priority=priority)
                request.meta['category'] = category['CATEGORY']
                request.meta['gender'] = category['GENDER']
                request.meta['pageId'] = pageId
                request.meta['categoryUrl'] = category_url
                yield request

    def parseFirstPaginatedPage(self,response):

        #print('Crawling first page : '+response.url)

        paginated_url = response.url

        pageId = response.meta['pageId']

        category = response.meta['category']

        gender = response.meta['gender']

        #extracting product blocks from first page
        blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH)

        pageProducts = []

        for block in blocks:
            url_list = block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()
            if len(url_list)>0:
                pdpUrl = self.base_url+url_list[0]
                pageProducts.append(pdpUrl)

        #extracting product blocks from rest of the pages, if we find new products, we'll append them to pageProducts
        start_page = 1
        while True:
            url = 'https://www.cosstores.com/gb/ProductListClientService/loadAdditionalProducts?&pageId=' + str(pageId) + '&page='+str(start_page)+'&DataType=html'
            #print('crawling paginated : '+url)
            body = requests.get(url).text
            response = HtmlResponse(url=url, body=body, encoding='utf-8')
            blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH)
            if len(blocks)>0:
                for block in blocks:
                    url_list = block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()
                    if len(url_list) > 0:
                        pdpUrl = self.base_url + url_list[0]
                        pageProducts.append(pdpUrl)
            else:
                break

            start_page = start_page+1

        priority = 5000

        input_rank = 0
        # print(response.url + ' #pageno : ' + str(response.meta['PageNo'])+ ' #rankstart : '+str(input_rank))
        for pp in pageProducts:
            priority = priority - 1
            input_rank = input_rank + 1
            request = Request(pp, callback=self.parsePdpPage, priority=priority)
            request.meta['gender'] = gender
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = paginated_url
            request.meta['category'] = category
            yield request



    def parsePdpPage(self,response):

        #print(response.body)

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
            fdi['defaultImage'] = response.xpath(conf.DEFAULTIMAGE_XPATH).extract()[0]
        except:
            fdi['defaultImage'] = ''
            pass

        try:
            img_list = []
            for img_tag in response.xpath(conf.IMAGEURLLIST_XPATH).extract():
                img_list.append(self.base_url+img_tag)
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
            fdi['sizes'] =  response.xpath(conf.SIZES_XPATH).extract()
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
