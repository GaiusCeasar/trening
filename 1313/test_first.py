from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('/home/max/PycharmProjects/simla/chromedriver')
browser.maximize_window()
browser.get('https://pre.webshop.retailcrm.ucann.ru')
time.sleep(1)
xpath = ('/html/body/div[1]/div/div/div[1]/div[1]/div/form/span[1]')
browser.find_element_by_xpath(xpath).click()
time.sleep(2)

login_xpath = ('/html/body/div[1]/div/div/div[1]/div[1]/div/form/span[1]/label/input')
browser.find_element_by_xpath(login_xpath).clear()
browser.find_element_by_xpath(login_xpath).send_keys('m.ivahnenko@sprintf.ru')

pas_xpath = ('/html/body/div[1]/div/div/div[1]/div[1]/div/form/span[2]/label/input')
browser.find_element_by_xpath(pas_xpath).send_keys('Simla24')

button_xpath = ('/html/body/div[1]/div/div/div[1]/div[1]/div/button')
browser.find_element_by_xpath(button_xpath).click()
time.sleep(4)

browser.get('https://pre.webshop.retailcrm.ucann.ru/catalog')
#catalog_xpath = ('/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/a[2]/div')
time.sleep(3)



plus_xpath = ('/html/body/div[1]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/div/button[2]')
browser.find_element_by_xpath(plus_xpath).click()

browser.get('https://pre.webshop.retailcrm.ucann.ru/cart')
time.sleep(3)


of_xpath = ('/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[4]/button/span/div')
browser.find_element_by_xpath(of_xpath).click()
html = browser.find_element_by_tag_name('html')
for i in range(25):
    html.send_keys(Keys.DOWN)
time.sleep(3)

self_delivery_xpath = ('/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[3]/div/div[3]/div')
browser.find_element_by_xpath(self_delivery_xpath).click()
time.sleep(1)

cash_xpath = ('/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[1]/div')
browser.find_element_by_xpath(cash_xpath).click()

order_xpath = ('/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/button')
browser.find_element_by_xpath(order_xpath).click()


browser.save_screenshot('Order.png')







#browser.quit()
