# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from webframework.extension.util.http_utils import HTTPUtils
from time import sleep
from pagemodel.delete_ticket import Delete_ticket
from pagemodel.board import Board
from pagemodel.workspace import Workspace
from pagemodel.open_application import Open_application
from pagemodel.login import Login
from pagemodel.create_ticket import Create_ticket


class Perf_failed_test(BaseTest):
    common_utils = CommonUtils()    
    delete_ticket = Delete_ticket()
    board = Board()
    workspace = Workspace()
    open_application = Open_application()
    login = Login()
    create_ticket = Create_ticket()
    parameters = get_all_parameters()
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    
    # 1. -> 1.1. **** 1.1. -> 1.1.2. **** 1.1.2. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2. **** 1.1.2. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4.3. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4.3. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 
    def test_case_1_to_1_1_2_4_1(self):
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
        self.board.enter_workspace()
        # Output
        self.workspace.verify_view()
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Precondition
        self.board.select_ticket(self.parameters[u'ticket'])
        # Input
        self.board.delete_ticket()
        # Output
        self.delete_ticket.verify_view()
        # Precondition
        self.board.select_ticket(self.parameters[u'ticket'])
        # Input
        self.board.delete_ticket()
        # Output
        self.delete_ticket.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Precondition
        self.board.select_ticket(self.parameters[u'ticket'])
        # Input
        self.board.delete_ticket()
        # Output
        self.delete_ticket.verify_view()
        # Input
        self.delete_ticket.cancel()
        # Output
        self.board.verify_view()
        # Precondition
        self.board.select_ticket(self.parameters[u'ticket'])
        # Input
        self.board.delete_ticket()
        # Output
        self.delete_ticket.verify_view()
        # Input
        self.delete_ticket.delete()
        # Output
        self.board.verify_view()
        # Input
        self.board.move_ticket(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.move_ticket(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.move_ticket(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
