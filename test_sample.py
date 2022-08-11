import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture
def test_a(self):
        global  driver
        driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        driver.close()
        print("test passed")


def test_b(self,test_a):
       driver.find_element(by=By.ID,value="txtUsername").send_keys("Admin")
       driver.find_element(by=By.ID,value="txtPassword").send_keys("admin123")
       driver.find_element(by=By.ID,value="btnLogin").click()
    #def test_c():
     #       print("test passed")
      #      driver.close()
