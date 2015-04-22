# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Edit_ticket(CommonUtils):
    # Pagemodel timestamp: 20150410091912
    # Pagemodel url: http://lankku.n4sjamk.org/boards/552769027aced20e001e0523
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: dynamic
    # Pagemodel template: False
    # Links found: 0
    RED = (By.XPATH, u'//BODY/DIV[2]/DIV[1]/FORM[1]/SECTION[1]/DIV[1]/DIV[2]/DIV[1]') # x: 423 y: 88 width: 100 height: 24
    BLUE = (By.XPATH, u'//BODY/DIV[2]/DIV[1]/FORM[1]/SECTION[1]/DIV[1]/DIV[2]/DIV[2]') # x: 523 y: 88 width: 100 height: 24
    VIOLET = (By.XPATH, u'//BODY/DIV[2]/DIV[1]/FORM[1]/SECTION[1]/DIV[1]/DIV[2]/DIV[3]') # x: 623 y: 88 width: 100 height: 24
    YELLOW = (By.XPATH, u'//BODY/DIV[2]/DIV[1]/FORM[1]/SECTION[1]/DIV[1]/DIV[2]/DIV[4]') # x: 723 y: 88 width: 100 height: 24
    CONTENT = (By.CSS_SELECTOR, u'textarea') # x: 439 y: 128 width: 368 height: 128
    DELETE = (By.CLASS_NAME, u'btn-danger') # x: 439 y: 272 width: 176 height: 36
    DONE = (By.CLASS_NAME, u'btn-primary') # x: 631 y: 272 width: 176 height: 36

    def verify(self, parameters=None): # Type: verification
        self.wait_for_present(self.DELETE)

    def delete(self, parameters=None): # Type: input
        self.click(self.DELETE)

    def change_content(self, parameters=None): # Type: input
        color = random.randint(0, 3)
        if color == 0:
            self.click(self.RED)
        elif color == 1:
            self.click(self.BLUE)
        elif color == 2:
            self.click(self.VIOLET)
        else:
            self.click(self.YELLOW)
        content = random.randint(0, 2)
        if content == 0:
            self.type(self.CONTENT, parameters[u'content1'])
        elif content == 1:
            self.type(self.CONTENT, parameters[u'content2'])
        else:
            self.type(self.CONTENT, parameters[u'content3'])
        self.click(self.DONE)
