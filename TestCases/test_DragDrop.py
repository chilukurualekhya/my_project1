from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from PageObjects.Drag_Drop import Drag_Drop
from TestCases.conftest import setup
from Utilities.Readconfig import readconfig


class Test005():
    baseurl=readconfig.GetAppURL()

    def test_005(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)

        #click on link
        self.Dragdrop = Drag_Drop(self.driver)
        self.Dragdrop.drag_drop()

        #perform drag drop
        self.Dragdrop.perform_drag_drop()

        txt_A,txt_B = self.Dragdrop.driver()
        assert txt_A == "txt_B"
        assert txt_B == "txt_A"



