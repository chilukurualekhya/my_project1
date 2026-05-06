from selenium.webdriver.common.by import By


class Basic_Auth():
    lnk_txt_Basic="Basic Auth"
    xpath_confirm ="//p[contains(text(),'Congratulations! You must have the proper credentials.')]"

    def __init__(self,driver):
        self.driver =driver


    def Basic_auth(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_txt_Basic).click()

    def Confirmmsg(self):
        return self.driver.find_element(By.XPATH,self.xpath_confirm).text





