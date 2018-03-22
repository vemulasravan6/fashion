# -*- coding: utf-8 -*-
import scrapy,re
import json
from myntraretail.items import MyntraretailItem,FashionDbItem
from scrapy.http.request import Request
import time
import datetime
import util as util_obj
import lefties_config as conf
import requests
from scrapy.selector import Selector
import gzip
import StringIO
import requests
import wget
import wget
import gzip
import subprocess
import os
from scrapy.http import HtmlResponse
import modaoperandi_config as conf

class ModaoperandiSpider(scrapy.Spider):
    name = conf.SOURCE
    start_urls  =  [conf.START_URL]
    handle_httpstatus_list = [200,404,500]

    def readDataFromUrl(self, url, compressedFile=True):
        path = url.split('/')[-1]
        data_download_status = False
        file_content = ''
        shell_cmd = "wget -O " + path + " -q " + url
        try:
            data = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
            data_download_status = True
            if compressedFile:
                f = gzip.open(path, 'rb')
            else:
                f = open(path, 'r')
            file_content = f.read().lower()
            f.close()
            os.remove(path)
        except:
            data = None
            print("HTML_DOWNLOAD_EXCEPTION")
            pass
        return file_content, data_download_status

    def parse(self, response):
        siteMapContent = self.readDataFromUrl(conf.SITE_MAP_URL, compressedFile=True)[0]
        priority  = 5000000
        input_rank = 0
        for url in Selector(text=siteMapContent).xpath('//loc/text()').extract()[:100]:
            input_rank = input_rank + 1
            priority-=1


            #html parsing
            #request = scrapy.Request(url=url, callback=self.parsePdpPage, priority=priority)


            #json parsing
            request = scrapy.Request(url=url, callback=self.parsePdpPageJson, priority=priority)

            request.meta['rank'] = input_rank
            yield request


    def parsePdpPage(self,response):

        print('Crawling pdp # '+response.url+' '+str(response.meta['rank']) )

        fdi = FashionDbItem()

        #fdi['paginatedUrl'] = response.meta['paginatedUrl']

        fdi['gender'] = 'WOMEN'

        fdi['rank'] =  response.meta['rank']

        fdi['url'] = response.url

        fdi['source'] = self.name

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        try:
            fdi['brand'] = response.xpath(conf.BRAND_XPATH).extract()[0]
        except:
            fdi['brand'] = ''#'GBP'
            pass
        try:
            fdi['currency'] = response.xpath(conf.CURRENCY_XPATH).extract()[0]
        except:
            fdi['currency'] = ''#'GBP'
            pass

        try:
            fdi['articleType'] = response.xpath(conf.ARTICLETYPE_XPATH).extract()[0]
            fdi['category'] =   fdi['articleType']
        except:
            fdi['articleType']  =   ''
            fdi['category']     =   ''
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
                img_list.append(img_tag)

            fdi['imageUrlList'] = img_list
        except:
            fdi['imageUrlList'] = ''
            pass

        try:
            fdi['selling_price'] = float(response.xpath(".//div[contains(@class,'price_styling current_price')]/text()").extract()[-1])
        except:
            fdi['selling_price'] = ''
            pass

        try:
            fdi['mrp'] = float(response.xpath(".//div[contains(@class,'price_styling current_price')]/text()").extract()[-1])
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


    def parsePdpPageJson(self,response):

        fdi = FashionDbItem()

        fdi['url'] = response.url

        productJson = ''

        try:
            productJson = response.xpath(conf.PRODUCT_JSON).extract()[0] #json.loads()
            productJson = json.loads(productJson, )
            print(json.dumps(productJson, indent=2, sort_keys=True))

        except:
            pass



