from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class objectRepos:
    #network_security = (AppiumBy.XPATH, "//*[@text='Network & internet']")
    network_security = "//*[@text='Network & internet']"
    """
    #Login Feature
    
    """
    id_Continue_anyway = "android:id/button1"
    id_Skip_button = "com.pta.nevro.nevroptaandroid:id/skipBtn"
    id_Accept_EULA = "com.pta.nevro.nevroptaandroid:id/B1"
    id_log_in_link = "com.pta.nevro.nevroptaandroid:id/B65"


    id_HFX_logo = "com.pta.nevro.nevroptaandroid:id/nevro_logo"
    id_HFX_Find_account = "com.pta.nevro.nevroptaandroid:id/nevro_logo"
    Xpath_HFX_Email = "//android.widget.EditText[@content-desc='F3']"
    xpath_HFX_password = "//android.widget.EditText[@content-desc='F7']"
    id_HFX_need_help = "com.pta.nevro.nevroptaandroid:id/B66"
    id_login_button = "com.pta.nevro.nevroptaandroid:id/B64"