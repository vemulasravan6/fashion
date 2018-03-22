#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'criminaldamage'

START_URL         = 'https://www.criminaldamage.co.uk/'

CATEGORIES_GENDER_XPATHS  = [
                                {
                                    "GENDER"    : "MENS",
                                    "CATEGORY"  : "MENSWEAR",
                                    "XPATH"     : ".//*[@id='nav-wide']/li[2]/div/ul/li"
                                },
                                {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "WOMENSWEAR",
                                    "XPATH": ".//*[@id='nav-wide']/li[3]/div/ul/li"
                                },
                                {
                                    "GENDER": "UNISEX",
                                    "CATEGORY": "ACCESSORIES",
                                    "XPATH": ".//*[@id='nav-wide']/li[4]/div/ul/li"
                                }
                            ]

'''

'''

PRODUCT_BLOCK_XPATH = ".//div[@class='product-container']"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//h2/a/@href"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

ARTICLETYPE_XPATH = ".//*[@id='breadcrumb']/ul/li[last()-1]/span/a/text()"

CURRENCY_XPATH = ".//meta[@itemprop='priceCurrency']/@content"

#ITEM_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-total"

#PER_PAGE_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-limit"

STYLENAME_XPATH = ".//div[@itemprop='name']/h1/text()"

DEFAULTIMAGE_XPATH = ".//span[@class='image_url']/text()"

IMAGEURLLIST_XPATH = ".//div/ul/li/a/img/@src"

DESCRIPTION_XPATH= ".//*[@itemprop='description']//text()"

COLOUR_XPATH = ".//meta[@property='og:product:color']/@content"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//*[@id='attribute169']/option/text()"

SELLING_PRICE_XPATH = ".//meta[@itemprop='price']/@content"

MRP_XPATH = ".//meta[@itemprop='price']/@content"

STYLEID_XPATH = ".//div[@id='productContainer']/div[@class='productImages']/@data-selected-article"

STOCK_XPATH = ".//link[@itemprop='availability']/@href"

STYLEID_REGEX = "productId:'(.*?)',"

SIZES_REGEX = ''