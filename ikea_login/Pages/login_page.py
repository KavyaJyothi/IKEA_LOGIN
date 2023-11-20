from selenium import webdriver
from base.selenium_driver import SeleniumDriver

class Login_Page(SeleniumDriver):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #locator
    login_page_redirection_xpath="(//span[contains(text(),'Hej! Log in or sign up')])[1]"
    login_button_id="header__button"
    email_field_id="username"
    password_field_id="password"
    continue_xpath="//span[contains(text(),'Continue')]"
    element_check_xpath="(//div[@class='member-card__title'and contains(text(),'Family card number')])[1]"
    def login_into_ikea(self, username, password):

        self.driver.clickElement("xpath",self.login_page_redirection_xpath)
        self.driver.clickElement("id",self.login_button_id)
        self.driver.sendKeys("id", self.email_field_id,username)
        self.driver.sendKeys("id", self.password_field_id, password)
        self.driver.clickElement("xpath", self.continue_xpath)

    def verify_successful_login(self):
        value=self.driver.element_check_xpath("xpath",self.element_check_xpath)
        return value



