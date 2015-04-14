# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Edit_board(CommonUtils):
    # Pagemodel timestamp: 20150410091056
    # Pagemodel url: http://lankku.n4sjamk.org/boards
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    CLASS_DIALOG_HEADER = (By.CLASS_NAME, u'dialog-header') # x: 432 y: 64 width: 400 height: 54
    NAME_BOARD = (By.CSS_SELECTOR, u'input[name="board-name"]') # x: 448 y: 140 width: 368 height: 36
    NAME_BOARD_SHARE = (By.CSS_SELECTOR, u'input[name="board-share"]') # x: 448 y: 198 width: 176 height: 36
    CLASS_BTN_SECONDARY = (By.CLASS_NAME, u'btn-secondary') # x: 640 y: 198 width: 176 height: 36
    CLASS_BTN_PRIMARY = (By.CLASS_NAME, u'btn-primary') # x: 448 y: 460 width: 368 height: 36

    def verify(self, parameters=None): # Type: verification
        self.wait_for_present(self.CLASS_BTN_SECONDARY)

    def change_name(self, parameters=None): # Type: input
        name = random.randint(0, 2)
        if name == 0:
            self.type(self.NAME_BOARD, parameters[u'name1'])
        elif name == 1:
            self.type(self.NAME_BOARD, parameters[u'name2'])
        else:
            self.type(self.NAME_BOARD, parameters[u'name3'])
        self.click(self.CLASS_BTN_PRIMARY)
