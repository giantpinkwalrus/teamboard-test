# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Board(CommonUtils):
    # Pagemodel timestamp: 20150410085949
    # Pagemodel url: http://lankku.n4sjamk.org/boards/552766ae7aced20e001e0521
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    CLASS_LOGO = (By.CLASS_NAME, u'logo') # x: 16 y: 16 width: 32 height: 32
    CLASS_FA_USER = (By.CLASS_NAME, u'fa-user') # x: 1216 y: 17 width: 30 height: 30
    CLASS_TITLE = (By.CLASS_NAME, u'title') # x: 64 y: 19 width: 1135 height: 32
    CLASS_FA_ARROW_LEFT = (By.CLASS_NAME, u'fa-arrow-left') # x: 18 y: 82 width: 48 height: 48
    CLASS_FA_PENCIL = (By.CLASS_NAME, u'fa-pencil') # x: 18 y: 130 width: 48 height: 48
    CLASS_FA_MAGNET = (By.CLASS_NAME, u'fa-magnet') # x: 18 y: 178 width: 48 height: 48
    CLASS_FA_GLOBE = (By.CLASS_NAME, u'fa-globe') # x: 18 y: 226 width: 48 height: 48

    # Dynamic objects:
    LOGOUT = (By.XPATH, u'id(\'application\')/DIV[1]/NAV[1]/UL[1]/LI[4]/SPAN[2]')     # x: 1553 y: 223 width: 49 height: 28 # Dynamic object
    CLASS_TICKET = (By.CLASS_NAME, u'ticket')     # x: 485 y: 121 width: 194 height: 110 # Dynamic object
    CLASS_BOARD = (By.CLASS_NAME, u'board')     # x: 0 y: 64 width: 1920 height: 1080 # Dynamic object

    def verify(self, parameters=None): # Type: verification
        self.wait_for_present(self.CLASS_FA_ARROW_LEFT)

    def back_to_workspace(self, parameters=None):
        self.click(self.CLASS_FA_ARROW_LEFT)

    def edit_board(self, parameters=None): # Type: input
        self.click(self.CLASS_FA_PENCIL)

    def log_out(self, parameters=None):
        self.click(self.CLASS_FA_USER)
        self.wait_for_present(self.LOGOUT)
        self.click(self.LOGOUT)

    def create_ticket(self, parameters=None): # Type: input
        x = random.randint(-600, 600)
        y = random.randint(-300, 300)
        self.mouse_click_by_offset(self.CLASS_BOARD, x, y)
        time.sleep(0.05)
        self.mouse_click_by_offset(self.CLASS_BOARD, x, y)

    def edit_ticket(self, parameters=None): # Type: input
        elements = self.find_elements(self.CLASS_TICKET)
        if elements:
            element = random.choice(elements)
            self.click(element)
            time.sleep(0.05)
            self.click(element)
