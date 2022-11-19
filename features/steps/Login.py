import time
from behave import *
from pageObjects.objectRepo import objectRepos
from utils.MobileFunctions import base


class Login(base):
    @given(u'Launch the PTA App')
    def step_impl(self):
        base.getAndroidEmulator(self)
        log = base.getlogger(self)
        log.info("Emulator Launched")

    @when(u'User see the Login Screen')
    def step_impl(self):
        pageObjects = objectRepos
        log = base.getlogger(self)
        time.sleep(5)
        base.presence_of_element_located(self, "id", pageObjects.id_Continue_anyway)
        base.clickElement(self, "id", pageObjects.id_Continue_anyway)
        log.info(pageObjects.id_Continue_anyway + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_Skip_button)
        base.clickElement(self, "id", pageObjects.id_Skip_button)
        log.info(pageObjects.id_Skip_button + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_Accept_EULA)
        base.clickElement(self, "id", pageObjects.id_Accept_EULA)
        log.info(pageObjects.id_Accept_EULA + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_log_in_link)
        base.clickElement(self, "id", pageObjects.id_log_in_link)
        log.info(pageObjects.id_log_in_link + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_HFX_logo)
        log.info(pageObjects.id_HFX_logo + "is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_HFX_Find_account)
        log.info(pageObjects.id_HFX_Find_account + " is verified")

        base.enterText(self, "xpath", pageObjects.Xpath_HFX_Email, "rc@mailinator.com")
        log.info(pageObjects.Xpath_HFX_Email + " is verified")

        base.enterText(self, "xpath", pageObjects.xpath_HFX_password, "12345678")
        log.info(pageObjects.xpath_HFX_password + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_login_button)
        base.clickElement(self, "id", pageObjects.id_login_button)
        log.info(pageObjects.id_login_button + " is verified")


    @then(u'User able to see the spinner loading')
    def step_impl(self):
        pass
