#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'otto'

URL         = 'https://www.otto.de'

CATEGORIES_GENDER_XPATHS  = [
                                {
                                    "GENDER": "MEN",
                                    "CATEGORY": "ALL",
                                    "XPATH": ".//*[@id='navigationWrp']/nav/ul/li[5]/div/div/ul/li/ul/li/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "ALL",
                                    "XPATH": ".//*[@id='navigationWrp']/nav/ul/li[3]/div/div/ul/li/ul/li/a/@href"
                                }, {
                                    "GENDER": "KIDS",
                                    "CATEGORY": "ALL",
                                    "XPATH": ".//*[@id='navigationWrp']/nav/ul/li[7]/div/div/ul/li/ul/li/a/@href"
                                }
                            ]

PER_PAGE_COUNT = 72

PRODUCT_BLOCK_XPATH = ".//article[@class='product small']"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//a/@href"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

BRAND_XPATH = ".//*[@itemprop='brand']/text()"

ARTICLETYPE_XPATH = ".//td[@class='breadcrumb']/span[1]/span[last()]/a/span/text()"

CURRENCY_XPATH = ".//meta[@itemprop='priceCurrency']/@content"

ITEM_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-total"

PAGE_COUNT_XPATH = ".//div[@class='san_paging__bottomWrapper']/ul/li[last()-1]/span/p/text()"

STYLENAME_XPATH = ".//meta[@property='og:title']/@content"

DEFAULTIMAGE_XPATH = ".//meta[@property='og:image']/@content"

IMAGEURLLIST_XPATH = ".//*[@id='js_prd_verticalImageControlThumbnailList']/li/img/@src"

DESCRIPTION_XPATH= ".//*[@itemprop='description']//text()"

COLOUR_XPATH = ".//*[@id='productDataJson']/text()"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//*[@id='dimensions']/div[3]/div[2]/ul/li/@title"

SELLING_PRICE_XPATH = ".//*[@id='reducedPriceAmount']/@content"

MRP_XPATH = ".//*[@id='oldPriceAmount']/text()"

STYLEID_XPATH = ".//section/@data-product-id"