from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import os
import time
from dotenv import load_dotenv
load_dotenv()

options = Options()
options.add_argument("--disable-notifications")
options.add_argument('--headless')
driver = webdriver.Chrome(os.getcwd() + '/chromedriver', chrome_options=options)
driver.get('https://www.facebook.com')
driver.set_window_size(1024, 768)

username = driver.find_elements_by_css_selector("input[name=email]")[0]
username.send_keys(os.getenv("EMAIL"))
password = driver.find_elements_by_css_selector("input[name=pass]")[0]
password.send_keys(os.getenv("PASSWORD"))
login_button = driver.find_elements_by_css_selector("input[type=submit]")[0]
login_button.click()

keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")[0]
keepGo.click()
time.sleep(2)

radio = driver.find_elements_by_css_selector("input[name=verification_method]~ span")[1]
radio.click()

keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")[0]
keepGo.click()

check = input('請輸入 start 已繼續：')
if (check == 'start'):
  keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")[0]
  keepGo.click()
  time.sleep(2)