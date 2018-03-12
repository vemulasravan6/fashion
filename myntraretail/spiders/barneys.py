# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import util as util_obj
import hmde_config as conf
import requests

class BarneysSpider(scrapy.Spider):
    name = conf.SOURCE
    start_urls = [conf.URL]
    base_url = conf.URL
    handle_httpstatus_list = [200,404,500]

    def parse(self, response):

        response = util_obj.getScrapyResponse('http://www.hm.com/de')

        for category in  conf.CATEGORIES_GENDER_XPATHS:

            page_size = conf.PAGE_SIZE

            for url in response.xpath(category['XPATH']).extract():

                if 'http' not in url:
                    url =  'http'+url
                url_slug = "/".join(url.split('/')[-2:])
                pdpCategory = url.split('/')[-1]
                url = "http://api.hm.com/v2/DE/de/products/display?categories="+url_slug+"&concealCategories=true&pageSize="+str(page_size)+"&page=1&deviceType=MOBILE"
                resp = requests.get(url).json()
                input_rank = 1
                if 'pagination' in resp:
                    if 'count' in resp['pagination']:
                        if resp['pagination']['count']>0:
                            product_count = resp['pagination']['count']
                            print(product_count)
                            page_count = (product_count/page_size)+2
                            print(page_count)
                            for i in range(1, page_count):
                                url = "http://api.hm.com/v2/DE/de/products/display?categories="+url_slug+"&concealCategories=true&pageSize="+str(page_size)+"&page="+str(i)+"&deviceType=MOBILE"
                                print(url)
                                resp = requests.get(url).json()
                                for productItem in resp['displayArticles']:

                                    print(productItem)

                                    fdi = FashionDbItem()

                                    fdi['paginatedUrl'] = url

                                    fdi['gender'] = category['GENDER']

                                    fdi['rank'] = input_rank

                                    fdi['source'] = self.name

                                    fdi['run_date'] = str(datetime.datetime.now()).split()[0]

                                    try:
                                        fdi['url'] = productItem['webUrl']
                                    except:
                                        fdi['url'] = ''
                                        pass

                                    try:
                                        fdi['brand'] = 'h & m'
                                    except:
                                        fdi['brand'] = ''
                                        pass

                                    try:
                                        fdi['currency'] = productItem['priceInfo']['currencyIso']
                                    except:
                                        fdi['currency'] = ''  # 'GBP'
                                        pass

                                    try:
                                        fdi['category'] = pdpCategory
                                    except:
                                        fdi['category'] = ""
                                        pass

                                    try:
                                        fdi['articleType'] = pdpCategory
                                    except:
                                        fdi['articleType'] = ''
                                        pass

                                    try:
                                        fdi['styleName'] = productItem['name']
                                    except:
                                        fdi['styleName'] = ''
                                        pass

                                    try:
                                        fdi['defaultImage'] = 'http:'+productItem['primaryImage']['url']
                                    except:
                                        fdi['defaultImage'] = ''
                                        pass

                                    try:
                                        imgLis = []
                                        imgLis.append(fdi['defaultImage'])
                                        imgLis.append('http:'+productItem['secondaryImage']['url'])
                                        fdi['imageUrlList'] = imgLis
                                    except:
                                        fdi['imageUrlList'] = ''
                                        pass

                                    try:
                                        fdi['description'] = ''
                                    except:
                                        fdi['description'] = ''
                                        pass

                                    try:
                                        fdi['colour'] = productItem['colourDescription']
                                    except:
                                        fdi['colour'] = ''
                                        pass

                                    try:
                                        lis = []
                                        for size in productItem['availableSizeInfo']:
                                            lis.append(size['sizeName'])

                                        fdi['sizes'] = lis
                                    except:
                                        fdi['sizes'] = []
                                        pass

                                    try:
                                        fdi['selling_price'] = productItem['priceInfo']['price']
                                    except:
                                        fdi['selling_price'] = ''
                                        pass

                                    try:
                                        fdi['mrp'] = productItem['priceInfo']['price']
                                    except:
                                        fdi['mrp'] = ''
                                        pass

                                    try:
                                        fdi['styleId'] = productItem['articleCode']
                                    except:
                                        fdi['styleId'] = ''
                                        pass

                                    print(fdi)

                                    input_rank = input_rank+1

                                    print("=" * 120)

                                    yield fdi


                        else:
                            print('O Records')


