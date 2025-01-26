# from selenium.webdriver import Chrome

import time
from pageObjects.login_page import LoginPage
from utilities.customLogger import sample_logger


class Test001Login:
    baseURL = "https://practicetestautomation.com/practice-test-login/"
    # baseURL = get_baseurl()
    username = "student11"
    password = "Password123"
    logger = sample_logger(mode='a', filename='Logs/logs.log', name='custom_logger1')

    def test_login_page_title(self, setup):
        self.logger.info("************ Test001Login ************\n")
        self.logger.info("************ test_login_page_title STARTED ************")
        driver = setup
        # driver = Chrome()
        driver.get(url=self.baseURL)
        # time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver.title == expected_title:
            self.logger.info("************ test_login_page_title PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_login_page_title_failure.png")
            self.logger.error("************ test_login_page_title FAILED ************")
            # driver.quit()
            assert False

    def test_login_positive(self, setup):
        self.logger.info("************ test_login_positive STARTED ************")
        driver = setup
        # driver = Chrome()
        driver.get(url=self.baseURL)
        # time.sleep(2)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        # time.sleep(2)
        lp.set_password(password=self.password)
        # time.sleep(2)
        lp.login()
        # time.sleep(2)
        new_page_title = driver.title
        expected_string_title = "Logged In Successfully | Practice Test Automation"
        if new_page_title == expected_string_title:
            lp.logout()
            self.logger.info("************ test_login_positive PASSED ************")
            # time.sleep(2)
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_login_positive_failure.png")
            self.logger.error("************ test_login_positive FAILED ************")
            # time.sleep(2)
            # driver.quit()
            assert False

    def test_negative_username(self, setup):
        self.logger.info("************ test_negative_username STARTED ************")
        driver = setup
        # driver = Chrome()
        driver.get(url=self.baseURL)
        # time.sleep(2)
        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        # time.sleep(2)
        lp.set_password(password=self.password)
        # time.sleep(2)
        lp.login()
        # time.sleep(2)
        if "Your username is invalid!" in driver.page_source:
            self.logger.info("************ test_negative_username PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_negative_username_failure.png")
            self.logger.error("************ test_negative_username FAILED ************")
            # driver.quit()
            assert False


class Test002Login:
    baseURL = "https://practicetestautomation.com/practice-test-login/"
    # baseURL = get_baseurl()
    username = "student"
    password = "Password123"
    logger = sample_logger(mode='a', filename='Logs/logs.log', name='custom_logger2')

    def test_login_page_title2(self, setup):
        self.logger.info("************ Test002Login ************\n")
        self.logger.info("************ test_login_page_title2 STARTED ************")
        driver = setup
        # driver = Chrome()
        driver.get(url=self.baseURL)
        # time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver.title == expected_title:
            self.logger.info("************ test_login_page_title2 PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_login_page_title_failure2.png")
            self.logger.error("************ test_login_page_title2 FAILED ************")
            # driver.quit()
            assert False

    def test_login_positive2(self, setup):
        self.logger.info("************ test_login_positive2 STARTED ************")
        driver = setup
        # driver = Chrome()
        driver.get(url=self.baseURL)
        # time.sleep(2)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        # time.sleep(2)
        lp.set_password(password=self.password)
        # time.sleep(2)
        lp.login()
        # time.sleep(2)
        new_page_title = driver.title
        expected_string_title = "Logged In Successfully | Practice Test Automation"
        if new_page_title == expected_string_title:
            lp.logout()
            self.logger.info("************ test_login_positive2 PASSED ************")
            # time.sleep(2)
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_login_positive_failure2.png")
            self.logger.error("************ test_login_positive2 FAILED ************")
            # time.sleep(2)
            # driver.quit()
            assert False

    def test_negative_username2(self, setup):
        self.logger.info("************ test_negative_username2 STARTED ************")
        driver = setup
        # driver = Chrome()
        driver.get(url=self.baseURL)
        # time.sleep(2)
        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        # time.sleep(2)
        lp.set_password(password=self.password)
        # time.sleep(2)
        lp.login()
        # time.sleep(2)
        if "Your username is invalid!" in driver.page_source:
            self.logger.info("************ test_negative_username2 PASSED ************")
            # driver.quit()
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_negative_username_failure2.png")
            self.logger.error("************ test_negative_username2 FAILED ************")
            # driver.quit()
            assert False
