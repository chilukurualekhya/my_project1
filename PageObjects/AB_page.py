
from selenium.webdriver.common.by import By


class AB_testing():
    LNK_TXT_AB = "A/B Testing"
    LNK_TXT_Elemental = "Elemental Selenium"
    X_PATH_confMSG = "//h1[normalize-space()='Elemental Selenium']"
    X_PATH_TAKEME = "//button[contains(text(),'Take me to the tips!')]"

    def __init__(self, driver):
        self.driver = driver

    def AB(self):
        self.driver.find_element(By.LINK_TEXT, self.LNK_TXT_AB).click()

    def elemental(self):
        self.driver.find_element(By.LINK_TEXT, self.LNK_TXT_Elemental).click()
        self.driver.switch_to.window(self.driver.window_handles[1])


    def Takeme(self):
        self.driver.find_element(By.XPATH, self.X_PATH_TAKEME).click()

    def Confirm_elemental(self):
        return self.driver.find_element(By.XPATH, self.X_PATH_confMSG).text
