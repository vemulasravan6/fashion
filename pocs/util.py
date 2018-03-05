from selenium import webdriver
#import scrapy
from scrapy.http import HtmlResponse

class Util():
    driver = None

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        pass

    def downloadUsingSelenium(self, url):
        response_html = ''
        try:
            self.driver.get(url)
            response_html = self.driver.page_source
        except:
            pass
        return response_html

    def getScrapyResponse(self,url):
        response = self.downloadUsingSelenium(url)
        response = HtmlResponse(url=url, body=response, encoding='utf-8')
        return response

    def closeDriver(self):
        self.driver.close()


u = Util()

print(u.getScrapyResponse("https://www.otto.de/p/patrizia-dini-by-heine-glencheckblazer-mit-wolle-567919549/#variationId=567919643"))

u.closeDriver()