.. default-role:: code

============
Scenario 1
============

Browser: Firefox
Operation System: Ubuntu 14.04

Wallace Coleman
Occupation: Elementary school student
Age: 10

Wallace is a young student at elementary school. He has been introduced to entry
level brainstorming toold like mind maps. His school bought tablet to all of the classrooms
and so that the students can use simple web tools for their school work.


Primary Actor: Wallace Coleman

Other Actors: Dad

Roles: Common Users


.. contents:: Table of contents
   :local:
   :depth: 2


=================
Scenario 1 Tests
=================

Wallace comes home from school and goes to dads computer and starts doing assigment that he got from school.
Assigment is to try out schools new tool Contriboard and do create his own idea board.


.. code:: robotframework

	*** Settings ***
	Resource 		ScenarioTests/resource.txt


Wallace opens computer, starts internet browser and goes to the webpage where schools new tool is.


.. code:: robotframework

    	*** Test Cases ***
	Wallace opens computer
		Open Browser To Login Page


First he looks at the page that just opened and triest to remember what he needed to do.
Wallace didn't remember what he needed to do first. So he starts trying to login into the page.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Invalid Login
		Invalid Login    ${InvalidUser}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${InvalidUser}    ${EMPTY}
		Go To Login Page
		Invalid Login    ${EMPTY}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${EMPTY}    ${EMPTY}
		Go To Login Page


As he had tried to log in couple times. He gets frustrated and yells his dad to help. Dad ask what's wrong and Wallace explains.
Dad thinks for a moment and tells Wallace to try registering. So Wallace clicks register button and with his dads help registers into the page.


.. code:: robotframework

	 *** Test Cases ***
	Wallace Registers
		Register User 	wallace.coleman@test.com 	wallacecoleman


When Wallace had registered, page changed back to mainpage. Now he could try to login with his credentials that he just registered.
Wallace tries to login.

Wallace succeeds to log in. Wallace tells his dad to go away and leave him to do his assigment at peace.
When dad has gone Wallace looks a while this new page that has just opened after login and tries to remember what he needed to do next.
Wallace start to explore the page and clicking different things


.. code:: robotframework

    	*** Test Cases ***
	Wallace Explores part 1
		Wallace First Try


Wallace accidently clicked logout and page changed back to mainpage where he just started. Luckily Wallace didn't panic
and he just does logs back in.


.. code:: robotframework

    	*** Test Cases ***
	Wallace ReLogin
		Login User    wallace.coleman@test.com    wallacecoleman


And Wallace is back on the page where he accidently left before. Wallace continues clicking.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Explores Part 2
		Repeat Keyword    3    Create Board

	Wallace Tests Help
		Open Board    2    2
		Open Help
		Close Help
		Close Board


Wallace found how to create boards. And remembers that teacher said that he has to name his idea board and change background of the board.
Wallace sees pen icon and trashcan icon on the boards that he just created. And tries clicking those icons.

Wallace deleted a board. He clicks pen icon on other board.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Tries Board buttons
		Delete Board    4    4
		Click Edit Board    3    3


Wallace opened board edit window. Wallace thinks sometime what name would be good for his board 
Wallace writes name for the board: "Ideas of Wallace" and tries to change background by clicking background list and testing different background possibilities.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Edits board
		Input Board Name    Ideas of Wallace
		Change Background    1    1
		Change Background    2    2
		Change Background    3    3
		Change Background    4    4
		Change Background    5    5
		Change Background    6    6
		Change Background    7    7
		Change Background    8    8
		Change Background    0    0


Wallace has decided what background he wants. Now that Wallace has named his board and chosen a background now he just need to click done button. 
But bird flies into window and Wallace accidently clicks cancel button. 


.. code:: robotframework

    	*** Test Cases ***
	Wallace Sets Background and clicks cancel
		Change Background    6    6
		Click Cancel Edit Board


Board naming and background setting was all in vain. So Wallace has to start editing board all again.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Edit Board Again
		Click Edit Board    3    3
		Input Board Name    Ides of Wallace
		Change Background    6    6
		Click Done Board Edit


Wallace has named his board, changed background and successfully clicked done button. Wallace clicks the board he just edited.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Opens Board
		Open Board    3    3


Page changes to new page and Wallace looks it carefully and thinks what he need to do next. Then mom calls Wallace to dinner.
Wallace goes to eat dinner and leaves computer as is.

Half hour later Wallace comes back and starts to explore and clicking things.


.. code:: robotframework

	 *** Test Cases ***
	Wallace Explores Part 3
		Click Magnet On
		Click Globe On
		Click Magnet Off
		Click Globe Off
		Click Edit Board From Board


When Wallace clicked pen he noticed that he had written his board name wrong. So he erases it and writes it again.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Changes Wrong Board Name
		Input Board Name    Ideas of Wallace
		Click Done Board Edit


Now that boards name is correct he starts clicking again.
Wallace noticed that by double clicking board he created tickets. Wallace tries to move a ticket.

.. code:: robotframework

	*** Test Cases ***
	Wallace Creates Tickets
		Create Ticket    1    1
		Create Ticket    2    2
		Create Ticket    3    3
		Create Ticket    4    4
		Create Ticket    5    5


Wallace learns that he can move tickets. Now he tries what magnet icon do and clicks it.
Nothing seems to happen so Wallace moves tickets and triest to find what magnet does.


.. code:: robotframework

	 *** Test Cases ***
	Wallace Tries Magnet
		Click Magnet On
		Create Ticket    6    6
		Create Ticket    7    7
		Create Ticket    8    8
		Click Magnet Off
		Create Ticket    9 	9
		Create Ticket    10 	10
		Create Ticket    11    11


Wallace learned what magnet do and creates more ticket and organizes them.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Creates And Moves New Tickets
		Create Ticket 	12    12
		Create Ticket 	13    13
		Create Ticket 	14    14


He has organized tickets where he wants them. Now Wallace thinks how he can write his ideas on the tickets
Wallace founds out that by double clicking ticket it opens ticket and he can write there. Wallace writes his idea on ticket.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Learns to Edit Ticket
		Open Ticket Edit    1    1
		Input Ticket Text    Idea Of Wallace1
		Click Done Ticket Edit


Wallace has written his first idea on a ticket. So writes he more on other tickets.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Edits Tickets
		Open Ticket Edit    2    2
		Input Ticket Text    Idea Of Wallace2
		Click Done Ticket Edit
		Open Ticket Edit    3    3
		Input Ticket Text    Idea Of Wallace3
		Click Done Ticket Edit
		Open Ticket Edit    4    4
		Input Ticket Text    Idea Of Wallace4
		Click Done Ticket Edit
		Open Ticket Edit    5    5
		Input Ticket Text    Idea Of Wallace5
		Click Done Ticket Edit
		Open Ticket Edit    6    6
		Input Ticket Text    Idea Of Wallace6
		Click Done Ticket Edit


Wallace has written more ideas on tickets and can't think anymore new ideas but there are still empty tickets
that he had created before. So Wallace tries to delete them and double clicks a empty ticket.
Wallace notices that there is a delete button on the opened ticket. He clicks it.
Wallace succesfully deleted empty ticket and starts deleting rest of the empty tickets.


.. code:: robotframework

    	*** Test Cases ***	
	Wallace Deletes Obselete Tickets	
		Delete Ticket    14    14
		Delete Ticket    13    13
		Delete Ticket    12    12
		Delete Ticket    11    11
		Delete Ticket    10    10
		Delete Ticket    9    9
		Delete Ticket    8    8
		Delete Ticket    7    7


Wallace deleted rest of the empty tickets and he thinks that he has finished his assigment. 
He thinks how he can close his board and sees arrow icon.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Closes Board
		Close Board


Wallace has closed his board but he wants to check that his tickets are still there so he opens his board.
And everything seems to be there.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Checks The Board
		Open Board    3    3
		Close Board


Wallace is done his assigment but now he needs to close the page. Wallace is too tired to think how he can leave the page.
So he calls his dad for help. Dad helps Wallace to close the page.


.. code:: robotframework

    	*** Test Cases ***
	Wallace Is Done
		Log Out
	
	Close
		Close Browser
		[Teardown]


Wallace thanks his dad and runs to play his Xbox.
