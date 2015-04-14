# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Remove_board(CommonUtils):
    # Pagemodel timestamp: 20150410091135
    # Pagemodel url: http://lankku.n4sjamk.org/boards
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    CLASS_DIALOG_HEADER = (By.CLASS_NAME, u'dialog-header') # x: 432 y: 64 width: 400 height: 54
    CLASS_BTN_NEUTRAL = (By.CLASS_NAME, u'btn-neutral') # x: 448 y: 194 width: 176 height: 36
    CLASS_BTN_DANGER = (By.CLASS_NAME, u'btn-danger') # x: 640 y: 194 width: 176 height: 36

    def verify(self, parameters=None): # Type: verification
        self.wait_for_present(self.CLASS_BTN_DANGER)

    def remove(self, parameters=None): # Type: input
        self.click(self.CLASS_BTN_DANGER)

    def cancel(self, parameters=None): # Type: input
        self.click(self.CLASS_BTN_NEUTRAL)
