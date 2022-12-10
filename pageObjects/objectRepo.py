from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class objectRepos:
    #network_security = (AppiumBy.XPATH, "//*[@text='Network & internet']")
    network_security = "//*[@text='Network & internet']"

    #Compatability Popup
    id_Continue_anyway = "android:id/button1"

    #EULA
    id_Skip_button = "com.pta.nevro.nevroptaandroid:id/skipBtn"
    id_Accept_EULA = "com.pta.nevro.nevroptaandroid:id/B1"

    #LoginPage Link
    id_log_in_link = "com.pta.nevro.nevroptaandroid:id/B65"

    #Create Account

    xpath_email_create_acc = "//android.widget.EditText[@content-desc='F3']"
    xpath_password_create_acc = "//android.widget.EditText[@content-desc='F4']"
    xpath_confirm_password_create_acc = "//android.widget.EditText[@content-desc='F5']"
    id_create_account_button = "com.pta.nevro.nevroptaandroid:id/B64"
    #wait more than 1 minute
    id_resend_verification = "com.pta.nevro.nevroptaandroid:id/B101"
    id_startwith_diff_email = "com.pta.nevro.nevroptaandroid:id/B102"

    # Login Page
    id_HFX_logo = "com.pta.nevro.nevroptaandroid:id/nevro_logo"
    id_HFX_Find_account = "com.pta.nevro.nevroptaandroid:id/nevro_logo"
    Xpath_HFX_Email = "//android.widget.EditText[@content-desc='F3']"
    xpath_HFX_password = "//android.widget.EditText[@content-desc='F7']"
    id_HFX_need_help = "com.pta.nevro.nevroptaandroid:id/B66"
    id_login_button = "com.pta.nevro.nevroptaandroid:id/B64"

    #User Details
    xpath_FN = "//android.widget.EditText[@content-desc='L91']"
    xpath_LN = "//android.widget.EditText[@content-desc='L92']"
    id_next_button = "com.pta.nevro.nevroptaandroid:id/B10"

    #SetupLaterr

    id_setup_later = "com.pta.nevro.nevroptaandroid:id/B11"
    #Notification

    #Popup-Allow Noti
    id_popup_allow= "com.pta.nevro.nevroptaandroid:string/B82"

    #Start A Scan
    id_scan_button = "com.pta.nevro.nevroptaandroid:id/scan_button"

    #bLE Conected Screen
    id_Continue_button = "com.pta.nevro.nevroptaandroid:id/B9"

    #Confirm Pain Areas
    id_Confirmbutton = "com.pta.nevro.nevroptaandroid:id/B132"
    id_lets_begin = "com.pta.nevro.nevroptaandroid:id/B24"

    # Start Assessment
    id_assessment = "com.pta.nevro.nevroptaandroid:id/homeAssessmentButton"

    #Painrelief
    id_title_assessment ="com.pta.nevro.nevroptaandroid:id/title_text"
    id_exit_btn = "com.pta.nevro.nevroptaandroid:id/exit_link"
    id_card_heading = "com.pta.nevro.nevroptaandroid:id/card_heading"
    id_paincontrol_score = "com.pta.nevro.nevroptaandroid:id/overall_pain_score_control"





