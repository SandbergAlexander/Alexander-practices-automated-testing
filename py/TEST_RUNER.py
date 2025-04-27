from selenium import webdriver
from selenium.webdriver.common.by import By
def testR():
    driver =  webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/test-app-or-home-page/simpel-home-page/index.html")
    driver.close()
 
input = input("do want to start test from termal? ")
if (input=="yes"):
    testR()
else:
    print("start GUI ")

