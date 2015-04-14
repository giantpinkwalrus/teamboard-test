# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Login(CommonUtils):
    # Pagemodel timestamp: 20150410085553
    # Pagemodel url: http://lankku.n4sjamk.org/login
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    UNKNOWN = (By.CSS_SELECTOR, u'img') # x: 539 y: 112 width: 32 height: 32
    CONTRIBOARD = (By.CSS_SELECTOR, u'h1') # x: 581 y: 112 width: 155 height: 32
    UNKNOWN_0 = (By.CSS_SELECTOR, u'label') # x: 540 y: 177 width: 28 height: 13
    NAME_EMAIL = (By.CSS_SELECTOR, u'input[name="email"]') # x: 540 y: 190 width: 200 height: 36
    NAME_PASSWORD = (By.CSS_SELECTOR, u'input[name="password"]') # x: 540 y: 248 width: 200 height: 36
    CLASS_BTN_PRIMARY = (By.CLASS_NAME, u'btn-primary') # x: 540 y: 300 width: 200 height: 36
    CLASS_HELP = (By.CLASS_NAME, u'help') # x: 540 y: 352 width: 200 height: 9
    NOT_REGISTERED = (By.CSS_SELECTOR, u'p') # x: 540 y: 373 width: 200 height: 14
    CLASS_BTN_SECONDARY = (By.CLASS_NAME, u'btn-secondary') # x: 540 y: 391 width: 200 height: 36

    def goto_register(self, parameters=None): # Type: input
        self.click(self.CLASS_BTN_SECONDARY)

    def log_in(self, parameters=None): # Type: input
        print "log in"
        self.type(self.NAME_EMAIL, parameters[u'email'])
        self.type(self.NAME_PASSWORD, parameters[u'password'])
        self.click(self.CLASS_BTN_PRIMARY)

    def verify(self, parameters=None): # Type: verification
        self.wait_for_present(self.CLASS_BTN_PRIMARY)
