from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import os
import time
from dotenv import load_dotenv
load_dotenv()

def check_auth(driver):
  keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")
  if(len(keepGo) > 0):
    keepGo[0].click()
    time.sleep(5)

    radio = driver.find_elements_by_css_selector("input[name=verification_method]~ span")[0]
    radio.click()

    keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")[0]
    keepGo.click()
    
    count = 0
    is_filled = False

    while count < 20 and is_filled == False:
      keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")
      if (len(keepGo) > 0):
        keepGo[0].click()
        time.sleep(2)
      
      username = driver.find_elements_by_css_selector("input[name=email]")
      if(len(username) > 0):
        username[0].send_keys(os.getenv("EMAIL"))
        password = driver.find_elements_by_css_selector("input[name=pass]")[0]
        password.send_keys(os.getenv("PASSWORD"))
        login_button = driver.find_elements_by_css_selector("input[type=submit]")[0]
        driver.save_screenshot('img.png')
        login_button.click()
        is_filled = True
      else: 
        count += 1
        print('try again')
        time.sleep(5)


