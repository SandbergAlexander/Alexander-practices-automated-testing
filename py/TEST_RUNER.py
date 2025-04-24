from selenium import webdriver
from selenium.webdriver.common.by import By
driver =  webdriver.Chrome()
driver.get("http://127.0.0.1:5500/test-app-or-home-page/simpel-home-page/index.html")
driver.close()