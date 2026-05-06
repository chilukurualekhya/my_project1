from PageObjects.Digest_Authentication import Digest


class Test_004():
     def test_004(self,setup):
         self.driver=setup
         self.driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")
         self.driver.maximize_window()

         self.digest=Digest(self.driver)
         messege =self.digest.confirmmsg()
         assert 'Congratulations!' in messege

