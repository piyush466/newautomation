from selenium import webdriver
from selenium.webdriver.common.by import By
# from Utilities.loggerfile import Logge
class Login:
    username_id = 'username'
    password_id = 'password'
    submit_id = 'submit'
    verifylogin = '//h1'



    def __init__(self,driver):
        self.driver = driver


    def setusername(self,username):
        self.driver.find_element(By.ID,self.username_id).send_keys(username)



    def setpassword(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)


    def clickbutn(self):
        self.driver.find_element(By.ID, self.submit_id).click()

    def successlogin(self):
        self.test = self.driver.find_element(By.XPATH,self.verifylogin)
        return self.test.text

































