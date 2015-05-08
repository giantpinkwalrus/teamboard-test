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
	Resource 		ScenarioTests/resource5.txt


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
		Login User


Test creating boards


.. code:: robotframework

    	*** Test Cases ***
	Test Creating Boards
		Repeat Keyword    15    New Board


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
		Random Open Board
		Close Board
		Random Open Board
		Close Board
		Random Open Board
		Close Board
		Random Open Board
		Close Board
		Random Open Board
		Close Board


Test creating tickets


.. code:: robotframework

    	*** Test Cases ***
	Test Creating Tickets
		Random Open Board
		Random Create Ticket    1    1
		Random Create Ticket    2    2
		Random Create Ticket    3    3
		Random Create Ticket    4    4
		Random Create Ticket    5    5
		Random Create Ticket    6    6
		Random Create Ticket    7    7
		Random Create Ticket    8    8
		Random Create Ticket    9    9
		Random Create Ticket    10    10
		Random Create Ticket    11    11
		Random Create Ticket    12    12
		Random Create Ticket    13    13
		Random Create Ticket    14    14
		Random Create Ticket    15    15


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
		Random Create Ticket    16    16
		Random Create Ticket    17    17
		Random Create Ticket    18    18
		Random Create Ticket    19    19
		Click Magnet Off
		Click Globe Off
		Edit Board From Board


Test ticket deletion

.. code:: robotframework

    	*** Test Cases ***
	Test Ticket Deletion
		Repeat Keyword    5    Random Delete Ticket


Test board deletion


.. code:: robotframework

    	*** Test Cases ***
	Test Board Deletion
		Close Board
		Repeat Keyword    5    Random Delete Board


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
		Random Create Ticket 	1 	1
		Random Edit Ticket    1    1
		Log Out
	
	Close Shared
		Close Browser
		
	Login
		Open Browser To Login Page
		Login User


Test Log Out


.. code:: robotframework

    	*** Test Cases ***
	Test Log Out
		Log Out
		Login User
		Log Out
		Login User
		Log Out


End Test

Contriboard testing complete --->  SELF SHUTDOWN

.. code:: robotframework

    	*** Test Cases ***
	End Test
		Close Browser
		[Teardown]
