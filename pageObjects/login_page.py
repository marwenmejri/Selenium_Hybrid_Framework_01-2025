from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_login = self.driver.find_element(by=By.ID, value='username')
        username_login.send_keys(username)

    def set_password(self, password):
        password_login = self.driver.find_element(by=By.ID, value='password')
        password_login.send_keys(password)

    def login(self):
        login_btn = self.driver.find_element(by=By.ID, value='submit')
        login_btn.click()

    def logout(self):
        logout_btn = self.driver.find_element(by=By.XPATH, value="(//a[normalize-space()='Log out'])[1]")
        logout_btn.click()


if __name__ == '__main__':
    driver1 = Chrome()
    driver1.maximize_window()
    driver1.get(url='https://practicetestautomation.com/practice-test-login/')
    # print(driver1.page_source)
    lp = LoginPage(driver=driver1)
    time.sleep(2)
    lp.set_username(username='student')
    time.sleep(2)
    lp.set_password(password='Password123')
    time.sleep(2)
    lp.login()
    time.sleep(2)
    lp.logout()
    time.sleep(2)
    driver1.quit()
