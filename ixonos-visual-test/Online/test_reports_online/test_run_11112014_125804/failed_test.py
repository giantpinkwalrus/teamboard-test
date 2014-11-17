# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from webframework.extension.util.http_utils import HTTPUtils
from time import sleep
from pagemodel.board import Board
from pagemodel.workspace import Workspace
from pagemodel.open_application import Open_application
from pagemodel.edit_ticket import Edit_ticket
from pagemodel.login import Login
from pagemodel.guest_login import Guest_login


class Perf_failed_test(BaseTest):
    common_utils = CommonUtils()    
    board = Board()
    workspace = Workspace()
    open_application = Open_application()
    edit_ticket = Edit_ticket()
    login = Login()
    guest_login = Guest_login()
    parameters = get_all_parameters()
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    
    # 1. -> 1.2. **** 1. -> 1.2. **** 1. -> 1.2. **** 1. -> 1.1. **** 1.1. -> 1.1.2. **** 1.1.2. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.2. **** 
    def test_case_1_to_1_1_2_4_2(self):
        # Input
        self.open_application.open_application_url(u'www.google.com')
        # Output
        self.guest_login.verify_view()
        # Input
        self.open_application.open_application_url(u'www.google.com')
        # Output
        self.guest_login.verify_view()
        # Input
        self.open_application.open_application_url(u'www.google.com')
        # Output
        self.guest_login.verify_view()
        # Input
        self.open_application.open_application_url(self.parameters[u'url'][u'login'])
        # Output
        self.login.verify_view()
        # Input
        self.login.sign_in(self.parameters[u'user'])
        # Output
        self.workspace.verify_view()
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.board.move_ticket(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.edit_ticket(self.parameters[u'ticket'])
        # Output
        self.edit_ticket.verify_view()
