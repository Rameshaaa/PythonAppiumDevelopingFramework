import time
from appium.webdriver.common.touch_action import TouchAction
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from features.steps.EmailGenrator import Random
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
        action = TouchAction(self.driver)
        pageObjects = objectRepos
        log = base.getlogger(self)
        time.sleep(5)
        #if pageObjects.id_Continue_anyway is not None:
         #Continue Anyway

        base.presence_of_element_located(self, "id", pageObjects.id_Continue_anyway)
        base.clickElement(self, "id", pageObjects.id_Continue_anyway)
        log.info(pageObjects.id_Continue_anyway + " is verified")
        #else:
        #Skip Button
        base.presence_of_element_located(self, "id", pageObjects.id_Skip_button)
        base.clickElement(self, "id", pageObjects.id_Skip_button)
        log.info(pageObjects.id_Skip_button + " is verified")

        #EULA
        base.presence_of_element_located(self, "id", pageObjects.id_Accept_EULA)
        base.clickElement(self, "id", pageObjects.id_Accept_EULA)
        log.info(pageObjects.id_Accept_EULA + " is verified")
        time.sleep(2)

        """
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

        """
        #Create Accouunt

        base.enterText(self, "xpath", pageObjects.xpath_email_create_acc, Random.random_email(3) + "@mailinator.com")
        log.info(pageObjects.xpath_email_create_acc + " is verified")

        base.enterText(self, "xpath", pageObjects.xpath_password_create_acc, "12345678")
        log.info(pageObjects.xpath_password_create_acc + " is verified")

        base.enterText(self, "xpath", pageObjects.xpath_confirm_password_create_acc, "12345678")
        log.info(pageObjects.xpath_confirm_password_create_acc + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_create_account_button)
        base.clickElement(self, "id", pageObjects.id_create_account_button)
        log.info(pageObjects.id_create_account_button + " is verified")

        #FN AND LN DETAILS
        time.sleep(90)
        base.enterText(self, "xpath", pageObjects.xpath_FN, "C")
        log.info(pageObjects.xpath_confirm_password_create_acc + " is verified")

        base.enterText(self, "xpath", pageObjects.xpath_LN, "C")
        log.info(pageObjects.xpath_confirm_password_create_acc + " is verified")

        #Touch Action - Tap by co-ordinates -- Keyboard Hides
        action.tap(self, 979, 2248, 200)
        time.sleep(3)

        #Next button from FN & LN
        base.presence_of_element_located(self, "id", pageObjects.id_next_button)
        base.clickElement(self, "id", pageObjects.id_next_button)
        log.info(pageObjects.id_next_button + " is verified")

        #Setup Later
        time.sleep(10)

        base.presence_of_element_located(self, "id", pageObjects.id_setup_later)
        base.clickElement(self, "id", pageObjects.id_setup_later)
        log.info(pageObjects.id_setup_later + " is verified")

        #Setup Later
        time.sleep(10)
        base.presence_of_element_located(self, "id", pageObjects.id_setup_later)
        base.clickElement(self, "id", pageObjects.id_setup_later)
        log.info(pageObjects.id_setup_later + " is verified")

        #Notification popup
        base.presence_of_element_located(self, "id", pageObjects.id_popup_allow)
        base.clickElement(self, "id", pageObjects.id_popup_allow)
        log.info(pageObjects.id_popup_allow + " is verified")

        time.sleep(10)
        #Start Scan button
        base.presence_of_element_located(self, "id", pageObjects.id_scan_button)
        base.clickElement(self, "id", pageObjects.id_scan_button)
        log.info(pageObjects.id_scan_button + " is verified")

        time.sleep(70)

        #BLE, Confirm Pain Area & Lets Begin Screen

        base.presence_of_element_located(self, "id", pageObjects.id_Continue_button)
        base.clickElement(self, "id", pageObjects.id_Continue_button)
        log.info(pageObjects.id_Continue_button + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_Confirmbutton)
        base.clickElement(self, "id", pageObjects.id_Confirmbutton)
        log.info(pageObjects.id_Confirmbutton + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_lets_begin)
        base.clickElement(self, "id", pageObjects.id_lets_begin)
        log.info(pageObjects.id_lets_begin + " is verified")

        #Home Assessment
        base.presence_of_element_located(self, "id", pageObjects.id_assessment)
        base.clickElement(self, "id", pageObjects.id_assessment)
        log.info(pageObjects.id_assessment + " is verified")

        #PainRelief Page
        base.presence_of_element_located(self, "id", pageObjects.id_title_assessment)
        log.info(pageObjects.id_title_assessment + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_card_heading)
        log.info(pageObjects.id_card_heading + " is verified")

        base.presence_of_element_located(self, "id", pageObjects.id_paincontrol_score)
        log.info(pageObjects.id_paincontrol_score + " is verified")

        time.sleep(5)


        start_x = 179
        start_y = 1300
        end_x = 609
        end_y = 749
        action = ActionChains(self.driver)
        actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_up()
        actions.pointer_action.pause(100)
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.release()
        actions.perform()

        action.long_press(None, start_x, start_y).move_to(None, end_x, end_y).release().perform()

    @then(u'User able to see the spinner loading')
    def step_impl(self):
        pass

