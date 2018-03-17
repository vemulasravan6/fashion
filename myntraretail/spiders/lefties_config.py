#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'lefties'

URL         = 'https://www.barneys.com/sitemap?_ga=2.70540944.147060301.1520925905-2073211617.1520925905'

BASE_URL    = 'https://www.barneys.com'

CATEGORIES_GENDER_XPATHS  = [
                                {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "WOMENSWEAR",
                                    "XPATH": ".//*[@id='atg_store_content']/section/nav[2]/div/ul/ul/li/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "MENSWEAR",
                                    "XPATH": ".//*[@id='atg_store_content']/section/nav[5]/div/ul/ul/li/a/@href"
                                }, {
                                    "GENDER": "KIDS",
                                    "CATEGORY": "KIDSWEAR",
                                    "XPATH": ".//*[@id='atg_store_content']/section/nav[7]/div/ul/ul/li/a/@href"
                                }
                            ]

PAGE_SIZE = 100

PRODUCT_BLOCK_XPATH = ".//*[contains(@class,'product-tile')]"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//a[@class='thumb-link']/@href"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

BRAND_XPATH = ".//span[@id='fp-data']/@data-brand"

ARTICLETYPE_XPATH2 = ".//*[@id='pdp_breadcrumbs']/div/span[last()]/a/span/text()"

ARTICLETYPE_XPATH = ".//span[@id='fp-data']/@data-category"

CURRENCY_XPATH = ".//*[@itemprop='priceCurrency']/@content"

ITEM_COUNT_XPATH = ".//*[@id='resultsCount']/@data-productvalue"

PAGE_COUNT_XPATH = ".//select/@data-totalpagecount"

STYLENAME_XPATH = ".//span[@id='fp-data']/@data-productname"

DEFAULTIMAGE_XPATH = ".//span[@itemprop='image']/@content"

IMAGEURLLIST_XPATH = ".//figure/a/@data-zoom"

DESCRIPTION_XPATH= ".//*[@class='pdpReadMore']//text()"

COLOUR_XPATH = ".//span[@id='fp-data']/@data-color"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//*[@id='fp_availableSizes']/@value"

SELLING_PRICE_XPATH = ".//span[@id='fp-data']/@data-minprice"

MRP_XPATH = ".//span[@id='fp-data']/@data-maxprice"

STYLEID_XPATH = ".//span[@id='fp-data']/@data-productid"

SKU_PATH = ".//span[@itemprop='sku']/@content"

STOCK_XPATH = ".//*[@itemprop='availability']/@href"