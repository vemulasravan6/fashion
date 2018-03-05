from selenium import webdriver
from scrapy.http import HtmlResponse
import inspect,sys,time

def getScrapyResponse(url):
    try:
        driver = webdriver.PhantomJS()
        driver.get(url)
        response_html = driver.page_source
        response_html = HtmlResponse(url=url, body=response_html, encoding='utf-8')
        driver.close()
        return response_html
    except:
        e_msg = 'EXCEPTION OCCURRED IN :' + inspect.stack()[0][3]
        e_msg = e_msg + str(sys.exc_info())
        e_msg = e_msg + ' | ' + ' Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
        print(e_msg)
        pass
    return ''


'''
class util:
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


'''