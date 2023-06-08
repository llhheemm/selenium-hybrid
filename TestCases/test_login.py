import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.LoginPage import LoginPage
from Utilities.properties import ReadConfig

class Test_01_Login:
    URL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_login(self):
        self.driver
