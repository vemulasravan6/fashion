#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'criminaldamage'

URL         = 'https://www.cosstores.com/gb/'

CATEGORIES_GENDER_XPATHS  = [
                                {
                                    "GENDER"    : "MENS",
                                    "CATEGORY"  : "MENSWEAR",
                                    "XPATH"     : ".//*[@id='nav-wide']/li[2]/div/ul/li/a/@href"
                                },
                                {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "WOMENSWEAR",
                                    "XPATH": ".//*[@id='nav-wide']/li[3]/div/ul/li/a/@href"
                                },
                                {
                                    "GENDER": "UNISEX",
                                    "CATEGORY": "ACCESSORIES",
                                    "XPATH": ".//*[@id='nav-wide']/li[4]/div/ul/li/a/@href"
                                }
                            ]

'''

'''

PRODUCT_BLOCK_XPATH = ".//li[contains(@class,'item product')]"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//a/@href"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

ARTICLETYPE_XPATH = ".//*[@id='breadcrumb']/ul/li[last()-1]/span/a/text()"

CURRENCY_XPATH = ".//meta[@property='og:price:currency']/@content"

#ITEM_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-total"

#PER_PAGE_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-limit"

STYLENAME_XPATH = ".//meta[@property='og:title']/@content"

DEFAULTIMAGE_XPATH = ".//meta[@property='og:image']/@content"

IMAGEURLLIST_XPATH = ".//ul[@class='slides']/li/div/img/@src"

DESCRIPTION_XPATH= ".//meta[@property='og:description']/@content"

COLOUR_XPATH = ".//meta[@property='og:product:color']/@content"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//div[contains(@class,'productSizes')]/label/text()"

SELLING_PRICE_XPATH = ".//meta[@property='og:price:amount']/@content"

MRP_XPATH = ".//meta[@property='og:price:amount']/@content"

STYLEID_XPATH = ".//div[@id='productContainer']/div[@class='productImages']/@data-selected-article"