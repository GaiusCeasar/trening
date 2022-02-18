from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('/home/max/PycharmProjects/simla/chromedriver')
browser.maximize_window()
browser.get('http://ipfront-feature-astmi-485.test.fast-system.ru/')

browser.execute_script("window.open('https://twitter.com')")

tabs = browser.window_handles #get list of open windows

browser.switch_to.window(tabs[1])
#browser.close() #close the current window
time.sleep(3)
browser.switch_to.window(tabs[0]) #return to first window