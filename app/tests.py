from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
import time
# WEBDRIVER_PATH ='/home/blackhil/.cache/selenium/chromedriver/linux64/113.0.5672.63/webdriver'
# SELENIUM_OPTIONS = [
#     '--headless',  # Run in headless mode (without a visible browser window)
#     '--no-sandbox',  # Add additional options as needed
# ]

class test(LiveServerTestCase):
    class test(LiveServerTestCase):
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        time.sleep(9)
        driver.quit()
