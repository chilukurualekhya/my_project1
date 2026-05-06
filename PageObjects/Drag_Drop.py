from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Drag_Drop():
    Lnk_txt_dragdrop= "Drag and Drop"
    id_A ="column-a"
    id_B="column-b"

    def __init__(self,driver):
        self.driver=driver
        self.wait =WebDriverWait(self.driver,10)

    def drag_drop(self):
       LINK= self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.Lnk_txt_dragdrop)))
       self.driver.LINK.click()


    def source_A(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.id_A)))

    def source_B(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.id_B)))

    def perform_drag_drop(self):
        source= self.driver.source_A()
        target= self.driver.source_B()

        actions =ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()


    def Text_AB(self):
        txt_A =self.driver.find_element(By.ID, self.id_A).text
        txt_B =self.driver.find_element(By.ID, self.id_B).text
        return txt_A,txt_B