from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChkBox():
    xpath_chkbox_link= "//a[normalize-space()='Checkboxes']"
    xpath_chkbox= "//form[@id='checkboxes']//input[@type='checkbox']"

    def __init__(self,driver):
        self.driver=driver


    def Checklink(self):
        wait = WebDriverWait(self.driver, 10)
        link=wait.until(EC.element_to_be_clickable((By.XPATH, self.xpath_chkbox_link)))
        link.click()

    def Chkbox_buttons(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, self.xpath_chkbox)))



