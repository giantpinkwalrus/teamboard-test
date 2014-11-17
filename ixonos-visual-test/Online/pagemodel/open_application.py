# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Open_application(CommonUtils):
    # Pagemodel timestamp: 20141110092516
    # Pagemodel url: http://80.242.17.165/
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1680, 1050)
    # Pagemodel type: root
    # Pagemodel template: False
    # Links found: 0
    
    def open_application_url(self, url):
        self.open_url(url)