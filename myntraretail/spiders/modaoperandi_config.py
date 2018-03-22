#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'modaoperandi'

START_URL = 'https://www.modaoperandi.com/'

SITE_MAP_URL = 'https://www.modaoperandi.com/sitemap.xml.gz'

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

BRAND_XPATH = ".//div[contains(@class,'product_detail_page ga-eec-product')]/@data-brand"

ARTICLETYPE_XPATH2 = ".//*[@id='pdp_breadcrumbs']/div/span[last()]/a/span/text()"

ARTICLETYPE_XPATH = ".//*[@id='wraps-body-content']/div[3]/div/div[1]/div/div[2]/div[1]/div/div/a[last()]/text()"

CURRENCY_XPATH = ".//div[contains(@class,'price_styling current_price')]/text()"

ITEM_COUNT_XPATH = ".//*[@id='resultsCount']/@data-productvalue"

PAGE_COUNT_XPATH = ".//select/@data-totalpagecount"

STYLENAME_XPATH = ".//div[contains(@class,'product_detail_page ga-eec-product')]/@data-name"

DEFAULTIMAGE_XPATH = ".//meta[@property='og:image']/@content"

IMAGEURLLIST_XPATH = ".//div[@class='pdp_thumbnail_slick_anchor']/img/@src"

DESCRIPTION_XPATH= ".//*[@id='wraps-body-content']//span[contains(@class,'description_text')]//text()"

COLOUR_XPATH = ".//div[@class='active_size']/img/@data-color-code"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//*[@class='specific_product_sizes']/text()"

SELLING_PRICE_XPATH = ".//div[contains(@class,'price_styling current_price')]/text()"

MRP_XPATH = ".//div[contains(@class,'price_styling current_price')]/text()"

STYLEID_XPATH = ".//div[contains(@class,'product_detail_page ga-eec-product')]/@data-variant_id"

SKU_PATH = ".//span[@itemprop='sku']/@content"

STOCK_XPATH = ".//*[@itemprop='availability']/@href"

PRODUCT_JSON = ".//div[@data-react-class='SiteComponent']/@data-react-props"