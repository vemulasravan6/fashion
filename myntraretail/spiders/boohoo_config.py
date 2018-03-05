#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      =   'boohoo'

URL         =   'http://www.boohoo.com/'

CATEGORIES_XPATH  =  ".//*[@id='navigation']/ul/li[3 and 4]/div/div/ul[2]/li/ul//li/a/@href"



'''

'''

ITEM_COUNT_XPATH = ''

PER_PAGE_COUNT_XPATH = 80

PAGE_COUNT_XPATH = ".//li[contains(@class,'pagination-item')][last()-1]/a/text()"

PRODUCT_BLOCK_XPATH = ".//*[@id='search-result-items']/li"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//div[@class='product-name']/a/@href"

STYLENAME_XPATH = ".//*[@itemprop='name']/text()"

DEFAULTIMAGE_XPATH = ".//*[@itemprop='image']/@src"

IMAGEURLLIST_XPATH = ".//*[@itemprop='image']/@src"

DESCRIPTION_XPATH= ".//*[@id='ui-id-2']//text()"

CURRENCY_XPATH = ".//*[@itemprop='priceCurrency']/@content"

COLOUR_XPATH = ".//*[@itemprop='color']/@content"

GENDER_XPATH = ".//*[@id='main']/ol/li[2]/a/text()"

CATEGORY_XPATH = ".//*[@id='main']/ol/li[last()-1]/a/text()"

ARTICLETYPE_XPATH = ".//*[@id='main']/ol/li[last()-1]/a/text()"

SIZES_XPATH = ".//ul[@class='swatches size']/li/span/text()"

SELLING_PRICE_XPATH = ".//*[@itemprop='price']/@content"

MRP_XPATH = ".//*[@itemprop='price']/@content"

STYLEID_REGEX = 'data-masterid="(.*?)"'

COLOR_REGEX = '"colorBasicDisplayValue": "(.*?)"'

BRAND_REGEX = '"brand(.*?),"'