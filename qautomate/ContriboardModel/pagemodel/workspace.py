# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Workspace(CommonUtils):
    # Pagemodel timestamp: 20150410085839
    # Pagemodel url: http://lankku.n4sjamk.org/boards
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    CLASS_LOGO = (By.CLASS_NAME, u'logo') # x: 16 y: 16 width: 32 height: 32
    CLASS_FA_USER = (By.CLASS_NAME, u'fa-user') # x: 1233 y: 17 width: 30 height: 30
    CLASS_TITLE = (By.CLASS_NAME, u'title') # x: 64 y: 19 width: 1152 height: 32
    CLASS_FA_PLUS = (By.CLASS_NAME, u'fa-plus') # x: 531 y: 160 width: 202 height: 182

    # Dynamic objects:
    BOARD = (By.CLASS_NAME, u'minimap')     # x: 652 y: 164 width: 194 height: 110 # Dynamic object
    EDIT = (By.CLASS_NAME, u'fa-pencil')     # x: 784 y: 316 width: 32 height: 32 # Dynamic object
    DELETE = (By.CLASS_NAME, u'fa-trash')     # x: 824 y: 316 width: 32 height: 32 # Dynamic object
    LOGOUT = (By.XPATH, u'id(\'application\')/DIV[1]/NAV[1]/UL[1]/LI[4]/SPAN[2]')     # x: 1153 y: 223 width: 49 height: 28 # Dynamic object

    def verify(self, parameters=None): # Type: verification
        self.wait_for_present(self.CLASS_FA_PLUS)

    def create_board(self, parameters=None):
        self.click(self.CLASS_FA_PLUS)

    def enter_board(self, parameters=None): # Type: input
        elements = self.find_elements(self.BOARD)
        if elements:
            element = random.choice(elements)
            self.click(element)

    def edit_board(self, parameters=None): # Type: input
        elements = self.find_elements(self.EDIT)
        if elements:
            element = random.choice(elements)
            self.click(element)

    def remove_board(self, parameters=None): # Type: input
        elements = self.find_elements(self.DELETE)
        if elements:
            element = random.choice(elements)
            self.click(element)

    def log_out(self, parameters=None): # Type: input
        self.click(self.CLASS_FA_USER)
        self.wait_for_present(self.LOGOUT)
        self.click(self.LOGOUT)
