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
        time.sleep(2)

        birth_option = driver.find_elements_by_xpath("//*[contains(text(), '請提供你的生日')]")
        approve_option = driver.find_elements_by_xpath("//*[contains(text(), '允許從其他電腦登入')]")

        if(len(birth_option) > 0):
            birth_option[0].click()
            time.sleep(2)
            date= driver.find_elements_by_css_selector("span._55pe")
            driver.execute_script("arguments[0].innerText = '{}'".format(os.getenv("year")), date[2])
            driver.execute_script("arguments[0].innerText = '{}月'".format(os.getenv("month")), date[3])
            driver.execute_script("arguments[0].innerText = '{}'".format(os.getenv("day")), date[4])
            keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")[0]
            keepGo.click()
            username = driver.find_elements_by_css_selector("input[name=email]")
            if(len(username) > 0):
                username[0].send_keys(os.getenv("EMAIL"))
                password = driver.find_elements_by_css_selector("input[name=pass]")[0]
                password.send_keys(os.getenv("PASSWORD"))
                login_button = driver.find_elements_by_css_selector("input[type=submit]")[0]
                login_button.click()

        elif(len(approve_option) > 0):
            approve_option[0].click()

            keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")[0]
            keepGo.click()

            count = 0
            is_filled = False

            while count < 20 and is_filled == False:
                keepGo = driver.find_elements_by_css_selector("#checkpointSubmitButton")
                if(len(keepGo) > 0):
                    keepGo[0].click()
                    time.sleep(2)

                username = driver.find_elements_by_css_selector("input[name=email]")
                if(len(username) > 0):
                    username[0].send_keys(os.getenv("EMAIL"))
                    password = driver.find_elements_by_css_selector("input[name=pass]")[0]
                    password.send_keys(os.getenv("PASSWORD"))
                    login_button = driver.find_elements_by_css_selector("input[type=submit]")[0]
                    login_button.click()
                    is_filled = True
                else: 
                    count += 1
                    print('try again')
                    time.sleep(5)


