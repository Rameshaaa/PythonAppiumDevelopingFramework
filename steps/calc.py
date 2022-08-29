import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from behave import *
from appium import webdriver
from pageObjects.objectRepo import objectRepo
from utils.baseFunctions import base


class settings(base):

    @given('Launch the Calculator App')
    def launch_Settings_app(self):
        base.getAndroidEmulator(self)
        log = base.getlogger(self)
        log.info("Emulator Launched")

    @when('Open the Network and Settings')
    def click_first_option_in_the_settings_Lists(self):
        pageobjects = objectRepo()
        log = base.getlogger(self)
        time.sleep(3)
        log.info("Element clicked")
        base.clickElement(self, 'xpath', pageobjects.networksecuirty)
        time.sleep(2)

    @then('look for other options')
    def app_close(self):
        self.driver.quit()
