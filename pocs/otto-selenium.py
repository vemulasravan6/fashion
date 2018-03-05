# -*- coding: utf-8 -*-

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("https://www.otto.de/p/patrizia-dini-by-heine-glencheckblazer-mit-wolle-567919549/#variationId=567919643")

#driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
#driver.find_element_by_id("search_button_homepage").click()

print (driver.page_source)

driver.quit()


'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(firefox_binary=binary)
#driver = webdriver.Firefox()

print(driver)

driver = webdriver.Firefox()

print(driver)

class OttoDe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.otto.de/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_otto_de(self):
        driver = self.driver
        driver.find_element_by_link_text("Blazer").click()
        driver.find_element_by_css_selector("a > p.p_btn50--4th.san_paging__btn").click()
        driver.find_element_by_css_selector("#san_pagingTopNext > a > p.p_btn50--4th.san_paging__btn > i").click()
        driver.find_element_by_css_selector("a > p.p_btn50--4th.san_paging__btn").click()
        driver.get("https://www.otto.de/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

'''