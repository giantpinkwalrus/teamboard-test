# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from webframework.extension.util.http_utils import HTTPUtils
from time import sleep
from pagemodel.remove_board import Remove_board
from pagemodel.board import Board
from pagemodel.workspace import Workspace
from pagemodel.open_application import Open_application
from pagemodel.edit_ticket import Edit_ticket
from pagemodel.login import Login
from pagemodel.edit_board import Edit_board


class Perf_failed_test(BaseTest):
    common_utils = CommonUtils()    
    remove_board = Remove_board()
    board = Board()
    workspace = Workspace()
    open_application = Open_application()
    edit_ticket = Edit_ticket()
    login = Login()
    edit_board = Edit_board()
    parameters = get_all_parameters()
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    
    # 1. -> 1.1. **** 1.1. -> 1.1.1. **** 1.1.1. -> 1.1.1.2. **** 1.1.1. -> 1.1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1. -> 1.1.1.3. **** 1.1.1. -> 1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.2. **** 1.1.1.1.2. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.2. **** 1.1.1.1.2. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.2. **** 1.1.1.1.2. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1. -> 1.1.1. **** 1.1.1. -> 1.1.1.3. **** 1.1.1.3. -> 1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1. -> 1.1.1.2. **** 1.1.1. -> 1.1.1.2. **** 1.1.1. -> 1.1.1.2. **** 1.1.1. -> 1.1.1.1. **** 1.1.1. -> 1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.2. **** 1.1.1.1.2. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.2. **** 1.1.1.1.2. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1. **** 1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 1.1.1.1. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.2. **** 1.1.1.1.2. -> 1.1.1.1. **** 1.1.1.1. -> 1.1.1.1.1. **** 
    def test_case_1_to_1_1_1_1_1(self):
        # Input
        self.open_application.open_application_url(self.parameters[u'url'][u'url'])
        # Output
        self.login.verify()
        # Input
        self.login.log_in(self.parameters[u'user'])
        # Output
        self.workspace.verify()
        # Input
        self.workspace.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.workspace.remove_board()
        # Output
        self.remove_board.verify()
        # Input
        self.workspace.create_board()
        # Output
        self.workspace.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.edit_ticket.delete()
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.edit_ticket.delete()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.edit_board.change_name(self.parameters[u'board'])
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.back_to_workspace()
        # Output
        self.workspace.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.board.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.edit_board.change_name(self.parameters[u'board'])
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.edit_board.change_name(self.parameters[u'board'])
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.edit_ticket.delete()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.board.back_to_workspace()
        # Output
        self.workspace.verify()
        # Input
        self.workspace.remove_board()
        # Output
        self.remove_board.verify()
        # Input
        self.remove_board.remove()
        # Output
        self.workspace.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.workspace.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.workspace.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.workspace.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.workspace.create_board()
        # Output
        self.workspace.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.board.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.edit_board.change_name(self.parameters[u'board'])
        # Output
        self.board.verify()
        # Input
        self.board.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.edit_board.change_name(self.parameters[u'board'])
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.edit_ticket.change_content(self.parameters[u'ticket'])
        # Output
        self.board.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.back_to_workspace()
        # Output
        self.workspace.verify()
        # Input
        self.workspace.enter_board()
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
        # Input
        self.board.create_ticket()
        # Output
        self.board.verify()
        # Input
        self.board.edit_board()
        # Output
        self.edit_board.verify()
        # Input
        self.edit_board.change_name(self.parameters[u'board'])
        # Output
        self.board.verify()
        # Input
        self.board.edit_ticket()
        # Output
        self.edit_ticket.verify()
