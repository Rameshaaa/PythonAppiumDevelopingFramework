import inspect
import logging

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import configparser


class base:

    def __init__(self):
        self.driver = None

    def getAndroidEmulator(self):
        config = configparser.ConfigParser()
        config.read('/Users/bosch/Desktop/PythonTestingFramework/features/properties.ini')
        #data = config['AndroidEmulator']['platformName']

        # caps = {
        #     "platformName": config['AndroidEmulator']['platformName'],
        #     "platformVersion": config['AndroidEmulator']['platformVersion'],
        #     "deviceName": config['AndroidEmulator']['deviceName'],
        #     "appPackage": config['AndroidEmulator']['appPackage'],
        #     "appActivity": config['AndroidEmulator']['appActivity'],
        #     "udid": config['AndroidEmulator']['udid']
        # }
        caps = {
             "platformName": "Android",
             "platformVersion": "12.0",
             "deviceName": "OnePlus 8 5G",
             "appPackage": "com.pta.nevro.nevroptaandroid",
             "appActivity": "com.pta.nevro.nevroptaandroid.ui.common.SplashActivity",
             "udid": "f4306c03"
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

    def enterText(self, locatorType, locatorValue, value: str):

        locatorType = locatorType.lower()
        ele = None

        if locatorType == "xpath":
            ele = self.driver.find_element(AppiumBy.XPATH, locatorValue)
            ele.send_keys(value)
            return ele
        elif locatorType == "id":
            ele = self.driver.find_element(AppiumBy.ID, locatorValue)
            ele.send_keys(value)
            return ele
        elif locatorType == "accessibility_id":
            ele = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locatorValue)
            ele.send_keys(value)
            return ele
        elif locatorType == "css_selector":
            ele = self.driver.find_element(AppiumBy.CSS_SELECTOR, locatorValue)
            ele.send_keys(value)
            return ele
        elif locatorType == "className":
            ele = self.driver.find_element(AppiumBy.CLASS_NAME, locatorValue)
            ele.send_keys(value)
            return ele
        elif locatorType == "name":
            ele = self.driver.find_element(AppiumBy.NAME, locatorValue)
            ele.send_keys(value)
            return ele
        elif locatorType == "link_text":
            ele = self.driver.find_element(AppiumBy.LINK_TEXT, locatorValue)
            ele.send_keys(value)
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
                ele = wait.until(expected_conditions.presence_of_element_located(AppiumBy.ID, locatorValue))
                return ele
            elif locatorType == "accessibility_id":
                wait = WebDriverWait(self.driver, 25, poll_frequency=2)
                ele = wait.until(
                    expected_conditions.presence_of_element_located(AppiumBy.ACCESSIBILITY_ID, locatorValue))
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

    def quit(self):
        self.driver.close()

    def listElements_iterator(self, locatorType, text):
        try:
            ele = None
            ele = self.driver.find_elements(locatorType)

            for el in ele:
                # print(el.text)
                if el.text == text:
                    el.click()
                else:
                    raise Exception
            return ele
        except:
            raise Exception

    def scrollelemnet(self, source_ele, target_ele):
        try:
            action = TouchAction(self.driver)
            action.press(source_ele).move_to(target_ele).release().perform()
        except:
            raise Exception
