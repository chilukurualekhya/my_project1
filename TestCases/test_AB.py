from operator import truediv

from PageObjects.AB_page import AB_testing
from Utilities.Readconfig import readconfig


class Test_001():
    baseurl=readconfig.GetAppURL()

    def test_001(self,setup):
        self.driver= setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.ABpage = AB_testing(self.driver)
        self.ABpage.AB()
        self.ABpage.elemental()

        self.confirmation= self.ABpage.Confirm_elemental()
        if self.confirmation=="Elemental Selenium":
            assert True
        else:
            assert False

        self.ABpage.Takeme()





