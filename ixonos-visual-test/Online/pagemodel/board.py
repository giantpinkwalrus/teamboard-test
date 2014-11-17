# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Board(CommonUtils):
    # Pagemodel timestamp: 20141110120833
    # Pagemodel url: http://80.242.17.165/main/board/54608e754a8ace3150a4d7cb
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    CREATE_TICKET_BUTTON = (By.CLASS_NAME, u'btn-add') # x: 1366 y: 6 width: 266 height: 46
    TEAMBOARD_TEXT = (By.CLASS_NAME, u'logo-text') # x: 64 y: 14 width: 132 height: 38
    BACKGROUND_BUTTON = (By.CLASS_NAME, u'fa-picture-o') # x: 1201 y: 20 width: 32 height: 25
    SNAP_TO_GRID_BUTTON = (By.CLASS_NAME, u'fa-magnet') # x: 1258 y: 20 width: 32 height: 25
    WORKSPACE_BUTTON = (By.XPATH, u'id(\'sidebar-container\')/DIV[1]/DIV[3]/DIV[1]/NAV[1]/UL[1]/A[1]/LI[1]/SPAN[1]') # x: 66 y: 83 width: 56 height: 22
    MINIMAP_BUTTON = (By.CLASS_NAME, u'fa-arrows-alt') # x: 1641 y: 83 width: 18 height: 14
    MINIMIZE_BUTTON = (By.CLASS_NAME, u'fa-chevron-left') # x: 207 y: 85 width: 19 height: 26
    LOG_OUT_BUTTON = (By.XPATH, u'id(\'sidebar-container\')/DIV[1]/DIV[3]/DIV[1]/NAV[1]/UL[1]/A[2]/LI[1]/SPAN[1]') # x: 66 y: 132 width: 58 height: 22
    USERVOICE_BUTTON = (By.CSS_SELECTOR, u'#feedback-uservoice-2>i.fa.fa-question-circle.fa-fw') # x: 96 y: 903 width: 41 height: 32
    EXPAND_BUTTON = (By.CLASS_NAME, u'fa-expand') # x: 1641 y: 918 width: 18 height: 14

    # Dynamic objects:
    DELETE_BUTTON = (By.CLASS_NAME, u'fa-trash-o')     # x: 1201 y: 20 width: 32 height: 25 # Dynamic object
    EDIT_BUTTON = (By.CLASS_NAME, u'fa-edit')     # x: 1258 y: 20 width: 32 height: 25 # Dynamic object

    MAXIMIZE_BUTTON = (By.CLASS_NAME, u'fa-chevron-right')     # x: 49 y: 85 width: 19 height: 26 # Dynamic object

    def log_out(self, parameters=None):
        self.click(self.LOG_OUT_BUTTON)

    def enter_workspace(self, parameters=None):
        self.click(self.WORKSPACE_BUTTON)

    def delete_ticket(self, parameters=None):
        self.click(self.DELETE_BUTTON)

    def create_ticket(self, parameters=None):
        self.click(self.CREATE_TICKET_BUTTON)

    def select_ticket(self, parameters=None):
        ticket_name = parameters[u'new_name']
        newTickets = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + ticket_name + "')]]/../div[1]"))
        ticket_name = parameters[u'edited_name']
        editedTickets = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + ticket_name + "')]]/../div[1]"))
        elements = newTickets + editedTickets
        if elements:
            element = random.choice(elements)
            self.click(element)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.TEAMBOARD_TEXT, u'Teamboard')
        self.verify_text(self.CREATE_TICKET_BUTTON, u'Create ticket')

    def move_ticket(self, parameters=None):
        ticket_name = parameters[u'new_name']
        newTickets = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + ticket_name + "')]]"))
        ticket_name = parameters[u'edited_name']
        editedTickets = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + ticket_name + "')]]"))
        elements = newTickets + editedTickets
        if elements:
            element = random.choice(elements)
            randX = random.randint(30, 80)
            randY = random.randint(30, 80)
            driver = get_driver()
            ActionChains(driver).drag_and_drop_by_offset(element, randX, randY).perform()
            sleep(2)

    def edit_ticket(self, parameters=None):
        ticket_name = parameters[u'new_name']
        newTickets = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + ticket_name + "')]]"))
        ticket_name = parameters[u'edited_name']
        editedTickets = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + ticket_name + "')]]"))
        elements = newTickets + editedTickets
        if elements:
            element = random.choice(elements)
            self.click(element)
