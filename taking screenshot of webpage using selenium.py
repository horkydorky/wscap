from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
time.sleep(6)

#set path
path=r"C:\Users\adhik\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service=Service(executable_path=path)
browser=webdriver.Chrome(service=service)
#url rakhne
url="https://www.google.com/"
browser.get(url)
browser.save_screenshot('screenshot.png')
browser.quit()