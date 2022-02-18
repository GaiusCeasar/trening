from selenium import webdriver
import time
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
time.sleep(5)

xpath_sum = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section/div[2]/div[1]/div[2]/span/div/div/input')
browser.find_element_by_xpath(xpath_sum).send_keys('102486')

xpath_enter_surname = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section/div[2]/div[2]/div[1]/div[1]/label/span/div/div/input')
browser.find_element_by_xpath(xpath_enter_surname).send_keys('Иванов')

xpath_enter_name = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section/div[2]/div[2]/div[1]/div[2]/label/span/div/div/input')
browser.find_element_by_xpath(xpath_enter_name).send_keys('Иван')

xpath_enter_patronymic = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section/div[2]/div[2]/div[1]/div[3]/label/span/div/div/input')
browser.find_element_by_xpath(xpath_enter_patronymic).send_keys('Иванович')

xpath_enter_date = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section/div[2]/div[2]/div[2]/span/div/div/div/div/div/input')
browser.find_element_by_xpath(xpath_enter_date).send_keys('01.01.1990')

html = browser.find_element_by_tag_name('html')
for i in range(25):
    html.send_keys(Keys.DOWN)

xpath_gender = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section/div[2]/div[2]/div[4]/div/label[1]/span')
browser.find_element_by_xpath(xpath_gender).click()

for i in range(25):
    html.send_keys(Keys.UP)

xpath_get_calculation = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[2]/button')
browser.find_element_by_xpath(xpath_get_calculation).click()
time.sleep(3)

xpath_get_abc = ('/html/body/div/div/div/main/div[2]/div[4]/div[1]/div[2]/div[2]')
browser.find_element_by_xpath(xpath_get_abc).click()

xpath_get_of = ('/html/body/div/div/div/main/div[2]/div[4]/div[2]/button')
browser.find_element_by_xpath(xpath_get_of).click()
time.sleep(2)

xpath_input_invalid = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[1]/div[2]/div[2]/span/div/div/input')
browser.find_element_by_xpath(xpath_input_invalid).send_keys('154631')

xpath_input_persent = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section[1]/div[2]/div[6]/span/div/div/input')
browser.find_element_by_xpath(xpath_input_persent).send_keys('6')

for i in range(5):
    html.send_keys(Keys.DOWN)

xpath_new_person = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[2]/div[2]/button')
browser.find_element_by_xpath(xpath_new_person).click()
time.sleep(2)

xpath_place_birth = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[3]/div[2]/form/div[1]/div[5]/input')
browser.find_element_by_xpath(xpath_place_birth).send_keys('Камышин')

xpath_telephon = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[3]/div[2]/form/div[1]/div[7]/span/div/div/input')
browser.find_element_by_xpath(xpath_telephon).send_keys('89261234567')

xpath_mail_person = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[3]/div[2]/form/div[1]/div[8]/span/div/div/input')
browser.find_element_by_xpath(xpath_mail_person).send_keys('Ivanov465464@ya.ru')

xpath_possport = ('/html/body/div/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[3]/div[2]/form/div[2]/div[1]/span/div/div/input')
browser.find_element_by_xpath(xpath_possport).send_keys('1547')

xpath_passport_number = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[3]/div[2]/form/div[2]/div[2]/span/div/div/input')
browser.find_element_by_xpath(xpath_passport_number).send_keys('154711')

xpath_passport_get = ('/html/body/div[1]/div/div/main/div[2]/div[4]/span/form/div[1]/section[3]/div[3]/div[2]/form/div[2]/div[4]/span/div/div/input')
browser.find_element_by_xpath(xpath_passport_get).send_keys('ОУФМС Камышин')