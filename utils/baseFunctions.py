import inspect
import logging

from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class base:

    def getAndroidEmulator(self):
        caps = {
            "platformName": "Android",
            "platformVersion": "11.0",
            "deviceName": "Pixel 5 Emulator",
            "appPackage": "com.android.settings",
            "appActivity": "com.android.settings.Settings"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def clickElement(self, locatorType, locatorValue):

        locatorType = locatorType.lower()
        ele = None

        if locatorType == "xpath":
            ele = self.driver.find_element(AppiumBy.XPATH, locatorValue)
            ele.click()
            return ele
        elif locatorType == "id":
            ele = self.driver.find_element(AppiumBy.ID, locatorValue)
            ele.click()
            return ele
        elif locatorType == "className":
            ele = self.driver.find_element(AppiumBy.CLASS_NAME, locatorValue)
            ele.click()
            return ele
        elif locatorType == "name":
            ele = self.driver.find_element(AppiumBy.NAME, locatorValue)
            ele.click()
            return ele
        elif locatorType == "link_text":
            ele = self.driver.find_element(AppiumBy.LINK_TEXT, locatorValue)
            ele.click()
            return ele
        elif locatorType == "css_selector":
            ele = self.driver.find_element(AppiumBy.CSS_SELECTOR, locatorValue)
            ele.click()
            return ele
        elif locatorType == "accessibility_id":
            ele = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue)
            ele.click()
            return ele
        else:
            print("Locator Type" + " " + "not found")

        return ele

    def presence_of_element_located(self, locatorType):

        try:
            ele = None
            wait = WebDriverWait(self.driver, 25, poll_frequency=2)
            ele = wait.until(expected_conditions.presence_of_element_located(locatorType))
            return ele
        except TimeoutException as ex:
            print(ex.message)

    def element_to_be_clickable(self, locatorType):

        try:
            ele = None
            wait = WebDriverWait(self.driver, 25, poll_frequency=2)
            ele = wait.until(expected_conditions.element_to_be_clickable(locatorType))
            return ele
        except TimeoutException as ex:
            print(ex.message)

    def text_to_be_present_in_element(self, locatorType, text):

        try:
            ele = None
            wait = WebDriverWait(self.driver, 25, poll_frequency=2)
            ele = wait.until(expected_conditions.text_to_be_present_in_element(locatorType))
            return ele
        except TimeoutException as ex:
            print(ex.message)

    def select_by_visible_text(self, locatorType, text):
        try:
            sel = Select(locatorType)
            sel.select_by_visible_text(text)
            return sel
        except Exception as ex:
            print(ex.message)

    def select_by_value(self, locatorType, value):
        try:
            sel = Select(locatorType)
            sel.select_by_value(value)
            return sel
        except Exception as ex:
            print(ex.message)

    def select_by_index(self, locatorType, index):
        try:
            sel = Select(locatorType)
            sel.select_by_index(index)
            return sel
        except Exception as ex:
            print(ex.message)

    def listElements(self, locatorType, text):
        try:
            ele = None
            ele = self.driver.find_elements(locatorType)

            for el in ele:
                print(el.text)
                if el.text == text:
                    el.click()
                else:
                    raise Exception
            return ele
        except:
            print("Issue with Iterator")
