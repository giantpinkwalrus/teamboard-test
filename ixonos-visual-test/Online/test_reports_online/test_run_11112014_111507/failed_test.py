# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from webframework.extension.util.http_utils import HTTPUtils
from time import sleep
from pagemodel.board import Board
from pagemodel.workspace import Workspace
from pagemodel.open_application import Open_application
from pagemodel.create_board import Create_board
from pagemodel.login import Login
from pagemodel.guest_login import Guest_login
from pagemodel.edit_board import Edit_board


class Perf_failed_test(BaseTest):
    common_utils = CommonUtils()    
    board = Board()
    workspace = Workspace()
    open_application = Open_application()
    create_board = Create_board()
    login = Login()
    guest_login = Guest_login()
    edit_board = Edit_board()
    parameters = get_all_parameters()
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    
    # 1. -> 1.2. **** 1. -> 1.2. **** 1. -> 1.1. **** 1.1. -> 1.1.2. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.2. **** 1.1.2. -> 1.1.2.2. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.1. **** 1.1.2.1. -> 1.1.2.__1 **** 1.1.2. -> 1.1.2.2. **** 1.1.2.2. -> 1.1.2.__1 **** 
    def test_case_1_to_1_1_2_2_to_1_1_2(self):
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
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.workspace.edit_board(self.parameters[u'board'])
        # Output
        self.edit_board.verify_view()
        # Input
        self.workspace.edit_board(self.parameters[u'board'])
        # Output
        self.edit_board.verify_view()
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.workspace.create_board()
        # Output
        self.create_board.verify_view()
        # Input
        self.create_board.create(self.parameters[u'board'])
        # Output
        self.workspace.verify_view()
        # Input
        self.workspace.edit_board(self.parameters[u'board'])
        # Output
        self.edit_board.verify_view()
        # Input
        self.edit_board.edit(self.parameters[u'board'])
        # Output
        self.workspace.verify_view()
