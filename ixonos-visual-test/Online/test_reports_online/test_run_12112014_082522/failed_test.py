# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from webframework.extension.util.http_utils import HTTPUtils
from time import sleep
from pagemodel.delete_ticket import Delete_ticket
from pagemodel.delete_board import Delete_board
from pagemodel.board import Board
from pagemodel.workspace import Workspace
from pagemodel.open_application import Open_application
from pagemodel.edit_ticket import Edit_ticket
from pagemodel.create_board import Create_board
from pagemodel.login import Login
from pagemodel.create_ticket import Create_ticket
from pagemodel.edit_board import Edit_board


class Perf_failed_test(BaseTest):
    common_utils = CommonUtils()    
    delete_ticket = Delete_ticket()
    delete_board = Delete_board()
    board = Board()
    workspace = Workspace()
    open_application = Open_application()
    edit_ticket = Edit_ticket()
    create_board = Create_board()
    login = Login()
    create_ticket = Create_ticket()
    edit_board = Edit_board()
    parameters = get_all_parameters()
    
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    
    # 1. -> 1.1. **** 1.1. -> 1.1.2. **** 1.1.2. -> 1.1.2.3. **** 1.1.2.3. -> 1.1.2.__1 **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.3. **** 1.1.2. -> 1.1.2.3. **** 1.1.2. -> 1.1.2.3. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.2. **** 1.1.2. -> 1.1.2.4. **** 1.1.2. -> 1.1.2.3. **** 1.1.2. -> 1.1.2.1. **** 1.1.2.1. -> 1.1.2.__1 **** 1.1.2. -> 1.1.2.2. **** 1.1.2.2. -> 1.1.2.__1 **** 1.1.2. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.2. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4.3. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.2. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4.3. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.2. **** 1.1.2.4.2. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2. **** 1.1.2. -> 1.1.2.2. **** 1.1.2.2. -> 1.1.2.__1 **** 1.1.2. -> 1.1.2.1. **** 1.1.2.1. -> 1.1.2.__1 **** 1.1.2. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 1.1.2.4.1. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.2. **** 1.1.2.4.2. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4.3. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.2. **** 1.1.2.4.2. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4.3. **** 1.1.2.4.3. -> 1.1.2.4.__1 **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4. **** 1.1.2.4. -> 1.1.2.4.1. **** 
    def test_case_1_to_1_1_2_4_1(self):
        # Input
        self.open_application.open_application_url(self.parameters[u'url'][u'login'])
        # Output
        self.login.verify_view()
        # Input
        self.login.sign_in(self.parameters[u'user'])
        # Output
        self.workspace.verify_view()
        # Precondition
        self.workspace.select_board(self.parameters[u'board'])
        # Input
        self.workspace.delete_board()
        # Output
        self.delete_board.verify_view()
        # Input
        self.delete_board.delete()
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
        # Precondition
        self.workspace.select_board(self.parameters[u'board'])
        # Input
        self.workspace.delete_board()
        # Output
        self.delete_board.verify_view()
        # Precondition
        self.workspace.select_board(self.parameters[u'board'])
        # Input
        self.workspace.delete_board()
        # Output
        self.delete_board.verify_view()
        # Precondition
        self.workspace.select_board(self.parameters[u'board'])
        # Input
        self.workspace.delete_board()
        # Output
        self.delete_board.verify_view()
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
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Precondition
        self.workspace.select_board(self.parameters[u'board'])
        # Input
        self.workspace.delete_board()
        # Output
        self.delete_board.verify_view()
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
        # Input
        self.workspace.enter_board(self.parameters[u'board'])
        # Output
        self.board.verify_view()
        # Input
        self.board.edit_ticket(self.parameters[u'ticket'])
        # Output
        self.edit_ticket.verify_view()
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
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
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
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
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
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.move_ticket(self.parameters[u'ticket'])
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
        self.board.edit_ticket(self.parameters[u'ticket'])
        # Output
        self.edit_ticket.verify_view()
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
        self.delete_ticket.delete()
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.cancel()
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
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
        # Input
        self.edit_ticket.edit(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.enter_workspace()
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
        # Input
        self.workspace.create_board()
        # Output
        self.create_board.verify_view()
        # Input
        self.create_board.create(self.parameters[u'board'])
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
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
        # Input
        self.create_ticket.create(self.parameters[u'ticket'])
        # Output
        self.board.verify_view()
        # Input
        self.board.edit_ticket(self.parameters[u'ticket'])
        # Output
        self.edit_ticket.verify_view()
        # Input
        self.edit_ticket.edit(self.parameters[u'ticket'])
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
        # Input
        self.board.edit_ticket(self.parameters[u'ticket'])
        # Output
        self.edit_ticket.verify_view()
        # Input
        self.edit_ticket.edit(self.parameters[u'ticket'])
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
        self.board.create_ticket()
        # Output
        self.create_ticket.verify_view()
