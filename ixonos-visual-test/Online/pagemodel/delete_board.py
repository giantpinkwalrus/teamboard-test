# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Delete_board(CommonUtils):
    # Pagemodel timestamp: 20141110120217
    # Pagemodel url: http://80.242.17.165/main/workspace
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    CANCEL_BUTTON = (By.CLASS_NAME, u'btn-default') # x: 416 y: 203 width: 183 height: 46
    DELETE_BUTTON = (By.CLASS_NAME, u'btn-danger') # x: 629 y: 203 width: 183 height: 46

    # Dynamic objects:
    TITLE = (By.XPATH, u'//BODY/DIV[3]/DIV[1]/DIV[1]/FORM[1]/DIV[1]/DIV[1]/DIV[1]')     # x: 416 y: 47 width: 396 height: 31 # Dynamic object

    def delete(self, parameters=None):
        self.click(self.DELETE_BUTTON)

    def cancel(self, parameters=None):
        self.click(self.CANCEL_BUTTON)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.TITLE, u'Delete board')
