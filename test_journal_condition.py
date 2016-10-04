# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("http://192.168.1.116:1294/proxy.html")
        wd.find_element_by_xpath("//div[@class='slimScrollDiv']/div[1]").click()
        wd.find_element_by_xpath("//div[@id='ajax-content']/div/div/z-include[1]/div/div/div/div[1]/div/div/div[1]/button[2]").click()
        wd.find_element_by_xpath("//div[@id='ajax-content']//button[.='Добавить условие']").click()
        wd.find_element_by_xpath("//div[@id='ajax-content']/div/div/z-include/div/div/div[2]/div[3]/z-include/div/div/form/fieldset/div[2]/div/div[3]/input").click()
        wd.find_element_by_xpath("//div[@id='ajax-content']/div/div/z-include/div/div/div[2]/div[3]/z-include/div/div/form/fieldset/div[2]/div/div[3]/input").clear()
        wd.find_element_by_xpath("//div[@id='ajax-content']/div/div/z-include/div/div/div[2]/div[3]/z-include/div/div/form/fieldset/div[2]/div/div[3]/input").send_keys("vol")
        wd.find_element_by_link_text("volodina@securit").click()
        wd.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
