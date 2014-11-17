# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from webframework.extension.util.http_utils import HTTPUtils
from time import sleep
from pagemodel.login import Login
from pagemodel.workspace import Workspace
from pagemodel.open_application import Open_application


class Perf_failed_test(BaseTest):
    common_utils = CommonUtils()    
    login = Login()
    workspace = Workspace()
    open_application = Open_application()
    parameters = get_all_parameters()
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    
    # 1. -> 1.1. **** 1.1. -> 1.1.2. **** 
    def test_case_1_to_1_1_2(self):
        # Input
        self.open_application.open_application_url(self.parameters[u'url'][u'login'])
        # Output
        self.login.verify_view()
        # Input
        self.login.sign_in(self.parameters[u'user'])
        # Output
        self.workspace.verify_view()
