.. default-role:: code

============
Scenario4
============

Browser: Firefox
Operation System: Ubuntu 14.04

James Nicholson
Occupation: Programmer
Age: 25

James is a programmer in small software company. James spend his working hours to
programming sofwares and designing new software. James uses spare time to make small mobile games and
hopes that he can someday make games for living.


Primary Actor: James Nicholson

Other Actors: TBA

Roles: Power user


.. contents:: Table of contents
   :local:
   :depth: 2


=================
Scenario 4 Tests
=================

James has made a small mobile game for android devices in 

.. code:: robotframework

	*** Settings ***
	Resource 		ScenarioTests/resource.txt
	

He needs to do sprint plan and SWOT for his product that he has made. James is using Contriboard as he has used it many times before
and knows what he can do with it.

James has a existing account for Contriboard so he logs in.


.. code:: robotframework

    	*** Test Cases ***
	James Opens Computer And Login
		Open Browser To Login Page
		Login User    james.nicholson@test.com    jamesnicholson
			

James succeeds to log in. James needs to do a SWOT plan and sprint plan so he creates two boards for those


.. code:: robotframework

    	*** Test Cases ***
	James Creates SWOT Board
		Create Board
		Click Edit Board    2    2
		Input Board Name    SWOT of Cool Game
		Change Background    3    3
		Click Done Board Edit
			
	James Creates Sprint Plan Board
		Create Board
		Click Edit Board    3    3
		Input Board Name    Sprint Plan of Cool Game
		Change Background    5    5
		Click Done Board Edit


James has created his boards so now he needs to start making his plans.


.. code:: robotframework

    	*** Test Cases ***
	James Opens SWOT Board
		Open Board    2    2
		Open Help
		Close Help


James clicks magnet on because he knows that using magnet will set tickets in places.
Now he his ready start to work. James start creating tickets, writing his things on them and moving them to correct places.


.. code:: robotframework

    	*** Test Cases ***
	James Creates Tickets To SWOT Board
		Click Magnet On
		Create Ticket    1    1
		Open Ticket Edit    1    1
		Input Ticket Text    Cool
		Click Done Ticket Edit
		Create Ticket    2    2
		Open Ticket Edit    2    2
		Input Ticket Text    Fun
		Click Done Ticket Edit
		Create Ticket    3    3
		Open Ticket Edit    3    3
		Input Ticket Text    Awesome
		Click Done Ticket Edit
		Create Ticket    4    4
		Open Ticket Edit    4    4
		Input Ticket Text    Bad
		Click Done Ticket Edit
		Create Ticket    5    5
		Open Ticket Edit    5    5
		Input Ticket Text    Good
		Click Done Ticket Edit


James thinks for a moment if there is anythin else to add.

James makes some additions on his plans and removes some that he thinks are obselete.


.. code:: robotframework

    	*** Test Cases ***
	James Edits Tickets
		Create Ticket    6    6
		Open Ticket Edit    6    6
		Input Ticket Text    Special
		Click Done Ticket Edit
		Create Ticket    7    7
		Open Ticket Edit    7    7
		Input Ticket Text    Random
		Click Done Ticket Edit
		Create Ticket    8    8
		Open Ticket Edit    8    8
		Input Ticket Text    Excellent
		Click Done Ticket Edit
		Click Magnet Off

	James Deletes Obselete Tickets
		Delete Ticket    2    2
		Delete Ticket    3    3


Now he is done his SWOT. So he continues to his sprint plan.


.. code:: robotframework

    	*** Test Cases ***
	James Changes Board
		Close Board
		Open Board    3    3


James starts to think what he need to do and which order.

As he had thinked his plan through in his head he starts creating tickets.


.. code:: robotframework

    	*** Test Cases ***
	James Creates Tickets To Sprint Plan
		Click Magnet On
		Create Ticket    1    1
		Open Ticket Edit    1    1
		Input Ticket Text    Code
		Click Done Ticket Edit
		Create Ticket    2    2
		Open Ticket Edit    2    2
		Input Ticket Text    Design
		Click Done Ticket Edit
		Create Ticket    3    3
		Open Ticket Edit    3    3
		Input Ticket Text    Test
		Click Done Ticket Edit
		Create Ticket    4    4
		Open Ticket Edit    4    4
		Input Ticket Text    Make AI
		Click Done Ticket Edit
		Create Ticket    5    5
		Open Ticket Edit    5    5
		Input Ticket Text    Plan
		Click Done Ticket Edit
		Click Magnet Off

James thinks for a moment if there is anythin else to add.

James looks at his plan and thinks that it is ready. So he closes the board.


.. code:: robotframework

    	*** Test Cases ***
	James Closes Board and Board is Deleted
		Close Board
		Delete Board    3    3


For some reason when he closed the board error show up and the board he just finished is destroyd.

James is furios. He tries to logout and login again if that returns his board.


.. code:: robotframework

    	*** Test Cases ***
	James Log Out and Login
		Log Out
		Login User    james.nicholson@test.com    jamesnicholson


James doesn't see his board. It's gone! So James starts to write angry feedback with Contriboard feedback sender.


.. code:: robotframework

    	*** Test Cases ***
	#James Sends Angry Feedback
		#Send Feedback
			

As he has written his feedback. He goes for a smoke to calm his nerves.

James comes back and checks his email if there is any response on his feedback. James has gotten a response that says: "disappeared board cannot be restored".
So James has no other choice than create it again.


.. code:: robotframework

    	*** Test Cases ***
	James Creates Sprint Plan Board Again
		Create Board
		Click Edit Board    3    3
		Input Board Name    Sprint Plan of Cool Game
		Change Background    5    5
		Click Done Board Edit


James starts to creating tickets to the board. Luckily he remembers what he had planned on the board.


.. code:: robotframework

    	*** Test Cases ***
	James Creates Tickets to Sprint Plan Board Again
		Open Board    2    2
		Click Magnet On
		Create Ticket    1    1
		Open Ticket Edit    1    1
		Input Ticket Text    Code
		Click Done Ticket Edit
		Create Ticket    2    2
		Open Ticket Edit    2    2
		Input Ticket Text    Design
		Click Done Ticket Edit
		Create Ticket    3    3
		Open Ticket Edit    3    3
		Input Ticket Text    Test
		Click Done Ticket Edit
		Create Ticket    4    4
		Open Ticket Edit    4    4
		Input Ticket Text    Make AI
		Click Done Ticket Edit
		Create Ticket    5    5
		Open Ticket Edit    5    5
		Input Ticket Text    Plan
		Click Done Ticket Edit
		Click Magnet Off
		Close Board
			
			
Now that he has done it he closes the board and wish that the error which occured before dont occur againg.

Board closes as it should. James checks both boards before leaving to do other things.


.. code:: robotframework

    	*** Test Cases ***
	James Checks both Boards
		Open Board    3    3
		Close Board
		Open Board    2    2
		Close Board
			

James has checked his boards as seems like everything is ready. So James logout and go do something else.


.. code:: robotframework

    	*** Test Cases ***
	James Is Ready
		Log Out
	
	Close
		Close Browser
		[Teardown]
