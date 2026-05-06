from PageObjects.Basic_Auth import Basic_Auth

from Utilities.Readconfig import readconfig


class Test002():

    def test001(self,setup):
        self.driver=setup
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        self.driver.maximize_window()

        self.Basic =Basic_Auth(self.driver)
        msg=self.Basic.Confirmmsg()
        assert "Congratulations!" in msg





