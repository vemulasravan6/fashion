# -*- coding: utf-8 -*-
import scrapy
import json
from selenium import webdriver
from scrapy.http import HtmlResponse
import inspect,sys,time
import util as util_obj


def wtf(filename,content):
    file_path = '/home/vemula/Desktop/'+filename
    with open(filename, 'w') as fpw:
        fpw.write(content)
        fpw.close()
        print('file written successfully..')

    with open(file_path, 'r') as fpr:
        print(fpr.readlines())
        fpr.close()
        print('file read successfully..')



class DemoSpider(scrapy.Spider):
    name = "demo"
    #allowed_domains = ["example.com"]
    start_urls = ['https://www.lefties.com/sa/women/jeans/super-skinny-ripped-jeans-c1029515p500757003.html']

    def parse(self, response):
        response = util_obj.getScrapyResponse('https://www.lefties.com/sa/women/jeans/super-skinny-ripped-jeans-c1029515p500757003.html')
        wtf('lefties1.html',response.body)
        yield response
