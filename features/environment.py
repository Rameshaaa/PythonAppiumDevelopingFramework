from appium import webdriver
from behave import *
from utils import MobileFunctions
from utils.MobileFunctions import base


class env(base):

    def before_scenario(self, scenario):
        base.getAndroidEmulator()

    def after_feature(self, scenario):
        base.quit()