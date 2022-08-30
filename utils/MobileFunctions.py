import inspect
import logging

from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
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
        elif locatorType == "accessibility_id":
            ele = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue)
            ele.click()
            return ele
        elif locatorType == "css_selector":
            ele = self.driver.find_element(AppiumBy.CSS_SELECTOR, locatorValue)
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
        else:
            print(locatorType + " " + "not found")

        return ele


    def presence_of_element_located(self, locatorType, locatorValue):

        locatorType = locatorType.lower()
        ele = None
        try:
            if locatorType == "xpath":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.XPATH, locatorValue))
                return ele
            elif locatorType == "id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.id, locatorValue))
                return ele
            elif locatorType == "accessibility_id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                return ele
            elif locatorType == "css_selector":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.CSS_SELECTOR, locatorValue))
                return ele
            elif locatorType == "className":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.CLASS_NAME, locatorValue))
                return ele
            elif locatorType == "name":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.NAME, locatorValue))
                return ele
            elif locatorType == "link_text":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.LINK_TEXT, locatorValue))
                return ele
            else:
                print(locatorType + " " + "not found")

            return ele
        except:
            raise Exception

    def element_to_be_clickable(self, locatorType, locatorValue):

        locatorType = locatorType.lower()
        ele = None
        try:
            if locatorType == "xpath":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.element_to_be_clickable(AppiumBy.XPATH, locatorValue))
                return ele
            elif locatorType == "id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.element_to_be_clickable(AppiumBy.id, locatorValue))
                return ele
            elif locatorType == "accessibility_id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(
                    expected_conditions.element_to_be_clickable(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                return ele
            elif locatorType == "css_selector":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.element_to_be_clickable(AppiumBy.CSS_SELECTOR, locatorValue))
                return ele
            elif locatorType == "className":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.element_to_be_clickable(AppiumBy.CLASS_NAME, locatorValue))
                return ele
            elif locatorType == "name":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.element_to_be_clickable(AppiumBy.NAME, locatorValue))
                return ele
            elif locatorType == "link_text":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.element_to_be_clickable(AppiumBy.LINK_TEXT, locatorValue))
                return ele
            else:
                print(locatorType + " " + "not found")

            return ele
        except:
            raise Exception

    def text_to_be_present_in_element(self, locatorType, locatorValue):

        locatorType = locatorType.lower()
        ele = None
        try:
            if locatorType == "xpath":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.text_to_be_present_in_element(AppiumBy.XPATH, locatorValue))
                return ele
            elif locatorType == "id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.text_to_be_present_in_element(AppiumBy.id, locatorValue))
                return ele
            elif locatorType == "accessibility_id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(
                    expected_conditions.text_to_be_present_in_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                return ele
            elif locatorType == "css_selector":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.text_to_be_present_in_element(AppiumBy.CSS_SELECTOR, locatorValue))
                return ele
            elif locatorType == "className":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.text_to_be_present_in_element(AppiumBy.CLASS_NAME, locatorValue))
                return ele
            elif locatorType == "name":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.text_to_be_present_in_element(AppiumBy.NAME, locatorValue))
                return ele
            elif locatorType == "link_text":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(expected_conditions.text_to_be_present_in_element(AppiumBy.LINK_TEXT, locatorValue))
                return ele
            else:
                print(locatorType + " " + "not found")

            return ele
        except:
            raise Exception

    def select_by_visible_text(self, locatorType, locatorValue, text):
        locatorType = locatorType.lower()
        sel = None
        try:
            if locatorType == "xpath":
                sel = Select(self.driver.find_element(AppiumBy.XPATH, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            if locatorType == "id":
                sel = Select(self.driver.find_element(AppiumBy.ID, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            if locatorType == "accessibility_id":
                sel = Select(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            if locatorType == "css_selector":
                sel = Select(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            elif locatorType == "className":
                sel = Select(self.driver.find_element(AppiumBy.CLASS_NAME, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            elif locatorType == "name":
                sel = Select(self.driver.find_element(AppiumBy.NAME, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            elif locatorType == "link_text":
                sel = Select(self.driver.find_element(AppiumBy.LINK_TEXT, locatorValue))
                sel.select_by_visible_text(text)
                return sel
            else:
                print(locatorType + " " + "not found")

            return sel
        except:
            raise Exception

    def select_by_value(self, locatorType, locatorValue, value):
        locatorType = locatorType.lower()
        sel = None
        try:
            if locatorType == "xpath":
                sel = Select(self.driver.find_element(AppiumBy.XPATH, locatorValue))
                sel.select_by_value(value)
                return sel
            if locatorType == "id":
                sel = Select(self.driver.find_element(AppiumBy.ID, locatorValue))
                sel.select_by_value(value)
                return sel
            if locatorType == "accessibility_id":
                sel = Select(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                sel.select_by_value(value)
                return sel
            if locatorType == "css_selector":
                sel = Select(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                sel.select_by_value(value)
                return sel
            elif locatorType == "className":
                sel = Select(self.driver.find_element(AppiumBy.CLASS_NAME, locatorValue))
                sel.select_by_value(value)
                return sel
            elif locatorType == "name":
                sel = Select(self.driver.find_element(AppiumBy.NAME, locatorValue))
                sel.select_by_value(value)
                return sel
            elif locatorType == "link_text":
                sel = Select(self.driver.find_element(AppiumBy.LINK_TEXT, locatorValue))
                sel.select_by_value(value)
                return sel
            else:
                print(locatorType + " " + "not found")

            return sel
        except:
            raise Exception

    def select_by_index(self, locatorType, locatorValue, index):
        locatorType = locatorType.lower()
        sel = None
        try:
            if locatorType == "xpath":
                sel = Select(self.driver.find_element(AppiumBy.XPATH, locatorValue))
                sel.select_by_index(index)
                return sel
            if locatorType == "id":
                sel = Select(self.driver.find_element(AppiumBy.ID, locatorValue))
                sel.select_by_index(index)
                return sel
            if locatorType == "accessibility_id":
                sel = Select(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                sel.select_by_index(index)
                return sel
            if locatorType == "css_selector":
                sel = Select(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue))
                sel.select_by_index(index)
                return sel
            elif locatorType == "className":
                sel = Select(self.driver.find_element(AppiumBy.CLASS_NAME, locatorValue))
                sel.select_by_index(index)
                return sel
            elif locatorType == "name":
                sel = Select(self.driver.find_element(AppiumBy.NAME, locatorValue))
                sel.select_by_index(index)
                return sel
            elif locatorType == "link_text":
                sel = Select(self.driver.find_element(AppiumBy.LINK_TEXT, locatorValue))
                sel.select_by_index(index)
                return sel
            else:
                print(locatorType + " " + "not found")

            return sel
        except:
            raise Exception

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

    def forceClick(self, locatorType):
        ele = None
        try:
            ele = self.driver.find_element(locatorType)
            action = ActionChains(self.driver)
            action.click(on_element=ele)
            action.perform()
        except:
            raise Exception

    def click_and_hold(self, locatorType):
        ele = None
        try:
            ele = self.driver.find_element(locatorType)
            action = ActionChains(self.driver)
            action.click_and_hold(on_element=ele)
            action.perform()
        except:
            raise Exception

    def rightClick(self, locatorType):
        ele = None
        try:
            ele = self.driver.find_element(locatorType)
            action = ActionChains(self.driver)
            action.context_click(on_element=ele)
            action.perform()
        except:
            raise Exception

    def doubleClick(self, locatorType):
        ele = None
        try:
            ele = self.driver.find_element(locatorType)
            action = ActionChains(self.driver)
            action.double_click(on_element=ele)
            action.perform()
        except:
            raise Exception

    def doubleClick(self, source_ele, target_ele):

        try:
            source_element = self.driver.find_element(source_ele)
            target_element = self.driver.find_element(target_ele)
            action = ActionChains(self.driver)
            action.drag_and_drop(source_element, target_element)
            action.perform()
        except:
            raise Exception

    def doubleClick(self, locatorType):
        ele = None
        try:
            ele = self.driver.find_element(locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(ele).click().perform()
        except:
            raise Exception
