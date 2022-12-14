import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from behave import *
from appium import webdriver
import configparser
from pageObjects.objectRepo import objectRepos
from utils.MobileFunctions import base


class settings(base):



    @given('Launch the Calculator App')
    def launch_Settings_app(self):
        #base.getAndroidEmulator(self)
        log = base.getlogger(self)
        log.info("Emulator Launched")


    @when('Open the Network and Settings')
    def click_first_option_in_the_settings_Lists(self):
        pageobjects = objectRepos()
        log = base.getlogger(self)
        time.sleep(3)
        base.clickElement(self, "xpath", pageobjects.network_security)
        log.info("Element clicked")
        time.sleep(10)


    @then('look for other options')
    def app_close(self):
        pass
