from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('/home/max/PycharmProjects/simla/chromedriver')
browser.maximize_window()
browser.get('http://ip-master.test.fast-system.ru/')

xpath_email = ('/html/body/div/div/div/div[1]/div/div/form/div[1]/span/div/div/input')
browser.find_element_by_xpath(xpath_email).clear()
browser.find_element_by_xpath(xpath_email).send_keys('per@tect.ru')

xpath_password = ('/html/body/div[1]/div/div/div[1]/div/div/form/div[2]/div/span/div/div/input')
browser.find_element_by_xpath(xpath_password).clear()
browser.find_element_by_xpath(xpath_password).send_keys('4567Saf')
time.sleep(1)

xpath_enter = ('/html/body/div/div/div/div[1]/div/div/form/button')
browser.find_element_by_xpath(xpath_enter).click()
time.sleep(3)

xpath_create = ('/html/body/div/div/div/main/div[2]/div/div[1]/div[1]/button')
browser.find_element_by_xpath(xpath_create).click()
time.sleep(2)

xpath_detailed_calculation = ('/html/body/div[1]/div/div/main/div[2]/div[3]/button[2]')
browser.find_element_by_xpath(xpath_detailed_calculation).click()
time.sleep(4)

#element = WebDriverWait(browser, 10).until(
#EC.presence_of_element_located((By.CLASS_NAME, "underline"))


xpath_choose_product = ('/html/body/div[1]/div/div/main/div[2]/div[2]/h2/span')
browser.find_element_by_xpath(xpath_choose_product).click()

browser.save_screenshot('list_products.png')

xpath_close_choose_product = ('/html/body/div[1]/div/div/main/div[2]/div[5]/div[2]/button')
browser.find_element_by_xpath(xpath_close_choose_product).click()

xpath_enter_number = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[1]/div[2]/div[2]/span/div/div/input')
browser.find_element_by_xpath(xpath_enter_number).clear()
browser.find_element_by_xpath(xpath_enter_number).send_keys('16461231')

xpath_enter_sum = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[1]/div[2]/div[3]/span/div/div/input')
browser.find_element_by_xpath(xpath_enter_sum).clear()
browser.find_element_by_xpath(xpath_enter_sum).send_keys('16461231')

xpath_enter_rate = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[1]/div[2]/div[6]/span/div/div/input')
browser.find_element_by_xpath(xpath_enter_rate).clear()
browser.find_element_by_xpath(xpath_enter_rate).send_keys('6.1')

html = browser.find_element_by_tag_name('html')
for i in range(5):
    html.send_keys(Keys.DOWN)

xpath_choose_client = ('//*[@id="__layout"]/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[2]/div[1]/span/div/div/span/div/div/div/div/label/input')
browser.find_element_by_xpath(xpath_choose_client).clear()
browser.find_element_by_xpath(xpath_choose_client).send_keys('Ветров')

xpath_choose_client_click = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[2]/div[1]/span/div/div/span/div/div/div/ul/li[1]')
browser.find_element_by_xpath(xpath_choose_client_click).click()



pre-1.simla.retailcrm.sprintf.ru

#browser.quit()