import time
# pytest -v --driver Chrome --driver-path E:/test/chromedriver.exe  test_simla_autor.py

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    selenium.maximize_window()
    selenium.get('https://pre.webshop.retailcrm.ucann.ru/')

    time.sleep(1)
    search_menu = selenium.find_element_by_class_name('WebHeaderBurger')
    search_menu.click()
    search_enter = selenium.find_element_by_class_name('WebHeader_login_enter_name')

    search_enter.click()

    search_input_login = selenium.find_element_by_name('login')
    search_input_login.clear()
    search_input_login.send_keys('m.ivahnenko@sprintf.ru')

    time.sleep(1)

    search_input_pw = selenium.find_element_by_name('password')
    search_input_pw.clear()
    search_input_pw.send_keys('Simla24')

    btn_submit = selenium.find_element_by_class_name('WebModalLogin_button')
    btn_submit.click()



    time.sleep(5)


    selenium.save_screenshot('result2.png')

