from selenium.webdriver import ActionChains


class WebFunctions:



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
            action.self_click(on_element=ele)
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

    def scroll_element(self, source_ele, target_ele):

        try:
            source_element = self.driver.find_element(source_ele)
            target_element = self.driver.find_element(target_ele)
            action = ActionChains(self.driver)
            action.drag_and_drop(source_element, target_element)
            action.perform()
        except:
            raise Exception

    def force_Click(self, locatorType):
        ele = None
        try:
            ele = self.driver.find_element(locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(ele).click().perform()
        except:
            raise Exception