.. default-role:: code

=======================================================================
  Contriboard Reference Product - Demostration for Customer Journey 
=======================================================================

Primary Actor: Evelyn Holmes

Other Actors: Wallace and Dave

Roles: Common Users




.. contents:: Table of contents
   :local:
   :depth: 2

============
Introduction
============



About this customer journey
---------------------------

This test case collection is trying to create a simple customer journey visible from service desing
point of use




Main Idea ?
-----------

Main idea is to collect most important funtions as collection of usage secenario test around reference product ContriBoard

ContriBoard ?
-------------

ContriBoard is a reference product which is used as on target context of N4S@JAMK project deliverables

Robot Framework overview
------------------------

`Robot Framework` is a generic open source test automation framework for
acceptance testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test libraries
implemented either with Python or Java, and users can create new higher-level
keywords from existing ones using the same syntax that is used for creating
test cases.

Reference Service
-----------------

The sample service for this test suite is a variation on a classic post-it wall as a virtual version.
The application allows a user to do three things:

  Login
  Create new board
  Share board
  Create new tickets
  Move tickets on board
  Add text inside tickets
  Work in real-time

Customer/Users During Scenario
-------------------------------

Evelyn Holmes

.. image:: https://www.dropbox.com/s/9tkaawsvn2gmw7m/evelyn_card%20copy.png?dl=1 
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

Evelyn Holmes is 67 years old retired woman who is going to arrange birthday party to his daughters son Wallace Coleman.

.. image:: https://www.dropbox.com/s/mucdlbvj85y57vm/wallace_card%20copy.png?dl=1
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

To make everthing happen ok, Evelyn is going to use ContriBoard as collect important notes on one place.
Evelen was working as a secretary in her previous work, so she is able to coordinate many items and using latest technology
ContriBoard as a tool was sold as an idea to her by his neighbour Dave Lawson.

.. image:: https://www.dropbox.com/s/1sob7ixq0wvyfrl/dave_card%20copy5.png?dl=1
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

Let's start our journey!

Take a look at this journey map to get on right track!

.. image:: https://www.dropbox.com/s/lopv5zjj3pvgba9/user_journeys-02.png?dl=1 
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

Evelyn has created user account for Contriboard few weeks ago when Dave Lawson was visting her. 
Dave helped Evelyn to create account and password. They also created a board called "Birthday Party Arragements"

.. code:: robotframework

	*** Settings ***
	Documentation     A test suite containing tests related to the first customer journey map.
	...
	...               These tests are data-driven by they nature. They use a single
	...               keyword, specified with Test Template setting, that is called
	...               with different arguments to cover different scenarios.
	...
	...               This suite also demonstrates using setups and teardowns in
	...               different levels.
	Suite Setup       Open Browser To Main Page
	Suite Teardown    Close Browser
	Test Setup        Go To Login Page
	#Test Template     Login With Invalid Credentials Should Fail
	Resource          resource.txt


Problems with login
-------------------

Evelyn has forgotten which email she used for Contriboard and tries to login using her usual email account which is sadly wrong.


.. code:: robotframework

    *** Test Cases ***
    Invalid Username
    		Input Invalid Username
    		Input Valid Password
    		Submit Credentials
    		Login Should Fail


Evelyn remembers she created a email just for Contriboard. Evelyn uses the correct account but does a typo with password.


.. code:: robotframework

    *** Test Cases ***
    Invalid Password
    		Input Valid Username
            Input Invalid Password
            Submit Credentials
            Login Should Fail


Evelyn Is little bit out of ideas why login is not working. She tries to login with another email and password.



.. code:: robotframework

    *** Test Cases ***
    Invalid Username And Password
    		Input Invalid Username
            Input Invalid Password
            Submit Credentials
            Login Should Fail


Phone ringing
-------------


RING RING! Phone rings!

Evelyn goes to the phone and Wallace who is visiting his grandmother takes a seat by the computer.
Wallace thinking that he will help his grandmother and crack the login of Contriboard so his grandmother can start working on his birthday party.
Wallace uses his considerable powers of guessing to try crack the login. Sadly he forgets to type in the username and also suprisingly doesn't guess the password right.

.. code:: robotframework

    *** Test Cases ***
    Empty Username
    		Empty Username   
    		Input Valid Password
    		Submit Credentials
    		Login Should Fail


Evelyns phone call takes a 5 minutes so Wallace has plenty of time to play with login screen


.. code:: robotframework

    *** Test Cases ***
    Empty Password
    		Input Valid Username
    		Input Invalid Password
    		Submit Credentials
    		Login Should Fail


Wallace hears Evelyn closed the phone! In panic Wallace cleans login form values and pressed by mistake enter...
Wallace runs to the backyard


.. code:: robotframework

    *** Test Cases ***
    Empty Username And Password
    		Empty Username    
    		Empty Password  
            Submit Credentials
    		Login Should Fail


Login at Last!
--------------

At last Evelyn is comes back and Wallace has vanished. There is only login screen to Contriboard with empty values from login screen
Because of empty login screen Evelyn remembers now correct account and password

.. code:: robotframework

    *** Test Cases ***
    Valid Login
    		Input Valid Username	
    		Input Valid Password
    		Submit Credentials
    		Login Should Succeed


How should I use it ?
---------------------

After login in Evelyn try to click some buttons to be able to recover how Contriboard was used. All what Dave was told her last week were foggy memories. There is nice button I should try to click some!


.. code:: robotframework

    *** Test Cases ***
    Living in Workspace
        Input Valid Username       
        Input Valid Password
        Submit Credentials
        Login Should Succeed
        Check Localization Options
        Add Board
        Remove Board
		
        
And what now?....
---------------------






