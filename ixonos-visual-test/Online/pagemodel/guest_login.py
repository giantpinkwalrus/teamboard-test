# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Guest_login(CommonUtils):
    # Pagemodel timestamp: 20141110124854
    # Pagemodel url: http://80.242.17.165/board/54608e754a8ace3150a4d7cb/access/7572af0a
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    LOGIN_TEXT = (By.CSS_SELECTOR, u'h2.ng-binding') # x: 695 y: 99 width: 290 height: 33
    USERNAME_INPUT = (By.CSS_SELECTOR, u'input[name="username"].form-control.ng-pristine.ng-invalid.ng-invalid-required') # x: 695 y: 155 width: 290 height: 34
    SIGN_IN_BUTTON = (By.CLASS_NAME, u'btn-login') # x: 695 y: 213 width: 290 height: 64

    def login(self, parameters=None):
        self.type(self.USERNAME_INPUT, parameters[u'username'])
        self.click(self.SIGN_IN_BUTTON)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.LOGIN_TEXT, u'Login')
