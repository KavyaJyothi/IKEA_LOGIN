import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
class SeleniumDriver():

    def __init__(self, driver):
        self.driver=driver
    def getByType(self, locator_type):
       try:
           locator_type = locator_type.upper()
           if locator_type == "ID":
               return By.ID
           elif locator_type == "XPATH":
               return By.XPATH
           elif locator_type == "NAME":
               return By.NAME
           elif locator_type == "CSS":
               return By.CSS_SELECTOR
           elif locator_type == "CLASS":
               return By.CLASS_NAME
           elif locator_type == "LINK":
               return By.LINK_TEXT
           elif locator_type == "PARTIAL_LINK":
               return By.PARTIAL_LINK_TEXT
           else:
               self.logging.ERROR("Invalid locator value")
       except:
           print("invalid locator value")
    def findElement(self, locator_type, locator_value):
        try:
            by_type=self.getByType(locator_type)
            ele= self.driver.find_element(by_type, locator_value)
            return ele
        except:
            print("unable to find the element with {0}, {1}", locator_value, locator_type)
    def elementDisplayed(self,locator_type, locator_value):
        try:
            ele= self.findElement(locator_type,locator_value)
            if ele.is_displayed():
                return True
            else:
                return False
        except:
            print("unable to find the element with {0}, {1}", locator_value, locator_type)
    def clickElement(self,locator_type, locator_value ):
        try:
            ele= self.findElement(locator_type, locator_value)
            return ele.click()
        except:
            print("unable to find the element with {0}, {1}", locator_value, locator_type)

    def sendKeys(self, locator_type, locator_value, value):
        try:
            ele= self.findElement(locator_type, locator_value)
            return ele.send_keys(value)
        except:
            print("unable to find the element with {0}, {1}", locator_value, locator_type)

