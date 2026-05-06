from selenium.webdriver.common.by import By


class Digest():
    xpath_Confirm ="//p[contains(text(),'Congratulations!')]"

    def __init__(self,driver):
        self.driver =driver


    def confirmmsg(self):
        return self.driver.find_element(By.XPATH,self.xpath_Confirm).text