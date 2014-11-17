# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Register(CommonUtils):
    # Pagemodel timestamp: 20141110094033
    # Pagemodel url: http://80.242.17.165/register
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    REGISTER_TEXT = (By.CSS_SELECTOR, u'h2.ng-binding') # x: 478 y: 99 width: 290 height: 33
    EMAIL_INPUT = (By.CLASS_NAME, u'ng-valid-email') # x: 478 y: 155 width: 290 height: 34
    PASSWORD_INPUT = (By.CSS_SELECTOR, u'input[name="password"].form-control.ng-pristine.ng-invalid.ng-invalid-required') # x: 478 y: 189 width: 290 height: 34
    PASSWORD_CONFIRM_INPUT = (By.ID, u'passwordConfirm') # x: 478 y: 260 width: 290 height: 34
    REGISTER_BUTTON = (By.CLASS_NAME, u'btn-register') # x: 478 y: 333 width: 290 height: 64
    SIGN_IN_BUTTON = (By.CLASS_NAME, u'btn-loginlink') # x: 478 y: 506 width: 290 height: 64

    def click_sign_in(self, parameters=None):
        self.click(self.SIGN_IN_BUTTON)

    def register(self, parameters=None):
        self.type(self.EMAIL_INPUT, parameters[u'email'])
        self.type(self.PASSWORD_INPUT, parameters[u'password'])
        self.type(self.PASSWORD_CONFIRM_INPUT, parameters[u'password'])
        self.click(self.REGISTER_BUTTON)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.REGISTER_TEXT, u'Register')
