#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'equipmentfr'

URL         = 'https://www.equipmentfr.com/'

CATEGORIES  =   {
                  "shirts"   : "https://www.equipmentfr.com/shop/shirts"
                }

'''
{
    ,
  "dresses"  : "https://www.equipmentfr.com/shop/dresses",
  "jackets"  : "https://www.equipmentfr.com/shop/jackets",
  "pajamas"  : "https://www.equipmentfr.com/shop/pajamas",
  "sweaters" : "https://www.equipmentfr.com/shop/sweaters"
}
'''

PER_PAGE_COUNT_XPATH = ".//div/ul/li[@class='item']/div[@class='item-wrapper']"

ITEM_COUNT_XPATH = ".//p[@class='amount']/text()"

PRODUCT_BLOCK_XPATH = ".//div/ul/li[@class='item']/div[@class='item-wrapper']"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//a/@href"

STYLENAME_XPATH = ".//*[@itemprop='name']/text()"

ARTICLETYPE_XPATH = ".//meta[@itemprop='category']/@content"

DEFAULTIMAGE_XPATH = ".//*[@itemprop='image']/@content"

IMAGEURLLIST_XPATH = ".//div[@id='gallery_thumbs']//ul/li/img/@src"

DESCRIPTION_XPATH= ".//*[@itemprop='description']//text()"

CURRENCY_XPATH = ".//meta[@itemprop='priceCurrency']/@content"

COLOUR_XPATH = ".//div[@class='product-color']/div/text()"

GENDER_XPATH = ".//meta[@itemprop='audience']/@content"

SIZES_XPATH = ".//fieldset[@id='product-options-wrapper']/script[1]/text()"

SELLING_PRICE_XPATH = ".//*[@itemprop='price']/@content"

MRP_XPATH = ".//*[@itemprop='price']/@content"

STYLEID_REGEX = "<li>Style: #(.*?)</li>"

STOCK_XPATH = ".//meta[@itemprop='availability']/@content"

BRAND_XPATH = ".//meta[@itemprop='brand']/@content"

SKU_XPATH = ".//meta[@itemprop='sku']/@content"