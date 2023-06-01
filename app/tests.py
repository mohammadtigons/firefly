# from django.test import TestCase
# from django.test import LiveServerTestCase
# from selenium import webdriver
# import time
# # WEBDRIVER_PATH ='/home/blackhil/.cache/selenium/chromedriver/linux64/113.0.5672.63/webdriver'
# # SELENIUM_OPTIONS = [
# #     '--headless',  # Run in headless mode (without a visible browser window)
# #     '--no-sandbox',  # Add additional options as needed
# # ]

# class test(LiveServerTestCase):
#     class test(LiveServerTestCase):
#         driver = webdriver.Chrome()
#         driver.get('https://www.google.com')
#         time.sleep(9)
#         driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
ser = Service(r"./driver/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://www.google.com")
get_url = driver.current_url
print("The current url is:"+str(get_url))
time.sleep(6)
driver.quit()
