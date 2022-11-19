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
        #base.presence_of_element_located(self, "id", pageObjects.id_Continue_anyway)
        base.clickElement(self, "id", pageObjects.id_Continue_anyway)

        #base.presence_of_element_located(self, "id", pageObjects.id_Skip_button)
        base.clickElement(self, "id", pageObjects.id_Skip_button)

        #base.presence_of_element_located(self, "id", pageObjects.id_Accept_EULA)
        base.clickElement(self, "id", pageObjects.id_Accept_EULA)

        #base.presence_of_element_located(self, "id", pageObjects.id_log_in_link)
        base.clickElement(self, "id", pageObjects.id_log_in_link)


        #base.presence_of_element_located(self, "id", pageObjects.id_HFX_logo)
        log.info(pageObjects.id_HFX_logo + "is verified")
        #base.presence_of_element_located(self, "id", pageObjects.id_HFX_Find_account)
        base.enterText(self, "xpath", pageObjects.Xpath_HFX_Email, "rc@mailinator.com")
        base.enterText(self, "xpath", pageObjects.xpath_HFX_password, "12345678")
        #base.presence_of_element_located(self, "id", pageObjects.id_HFX_Find_account)
        base.clickElement(self, "id", pageObjects.id_login_button)


    @then(u'User able to see the spinner loading')
    def step_impl(self):
        pass
