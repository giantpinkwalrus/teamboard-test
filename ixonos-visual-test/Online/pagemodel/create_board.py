# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Create_board(CommonUtils):
    # Pagemodel timestamp: 20141110115840
    # Pagemodel url: http://80.242.17.165/main/workspace
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    HEADING_INPUT = (By.ID, u'headingInput') # x: 396 y: 127 width: 555 height: 34
    CANCEL_BUTTON = (By.CLASS_NAME, u'btn-default') # x: 263 y: 225 width: 337 height: 46
    CREATE_BUTTON = (By.CLASS_NAME, u'btn-primary') # x: 630 y: 225 width: 337 height: 46

    # Dynamic objects:
    TITLE = (By.XPATH, u'//BODY/DIV[3]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]')     # x: 263 y: 47 width: 703 height: 31 # Dynamic object

    def cancel(self, parameters=None):
        self.click(self.CANCEL_BUTTON)

    def create(self, parameters=None):
        self.type(self.HEADING_INPUT, parameters[u'new_name'])
        self.click(self.CREATE_BUTTON)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.TITLE, u'Create a new board')
