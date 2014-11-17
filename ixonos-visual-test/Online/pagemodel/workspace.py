# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep
import random

class Workspace(CommonUtils):
    # Pagemodel timestamp: 20141110100951
    # Pagemodel url: http://80.242.17.165/main/workspace
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: normal
    # Pagemodel template: False
    # Links found: 0
    CREATE_BUTTON = (By.CLASS_NAME, u'btn-add') # x: 1030 y: 6 width: 179 height: 46
    TEAMBOARD_TEXT = (By.CLASS_NAME, u'logo-text') # x: 64 y: 14 width: 132 height: 38
    WORKSPACE_CONTAINER_FLUID_ROW = (By.CSS_SELECTOR, u'#workspace>div.container-fluid>div.row') # x: 232 y: 64 width: 1015 height: 48
    WORKSPACE_BUTTON = (By.XPATH, u'id(\'sidebar-container\')/DIV[1]/DIV[3]/DIV[1]/NAV[1]/UL[1]/A[1]/LI[1]/SPAN[1]') # x: 66 y: 83 width: 56 height: 22
    SEARCH_BUTTON = (By.CLASS_NAME, u'fa-search') # x: 1207 y: 83 width: 18 height: 14
    MINIMIZE_BUTTON = (By.CLASS_NAME, u'fa-chevron-left') # x: 207 y: 85 width: 19 height: 26
    LOG_OUT_BUTTON = (By.XPATH, u'id(\'sidebar-container\')/DIV[1]/DIV[3]/DIV[1]/NAV[1]/UL[1]/A[2]/LI[1]/SPAN[1]') # x: 66 y: 132 width: 58 height: 22
    USERVOICE_BUTTON = (By.CSS_SELECTOR, u'#feedback-uservoice-0>i.fa.fa-question-circle.fa-fw') # x: 96 y: 625 width: 41 height: 32

    # Dynamic objects:
    MAXIMIZE_BUTTON = (By.CLASS_NAME, u'fa-chevron-right')     # x: 49 y: 85 width: 19 height: 26 # Dynamic object
    DELETE_BUTTON = (By.CLASS_NAME, u'fa-trash-o')     # x: 875 y: 20 width: 32 height: 25 # Dynamic object
    EDIT_BUTTON = (By.CLASS_NAME, u'fa-edit')     # x: 932 y: 20 width: 32 height: 25 # Dynamic object

    def log_out(self, parameters=None):
        self.click(self.LOG_OUT_BUTTON)

    def create_board(self, parameters=None):
        self.click(self.CREATE_BUTTON)

    def delete_board(self, parameters=None):
        self.click(self.DELETE_BUTTON)

    def edit_board(self, parameters=None):
        board_name = parameters[u'new_name']
        newBoards = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + board_name + "')]]"))
        board_name = parameters[u'edited_name']
        editedBoards = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + board_name + "')]]"))
        elements = newBoards + editedBoards
        if elements:
            element = random.choice(elements)
            self.click(element)

    def enter_board(self, parameters=None):
        board_name = parameters[u'new_name']
        newBoards = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + board_name + "')]]/../div[1]/a/div/div"))
        board_name = parameters[u'edited_name']
        editedBoards = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + board_name + "')]]/../div[1]/a/div/div"))
        elements = newBoards + editedBoards
        print elements
        if elements:
            element = random.choice(elements)
            self.click(element)

    def select_board(self, parameters=None):
        board_name = parameters[u'new_name']
        newBoards = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + board_name + "')]]/../div[1]/div[2]"))
        board_name = parameters[u'edited_name']
        editedBoards = self.find_elements((By.XPATH, "//*[text()[contains(.,'" + board_name + "')]]/../div[1]/div[2]"))
        elements = newBoards + editedBoards
        if elements:
            element = random.choice(elements)
            self.click(element)

    def verify_view(self, parameters=None):
        sleep(1)
        self.wait_for_browser_loaded()
        self.verify_text(self.TEAMBOARD_TEXT, u'Teamboard')
        self.verify_text(self.CREATE_BUTTON, u'Create board')
