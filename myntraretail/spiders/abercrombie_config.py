#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'abercrombie'

URL         = 'https://www.abercrombie.com/shop/wd'

CATEGORIES  =   {
                  "shirts"   : "https://www.equipmentfr.com/shop/shirts",
                  "dresses"  : "https://www.equipmentfr.com/shop/dresses",
                  "jackets"  : "https://www.equipmentfr.com/shop/jackets",
                  "pajamas"  : "https://www.equipmentfr.com/shop/pajamas",
                  "sweaters" : "https://www.equipmentfr.com/shop/sweaters"
                }

'''

'''

ITEM_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-total"

PER_PAGE_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-limit"

PRODUCT_BLOCK_XPATH = ".//*[contains(@class,'product-grid__products')]/li[contains(@class,'product-card')]"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//h3/a[@class='product-card__name']/@href"

STYLENAME_XPATH = ".//*[@itemprop='name']/text()"

DEFAULTIMAGE_XPATH = ".//*[@itemprop='image' and @class='product-main-images__main-image']/@src"

IMAGEURLLIST_XPATH = ".//*[@itemprop='image']/@src"

DESCRIPTION_XPATH= ".//*[@itemprop='description']//text()"

CURRENCY_XPATH = "INR"

COLOUR_XPATH = ".//*[@itemprop='color']/@content"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

ARTICLETYPE_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

SIZES_XPATH = ".//ul[@class='product-sizes']/li/label/span/text()"

SELLING_PRICE_XPATH = ".//*[@itemprop='price']/@content"

MRP_XPATH = ".//*[@itemprop='price']/@content"

STYLEID_REGEX = 'data-productid="(.\d*?)"'