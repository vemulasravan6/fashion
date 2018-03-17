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


class LeftiesSpider(scrapy.Spider):
    name = conf.SOURCE
    start_urls  = ['https://www.lefties.com/9/info/sitemaps/sitemap-index-products-lf.xml'] # [conf.URL]
    base_url    = conf.BASE_URL
    handle_httpstatus_list = [200,404,500]

    def readDataFromUrl(self, url):
        path = url.split('/')[-1]
        data_download_status = False
        file_content = ''
        shell_cmd = "wget -O " + path + " -q " + url
        try:
            data = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
            data_download_status = True
            f = gzip.open(path, 'rb')
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
            for productUrl in (Selector(text=sitemapData).xpath('//loc/text()').extract()):
                print(productUrl)
            print("="*100)


        #print (gzip.GzipFile(fileobj=StringIO.StringIO(urllib2.urlopen(DOWNLOAD_LINK).read()), mode='rb').read())

        '''
        priority = 50000
        for category in  conf.CATEGORIES_GENDER_XPATHS:
            page_size = conf.PAGE_SIZE
            for url in response.xpath(category['XPATH']).extract():
                priority = priority - 1
                request = scrapy.Request(url=url+'?recordsPerPage=48&page=1', callback=self.parseCategoryPage, priority=priority)
                request.meta['gender'] = category['GENDER']
                yield request
        '''

    def parseCategoryPage(self,response):
        per_page_count = 48
        item_count = int(re.findall("(\d+)", response.xpath(conf.ITEM_COUNT_XPATH).extract()[0])[0])
        print(per_page_count,item_count)
        page_count = item_count / per_page_count
        #page_no = 0
        priority = 5000
        for i in range(1, page_count+2):
            start_from = i*per_page_count
            priority = priority - 1
            url = response.url.replace("page=1","page="+str(i))
            request = scrapy.Request(url=url, callback=self.parsePaginated, priority=priority)
            request.meta['PageNo'] = page_no
            request.meta['PerPageCount'] = per_page_count
            request.meta['gender'] = response.meta['gender']
            page_no = page_no + 1
            # for key in response.meta.keys():
            #    request.meta[key] = response.meta[key]
            yield request

    def parsePaginated(self,response):
        blocks = response.xpath(conf.PRODUCT_BLOCK_XPATH)
        priority = 5000
        input_rank = response.meta['PageNo'] * response.meta['PerPageCount']
        print(response.url + ' #pageno : ' + str(response.meta['PageNo'])+ ' #rankstart : '+str(input_rank))
        for block in blocks[:25]:
            priority = priority - 1
            input_rank = input_rank + 1
            pdpUrl  = self.base_url+block.xpath(conf.PRODUCT_URL_INSIDE_BLOCK_XPATH).extract()[0]
            request = Request(pdpUrl, callback=self.parsePdpPage, priority=priority)
            #request.meta['category'] = response.meta['category']
            request.meta['rank'] = input_rank
            request.meta['paginatedUrl'] = response.url
            request.meta['gender'] = response.meta['gender']
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

        try:
            fdi['brand'] = response.xpath(conf.BRAND_XPATH).extract()[0]
        except:
            fdi['brand'] = ''
            pass

        try:
            fdi['currency'] = response.xpath(conf.CURRENCY_XPATH).extract()[0]  #conf.CURRENCY_XPATH
        except:
            fdi['currency'] = ''#'GBP'
            pass

        try:
            fdi['category'] = response.xpath(conf.ARTICLETYPE_XPATH).extract()[0]
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
            fdi['sizes'] =  json.loads(response.xpath(conf.SIZES_XPATH).extract()[0])
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

        print(fdi)

        yield fdi

