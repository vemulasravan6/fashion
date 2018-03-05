#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'ae'

URL         = 'https://www.abercrombie.com/shop/wd'

CATEGORIES_GENDER_XPATHS  = [
                                {
                                    "GENDER": "MEN",
                                    "CATEGORY": "TOPS",
                                    "XPATH": ".//*[@id='flyout-mens']/div/div/div/div[1]/div[2]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "BOTTOMS",
                                    "XPATH": ".//*[@id='flyout-mens']/div/div/div/div[1]/div[3]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "SHOES",
                                    "XPATH": ".//*[@id='flyout-mens']/div/div/div/div[1]/div[4]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "UNDERWEAR",
                                    "XPATH": ".//*[@id='flyout-mens']/div/div/div/div[1]/div[5]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "ACCESSORIES",
                                    "XPATH": ".//*[@id='flyout-mens']/div/div/div/div[1]/div[6]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "TOPS",
                                    "XPATH": ".//*[@id='flyout-womens']/div/div/div/div[1]/div[2]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "BOTTOMS",
                                    "XPATH": ".//*[@id='flyout-womens']/div/div/div/div[1]/div[3]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "SHOES",
                                    "XPATH": ".//*[@id='flyout-womens']/div/div/div/div[1]/div[3]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "DRESSES & ROMPERS",
                                    "XPATH": ".//*[@id='flyout-womens']/div/div/div/div[1]/div[5]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "JEANS",
                                    "XPATH": ".//*[@id='flyout-cat7010140']/div/div/div/div[1]/div[1]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "JEANS",
                                    "XPATH": ".//*[@id='flyout-cat7010140']/div/div/div/div[1]/div[4]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "JEANS",
                                    "XPATH": ".//*[@id='flyout-cat7010140']/div/div/div/div[1]/div[2]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "JEANS",
                                    "XPATH": ".//*[@id='flyout-cat7010140']/div/div/div/div[1]/div[5]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "SWIMWEAR",
                                    "XPATH": ".//*[@id='flyout-cat8180035']/div/div/div/div[1]/div[1]/a/@href"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "SWIMWEAR",
                                    "XPATH": ".//*[@id='flyout-cat8180035']/div/div/div/div[1]/div[3]/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "AERIE",
                                    "XPATH": ".//*[@id='flyout-cat6610030']/div/div/div/div[1]/div/a/@href"
                                }, {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "BRAS",
                                    "XPATH": ".//*[@id='flyout-cat8240005']/div/div/div/div[1]/div/a/@href"
                                }
                            ]

PRODUCT_BLOCK_XPATH = ".//div[@class='product-details-container']"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//div[@class='product-info AEO']/a/@href"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

ARTICLETYPE_XPATH = ".//*[@id='breadcrumb']/ol/li[last()-1]/a/text()"

CURRENCY_XPATH = ".//*[@itemprop='priceCurrency']/@content"

ITEM_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-total"

PER_PAGE_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-limit"

STYLENAME_XPATH = ".//*[@itemprop='name']/text()"

DEFAULTIMAGE_XPATH = ".//div[@class='item item-img active']/img/@src"

IMAGEURLLIST_XPATH = ".//img[@alt='Product thumbnail image']/@src"

DESCRIPTION_XPATH= ".//*[@itemprop='description']//text()"

COLOUR_XPATH = ".//*[@class='psp-product-txt psp-product-color']/span/text()"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//*[@id='psp-sizedropdown-menu']/li/a/@data-size"

SELLING_PRICE_XPATH = ".//*[@id='psp-sale-price']/@content"

MRP_XPATH = ".//*[@id='psp-regular-price']/@content"

STYLEID_XPATH = ".//*[@class='pdp-about-ids-number']/text()"