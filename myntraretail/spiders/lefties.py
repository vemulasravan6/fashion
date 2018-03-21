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


class LeftiesSpider(scrapy.Spider):
    name = conf.SOURCE
    start_urls  =  [conf.START_URL]
    #base_url    = conf.BASE_URL
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
        for url in  (Selector(text=response.body).xpath('//loc/text()').extract()):
            sitemapData = self.readDataFromUrl(url)
            for productUrl in (Selector(text=sitemapData[0]).xpath('//loc/text()').extract()):

                pdpUrlContent = self.readDataFromUrl(productUrl, compressedFile=False)[0]

                scrapyResponseObject = HtmlResponse(url=productUrl, body=pdpUrlContent, encoding='utf-8')

                self.parsePdpPage(scrapyResponseObject)


    def parsePdpPage(self,response):

        fdi = FashionDbItem()

        fdi['url'] = response.url

        productJson = ''

        try:
            productJson = response.xpath(conf.PRODUCT_JSON).extract()[0] #json.loads()
            productJson = json.loads(productJson)
            fdi['brand'] = productJson['brand']
            fdi['currency'] = productJson['offers']['pricecurrency']
            fdi['category'] = productJson['offers']['category'].split('-')[-1].strip()
            fdi['gender'] = productJson['offers']['category'].split('-')[0].strip()
            fdi['articleType'] = productJson['offers']['category'].split('-')[-1].strip()
            fdi['styleName'] = productJson['name']
            fdi['defaultImage'] = productJson['image']
            fdi['description'] = productJson['description']
            fdi['selling_price'] = float(productJson['offers']['price'])
            fdi['mrp'] = float(productJson['offers']['price'])
            print(fdi)
        except:
            fdi['brand'] = ''
            fdi['currency'] = ''
            fdi['category'] = ''
            fdi['gender'] = ''
            fdi['articleType'] = ''
            fdi['styleName'] = ''
            fdi['defaultImage'] = ''
            fdi['description'] = ''
            fdi['selling_price'] = ''
            fdi['mrp'] = ''
            pass

        fdi['source'] = self.name

        fdi['run_date'] = str(datetime.datetime.now()).split()[0]

        try:
            sizes = []

            istoreid = re.findall('inditex.istoreid = (.*?);', response.body)[0]

            icatalogid = re.findall("inditex.icatalogid = (.*?);", response.body)[0]

            iproductid = re.findall("inditex.iproductid = (.*?);", response.body)[0]

            apiUrl = 'https://www.lefties.com/itxrest/2/catalog/store/' + istoreid + '/' + icatalogid + '/category/0/product/' + iproductid + '/detail?languageId=-1&appId=1'

            jsonResp = requests.get(apiUrl).json()

            for size in jsonResp['detail']['colors'][0]['sizes']:
                sizes.append(size['name'])

            fdi['sizes'] =  sizes

            fdi['styleId'] = jsonResp['id']

        except:
            fdi['sizes'] = ''
            fdi['styleId'] = ''
            pass

        print(fdi)

        #yield fdi

        '''
        try:
            fdi['imageUrlList'] = response.xpath(conf.IMAGEURLLIST_XPATH).extract()
        except:
            fdi['imageUrlList'] = ''
            pass

        try:
            fdi['colour'] = response.xpath(conf.COLOUR_XPATH).extract()[0]
        except:
            fdi['colour'] = ''
            pass 

        try:
            fdi['sku'] = response.xpath(conf.SKU_PATH).extract()[0]
        except:
            fdi['sku'] = ''
            pass

        try:
            fdi['stock'] =   "Out of stock" if  "OutOfStock" in response.xpath(conf.STOCK_XPATH).extract()[0] else 'In Stock'
        except:
            fdi['stock'] = ''
            pass
        
        '''


