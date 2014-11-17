# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Create_ticket(CommonUtils):
    # Pagemodel timestamp: 20141110124435
    # Pagemodel url: http://80.242.17.165/main/board/54608e754a8ace3150a4d7cb
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    BLUE_BUTTON = (By.CLASS_NAME, u'blue') # x: 247 y: 71 width: 184 height: 40
    PURPLE_BUTTON = (By.CLASS_NAME, u'purple') # x: 431 y: 71 width: 184 height: 40
    YELLOW_BUTTON = (By.CLASS_NAME, u'yellow') # x: 615 y: 71 width: 184 height: 40
    RED_BUTTON = (By.CLASS_NAME, u'red') # x: 798 y: 71 width: 184 height: 40
    HEADING_INPUT = (By.ID, u'headingInput') # x: 263 y: 127 width: 703 height: 46
    CONTENT_INPUT = (By.XPATH, u'//*[contains(@id,\'taTextElement\')]') # x: 268 y: 175 width: 693 height: 168
    CANCEL_BUTTON = (By.XPATH, u'//BODY/DIV[3]/DIV[1]/DIV[1]/FORM[1]/DIV[3]/DIV[1]/DIV[1]/DIV[1]/BUTTON[1]') # x: 263 y: 375 width: 337 height: 46
    CREATE_BUTTON = (By.CLASS_NAME, u'btn-primary') # x: 630 y: 375 width: 337 height: 46

    def cancel(self, parameters=None):
        self.click(self.CANCEL_BUTTON)

    def create(self, parameters=None):
        color = random.randint(0, 3)
        if color == 0:
            self.click(self.BLUE_BUTTON)
        elif color == 1:
            self.click(self.PURPLE_BUTTON)
        elif color == 2:
            self.click(self.YELLOW_BUTTON)
        else:
            self.click(self.RED_BUTTON)
        self.type(self.HEADING_INPUT, parameters[u'new_name'])
        self.type(self.CONTENT_INPUT, parameters[u'new_content'])
        self.click(self.CREATE_BUTTON)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.CREATE_BUTTON, u'Create')
