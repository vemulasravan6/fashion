__author__ = 'sravan'

from checkbox.lib import url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import json
import urllib2
import urlparse
import csv
from time import gmtime, strftime
import simplejson
from hashlib import sha1

def write_to_file(filename, content, format='utf-8', append=True, basedir = '.', ):
    site_separator = '\n'
    op = None
    if append:
        op = open(filename, 'a')
    else:
        op = open(filename, 'w')
    op.write(content.encode(format))
    op.write(site_separator.encode(format))
    op.close()
    #print "file written successfully.."
    return

def dict_to_json(d, ind=4):
    return simplejson.dumps(d, indent=ind)

def get_Seed_urls(category_url_file):
    final_seed_url_list = []
    f = open(category_url_file)
    for line in f:
        ##print line
        final_seed_url_list.append(line)
    f.close()
    ##print len(final_seed_url_list)
    return final_seed_url_list

def crawl2(category_url_file,output_dump_file,phantomJs_path,sleepTime):
    seed_urls = get_Seed_urls(category_url_file);
    ##print seed_urls
    cnt = 1
    driver = webdriver.PhantomJS(phantomJs_path)
    #driver = webdriver.Firefox()
    for url in seed_urls:
        url = 'http://www.playgroundonline.com/sachin-tendulkar-merchandise-gifts-store'
        #print "Crawling..."+str(cnt)
        ##print url
        #driver.implicitly_wait(1)
        driver.get(url)
        try:
            check = driver.find_element_by_xpath("html/body/div/div/div/div/div/div/div/div/div/div/p")
            #print "Msg from src : " + check.text
        except NoSuchElementException:
            all_items = []
            ##print 'Data available..'
            ##print "Crawling..." + url
            seed_url = url
            blocks = driver.find_elements_by_xpath("//div[4]/table/tbody/tr/td/div")
            for b in blocks:
                record = {}
                try:
                    mrp = b.find_element_by_css_selector(".skuCol").text
                    #print mrp

                    mrp = mrp.replace(',', '')
                    record['mrp']=mrp
                except NoSuchElementException:
                    mrp = 'NA'
                    record['mrp']=mrp
                    pass
                try:
                    title = b.find_element_by_xpath(".//div[@class='browseSkuName']/a").text
                    title = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['title']=title
                except NoSuchElementException:
                    title = 'NA'
                    record['title']=title
                    pass
                try:
                    thumbnail = b.find_element_by_xpath(".//ul/li/a/img").get_attribute("src")
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['thumbnail']=thumbnail
                except NoSuchElementException:
                    thumbnail = 'NA'
                    record['thumbnail']=thumbnail
                    pass
                try:
                    url = b.find_element_by_xpath(".//div[@class='browseSkuName']/a").get_attribute("href")
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['url']=url
                except NoSuchElementException:
                    url = 'NA'
                    record['url']=url
                    pass
                try:
                    category = driver.find_element_by_xpath("//div[@class='breadCrumbs']/a[2]").text
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['category']=category
                except NoSuchElementException:
                    category = 'NA'
                    record['category']=category
                    pass
                try:
                    subcategory = driver.find_element_by_xpath("//div[@class='breadCrumbs']/h1").text
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['subcategory']=subcategory
                except NoSuchElementException:
                    subcategory = 'NA'
                    record['subcategory']=subcategory
                    pass
                try:
                    stock = b.find_element_by_xpath(".//div[@class='browseSave']/span").text
                    if len(stock)>1:
                        record['stock'] = stock
                    else:
                        record['stock'] = 'NA'
                except NoSuchElementException:
                    stock = 'NA'
                    record['stock']=stock
                    pass
                crawl_date = strftime("%Y%m%d", gmtime())
                crawl_time = strftime("%Y%m%d%H%M%S", gmtime())
                record['crawl_time']=crawl_time
                record['crawl_date']=crawl_date
                record['seed_url']=seed_url
                record['sku']=''
                record['urlh']= sha1(seed_url).hexdigest()
                record['source']=''
                record['offers']=''
                record['brand']=''
                #record['stock']=stock
                record['variant']=''
                record['count']=''
                ##print record
                all_items.append(record)

            #print all_items
            #write_to_file(output_dump_file, '\n'.join([dict_to_json(cluster, ind=None) for cluster in all_items]), format='utf-8')
            #make_csv(all_items,'makeMyTrip.csv')
        #print "waiting for "+str(sleepTime)+" seconds.."
        time.sleep(sleepTime)
        cnt += 1
    driver.close()
    driver.quit()

def crawl(category_url_file,output_dump_file,phantomJs_path,sleepTime):
    seed_urls = get_Seed_urls(category_url_file);
    ##print seed_urls
    cnt = 1
    driver = webdriver.PhantomJS(phantomJs_path)
    #driver = webdriver.Firefox()
    for url in seed_urls:
        #url = 'http://www.playgroundonline.com/Gym+Equipment-Steppers'
        print("Crawling..."+str(cnt))
        ##print url
        #driver.implicitly_wait(1)
        driver.get(url)
        try:
            check = driver.find_element_by_xpath("html/body/div/div/div/div/div/div/div/div/div/div/p")
            #print "Msg from src : " + check.text
        except NoSuchElementException:
            all_items = []
            ##print 'Data available..'
            ##print "Crawling..." + url
            seed_url = remove_new_lines(url)
            blocks = driver.find_elements_by_xpath("//div[3]/div[1]/span/span/div[1]")
            for b in blocks:
                record = {}
                try:
                    mrp = b.find_element_by_css_selector(".browsePrice").text
                    mrp = mrp.replace(',', '')
                    record['mrp']=mrp
                except NoSuchElementException:
                    mrp = 'NA'
                    record['mrp']=mrp
                    pass
                try:
                    title = b.find_element_by_xpath(".//div[@class='browseSkuName']/a").text
                    title = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['title']=title
                except NoSuchElementException:
                    title = 'NA'
                    record['title']=title
                    pass
                try:
                    thumbnail = b.find_element_by_xpath(".//ul/li/a/img").get_attribute("src")
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['thumbnail']=thumbnail
                except NoSuchElementException:
                    thumbnail = 'NA'
                    record['thumbnail']=thumbnail
                    pass
                try:
                    url = b.find_element_by_xpath(".//div[@class='browseSkuName']/a").get_attribute("href")
                    #thumbnail = title.replace(',', '')
                    #url = remove_new_lines(url)
                    record['urlh']= sha1(url).hexdigest()
                    record['url']=url
                except NoSuchElementException:
                    url = 'NA'
                    record['url']=url
                    pass
                try:
                    category = driver.find_element_by_xpath("//div[@class='breadCrumbs']/a[2]").text
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['category']=category
                except NoSuchElementException:
                    category = 'NA'
                    record['category']=category
                    pass
                try:
                    subcategory = driver.find_element_by_xpath("//div[@class='breadCrumbs']/h1").text
                    #thumbnail = title.replace(',', '')
                    #dep = remove_new_lines(departure)
                    record['subcategory']=subcategory
                except NoSuchElementException:
                    subcategory = 'NA'
                    record['subcategory']=subcategory
                    pass
                try:
                    stock = b.find_element_by_xpath(".//div[@class='browseSave']/span").text
                    if len(stock)>1:
                        record['stock'] = stock
                    else:
                        record['stock'] = 'In Stock'
                except NoSuchElementException:
                    stock = 'NA'
                    record['stock']=stock
                    pass
                crawl_date = strftime("%Y%m%d", gmtime())
                crawl_time = strftime("%Y%m%d%H%M%S", gmtime())
                record['crawl_time']=crawl_time
                record['crawl_date']=crawl_date
                record['seed_url']=seed_url
                record['sku']=''
                record['source']=''
                record['offers']=''
                record['brand']=''
                #record['stock']=stock
                record['variant']=''
                record['count']=''
                ##print record
                all_items.append(record)
            #print all_items
            write_to_file(output_dump_file, '\n'.join([dict_to_json(cluster, ind=None) for cluster in all_items]), format='utf-8')
            #make_csv(all_items,'makeMyTrip.csv')
        #print "waiting for "+str(sleepTime)+" seconds.."
        time.sleep(sleepTime)
        cnt += 1
    driver.close()
    driver.quit()

def remove_new_lines(str):
    str = str.splitlines()
    str = ' '.join(str)
    return str

def make_csv(list,file_name):
    with open(file_name, 'a+') as f:
        writer = csv.writer(f)
        writer.writerows(list)
    f.close()

category_url_file = "all1.csv"  #Give list page seeds
output_dump_file = "dump1.json"  #Give output file
phantomJs_path = "/home/sravan/Dw/bin/phantomjs" #Give phantomJs path
sleepTime = 1 #Give sleep time for crawler

crawl(category_url_file,output_dump_file,phantomJs_path,sleepTime)
