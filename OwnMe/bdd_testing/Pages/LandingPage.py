class LandingPage:
    link_login_xpath = '//*[@id="id_login_head"]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.link_login_xpath).click()