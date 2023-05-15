import logging
import time

from selenium.webdriver.common.by import By

from Utilities.readproperties import ReadIni
from Utilities.loggerfile import Logge
from pageobject.Loginpage import Login

class Test_001:
    url = ReadIni.geturl()
    username = ReadIni.getusername()
    password = ReadIni.getpassword()

    logger= Logge.loggen()

    def test_login1(self, setup):
        self.logger.info("********test start***********")
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get(self.url)
        self.lp.setusername(self.username)
        self.logger.info(f"username is:- {self.username}")
        self.lp.setpassword(self.password)
        self.logger.info(f"password is:- {self.password}")
        self.lp.clickbutn()
        self.logger.info(f"Click on Submit:-{self.lp.submit_id}")
        self.logger.debug("******Test passed***********")
        time.sleep(2)
        # self.succ = self.driver.find_element(By.XPATH,"//h1")
        # print(self.succ.text)
        # print(self.lp.successlogin())
        # assert self.succ.text == 'Logged In Successfully', 'Test Failed'
        assert self.lp.successlogin() == 'Logged In Successfully', 'Test Failed'

print("heelloooooo")
print("new helloooo")

#piyush dra



