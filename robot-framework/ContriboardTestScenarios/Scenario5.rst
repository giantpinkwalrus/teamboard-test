.. default-role:: code

============
Scenario5
============

Browser: Firefox
Operation System: Ubuntu 14.04

ErrorRobot404
Occupation: Ultimate testing robot
Age: Unknown


Full product test.


Primary Actor: ErrorRobot404

Other Actors: NONE

Roles: Testing robot


.. contents:: Table of contents
   :local:
   :depth: 2


=================
Scenario 5 Tests
=================


.. code:: robotframework

	*** Settings ***
	Resource 		ScenarioTests/resource.txt
	
	*** Variables ***
	${ValidUser}      testrobot@test.com
	${ValidPassword}    testrobot


Primary function: Test Contriboard functionality

Test invalid login options


.. code:: robotframework

    	*** Test Cases ***
    	
    	Open Browser
        	Open Browser To Login Page
        	
	Test Invalid Login
		Invalid Login    ${InvalidUser}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${InvalidUser}    ${ValidPassword}
		Go To Login Page
		Invalid Login    ${ValidUser}    ${EMPTY}
		Go To Login Page
		Invalid Login    ${ValidUser}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${EMPTY}    ${EMPTY}
		Go To Login Page
		Invalid Login    ${EMPTY}    ${ValidPassword}
		Go To Login Page


Test valid login


.. code:: robotframework

    	*** Test Cases ***
	Test Valid Login
		Login User    testrobot@test.com    testrobot


Test creating boards


.. code:: robotframework

    	*** Test Cases ***
	Test Creating Boards
		Repeat Keyword    15    Create Board


Test editing boards


.. code:: robotframework

    	*** Test Cases ***
	Test Editing Boards
		Repeat Keyword    15    Random Edit Board
		Repeat Keyword    15    Random Set Board Background


Test opening boards


.. code:: robotframework

    	*** Test Cases ***
	Test Opening Boards
		Open Board    2    16
		Open Help
		Close Help
		Close Board
		Open Board    2    16
		Close Board
		Open Board    2    16
		Close Board
		Open Board    2    16
		Close Board
		Open Board    2    16
		Close Board


Test creating tickets


.. code:: robotframework

    	*** Test Cases ***
	Test Creating Tickets
		Open Board    2    16
		Create Ticket    1    1
		Create Ticket    2    2
		Create Ticket    3    3
		Create Ticket    4    4
		Create Ticket    5    5
		Create Ticket    6    6
		Create Ticket    7    7
		Create Ticket    8    8
		Create Ticket    9    9
		Create Ticket    10    10
		Create Ticket    11    11
		Create Ticket    12    12
		Create Ticket    13    13
		Create Ticket    14    14
		Create Ticket    15    15


Test Editing Tickets


.. code:: robotframework

    	*** Test Cases ***
	Test Editing Tickets
		Repeat Keyword    15    Random Edit Ticket


Test board functionalities


.. code:: robotframework

    	*** Test Cases ***
	Test Board Functionalities
		Click Magnet On
		Click Globe On
		Create Ticket    16    16
		Create Ticket    17    17
		Create Ticket    18    18
		Create Ticket    19    19
		Click Magnet Off
		Click Globe Off
		Edit Board From Board


Test ticket deletion

.. code:: robotframework

    	*** Test Cases ***
	Test Ticket Deletion
		Repeat Keyword    5    Delete Ticket    1    10


Test board deletion


.. code:: robotframework

    	*** Test Cases ***
	Test Board Deletion
		Close Board
		Repeat Keyword    5    Delete Board    2    11


Test feedback sending


.. code:: robotframework

    	*** Test Cases ***
	#Test Feedback Sending
		#Send Feedback


Test Board sharing


.. code:: robotframework

    	*** Test Cases ***
	Test Board sharing
		Random Share Board
		Log Out
	
	Close Sharing
		Close Browser
		
	Open Shared Board
		Open Shared Board
		Login to Shared Board
		Open Help
		Close Help
		Create Ticket    1    1
		Random Edit Ticket    1    1
		Log Out
	
	Close Shared
		Close Browser
		
	Login
		Open Browser To Login Page
		Login User    testrobot@test.com    testrobot


Test Log Out


.. code:: robotframework

    	*** Test Cases ***
	Test Log Out
		Log Out
		Login User    testrobot@test.com    testrobot
		Log Out
		Login User    testrobot@test.com    testrobot
		Log Out


End Test

Contriboard testing complete --->  SELF SHUTDOWN

.. code:: robotframework

    	*** Test Cases ***
	End Test
		Close Browser
		[Teardown]
