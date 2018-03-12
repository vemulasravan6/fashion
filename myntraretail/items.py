# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class MyntraretailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pdpTitle = scrapy.Field()
    pdpUrl = scrapy.Field()
    pdpPrice = scrapy.Field()
    pdpDescription = scrapy.Field()
    pdpImage = scrapy.Field()
    pdpColor = scrapy.Field()
    pdpImg = scrapy.Field()
    pdpSizes = scrapy.Field()
    pdpCategory = scrapy.Field()
    pdpCrawlTime = scrapy.Field()
    pass


class FashionDbItem(Item):
    fdbId       = Field()
    source      = Field()
    styleName   = Field()
    url         = Field()
    styleId     = Field()
    articleType = Field()
    gender      = Field()
    brand       = Field()
    colour      = Field()
    sizes       = Field()
    selling_price= Field()
    mrp         = Field()
    defaultImage= Field()
    imageUrlList= Field()
    description = Field()
    activatedAt = Field()
    attributes  = Field()
    data        = Field()
    currency    = Field()
    run_date    = Field()
    rank        = Field()
    paginatedUrl = Field()
    category = Field()
    stock = Field()
    sku = Field()
    pass