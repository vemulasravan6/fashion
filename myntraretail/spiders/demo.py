# -*- coding: utf-8 -*-
import scrapy
import json

def wtf(filename,content):
    file_path = '/home/vemula/Desktop/'+filename
    with open(file_path, 'w') as fpw:
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
    start_urls = ['https://www.otto.de/p/s-oliver-red-label-hemd-613244293/#variationId=613257556']

    def parse(self, response):
        wtf('otto.html',response.body)
        yield response
