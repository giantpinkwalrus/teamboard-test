.. default-role:: code

============
Scenario3
============

Browser: Internet Explorer 11
Operation System: Windows 8.1

Evelyn Holmes
Occupation: Retired person
Age: 67

Evelyn is retired person who is really active member of various senior
communities and societies. She just bought a computer and tries to keep
up with the technology.


Primary Actor: Evelyn Holmes

Other Actors: Wallace and Dave

Roles: Common Users


.. contents:: Table of contents
   :local:
   :depth: 2


=================
Scenario 3 Tests
=================

Evelyn is going to arrange birthday party to his daughters son Wallace Coleman.


To make everything happen ok, Evelyn is going to use ContriBoard as collect important notes on one place. 
Evelyn was working as a secretary in her previous work, so she is able to coordinate many items and using latest technology 
ContriBoard as a tool was sold as an idea to her by his neighbour Dave Lawson.


Evelyn has created user account for Contriboard few weeks ago when Dave Lawson was visting her. 
Dave helped Evelyn to create account and password. They also created a board called "Birthday Party Arragements"


.. code:: robotframework

	*** Settings ***
	Resource 		ScenarioTests/resource3.txt
	

Evelyn has forgotten which email she used for Contriboard and tries to login using her usual email account which is sadly wrong.

Evelyn remembers she created a email just for Contriboard. Evelyn uses the correct account but does a typo with password.

Evelyn Is little bit out of ideas why login is not working. She tries to login with another email and password.


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Opens Computer
    		Open Browser To Login Page	
	
	
	Evelyn Invalid Login
		Invalid Login    ${InvalidUser}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${ValidUser}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${InvalidUser}    ${InvalidPassword}
		Go To Login Page


Phone ringing

RING RING! Phone rings!

Evelyn goes to the phone and Wallace who is visiting his grandmother takes a seat by the computer. 
Wallace thinking that he will help his grandmother and crack the login of Contriboard so his grandmother 
can start working on his birthday party. Wallace uses his considerable powers of guessing to try crack the login. 
Sadly he forgets to type in the username and also suprisingly doesn't guess the password right.

Evelyns phone call takes a 5 minutes so Wallace has plenty of time to play with login screen

Wallace hears Evelyn closed the phone! In panic Wallace cleans login form values and presses by mistake enter... Wallace runs to the backyard


.. code:: robotframework

    	*** Test Cases ***
	Wallace Invalid Login
		Invalid Login    ${EMPTY}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${InvalidUser}    ${InvalidPassword}
		Go To Login Page
		Invalid Login    ${EMPTY}    ${EMPTY}
		Go To Login Page


At last Evelyn is comes back and Wallace has vanished. There is only login screen to Contriboard with empty values
from login screen Because of empty login screen Evelyn remembers now correct account and password


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Valid Login
		Login User


After login in Evelyn try to click some buttons to be able to recover how Contriboard was used. 
All what Dave was told her last week were foggy memories. "There is nice button I should try to click some!"


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Explores Everything
		Click Profile
		#Click Feedback
		Close Profile
		Create Board
		Click Edit Board    3    3
		Click Done Board Edit
		Open Board    3    3
		Create Ticket
		Move Ticket    1    1
		Click Magnet On
		Click Globe On
		Click Magnet Off
		Click Globe Off
		Click Edit Board From Board
		Click Done Board Edit
		Edit Ticket    1    1
		Delete Ticket    1    1
		Close Board
		Delete Board    2    2


Now that she has clicked some buttons she has somekind on idea what she need to do. So she opens the board she and Dave created before.


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Opens Board That Was Created Before
		Open Board    2    2

Evelyn starts creating ticket as tasks what she need to do for the birthday party.


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Creates And Edits Tickets
		Repeat Keyword    6    Create Ticket
		Open Ticket Edit    1    1
		Input Ticket Text    Cake
		Click Done Ticket Edit
		Open Ticket Edit    2    2
		Input Ticket Text    Clown
		Click Done Ticket Edit
		Open Ticket Edit    3    3
		Input Ticket Text    Other foods
		Click Done Ticket Edit
		Open Ticket Edit    4    4
		Input Ticket Text    Drinks
		Click Done Ticket Edit
		Open Ticket Edit    5    5
		Input Ticket Text    Invites
		Click Done Ticket Edit
		Open Ticket Edit    6    6
		Input Ticket Text    Other Entertaiment
		Click Done Ticket Edit


Evelyn organizes tasks on priorities order which need to do first.


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Organizes Tickets
		Click Magnet On
		Move Ticket    1    1
		Move Ticket    2    2
		Move Ticket    3    3
		Move Ticket    4    4
		Move Ticket    5    5
		Move Ticket    6    6


Evelyn calls for Wallace to come help her. Wallace runs to Evelyn and Evelyn asks what he wants for his birthday. 
What kind of cake? What foods he wants? Who to Invite? What kind of entertaiment he wants? 


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Edits Tickets
		Open Ticket Edit    1    1
		Input Ticket Text    Cake: Chocolate
		Click Done Ticket Edit
		Open Ticket Edit    2    2
		Input Ticket Text    Clown: No Need
		Click Done Ticket Edit
		Open Ticket Edit    3    3
		Input Ticket Text    Other foods: Chips and Candy
		Click Done Ticket Edit
		Open Ticket Edit    4    4
		Input Ticket Text    Drinks: Coke, Sprite, Fanta, Water and Juice
		Click Done Ticket Edit
		Open Ticket Edit    5    5
		Input Ticket Text    Invites: Classmates
		Click Done Ticket Edit
		Open Ticket Edit    6    6
		Input Ticket Text    Other Entertaiment: Games
		Click Done Ticket Edit


Now that Wallace and Evelyn had added everything on the tickets. Evelyn stops planning for today and closes the board and logs out.


.. code:: robotframework

    	*** Test Cases ***
	Evelyn Is Ready
		Close Board
		Log Out
	
	Close
		Close Browser
		[Teardown]

