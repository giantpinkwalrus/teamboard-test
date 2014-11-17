# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Delete_ticket(CommonUtils):
    # Pagemodel timestamp: 20141110132701
    # Pagemodel url: http://80.242.17.165/main/board/54608e754a8ace3150a4d7cb
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    TITLE = (By.CSS_SELECTOR, u'div.ng-binding.ng-scope') # x: 557 y: 47 width: 548 height: 31
    CANCEL_BUTTON = (By.CLASS_NAME, u'btn-default') # x: 557 y: 203 width: 259 height: 46
    DELETE_BUTTON = (By.CLASS_NAME, u'btn-danger') # x: 846 y: 203 width: 259 height: 46

    def delete(self, parameters=None):
        self.click(self.DELETE_BUTTON)

    def cancel(self, parameters=None):
        self.click(self.CANCEL_BUTTON)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.DELETE_BUTTON, u'Delete')
