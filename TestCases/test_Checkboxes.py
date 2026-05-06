import time

from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Checkboxes import ChkBox
from TestCases.conftest import setup
from Utilities.Readconfig import readconfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test003():
    baseurl= readconfig.GetAppURL()

    def test_003(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        wait = WebDriverWait(self.driver, 10)

        self.Check= ChkBox(self.driver)
        # Click on Checkbox page link
        self.Check.Checklink()

        buttons = self.Check.Chkbox_buttons()
        wait.until(EC.element_to_be_clickable(buttons[0]))
        buttons[0].click()
        assert buttons[0].is_selected()



