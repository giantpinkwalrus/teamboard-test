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

This test case collection is a demonstration of how to create a simple customer journey visible from service desing
point of view




Main Idea ?
-----------

the main idea is to collect most important functions as a collection of use secenario test around the reference product ContriBoard

ContriBoard ?
-------------

ContriBoard is a reference product used as a target context of N4S@JAMK project deliverables

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

The sample service for this test suite is a variation of a classic post-it wall as a virtual version.
The application allows the user to do the following things:

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

Evelyn Holmes is 67 years old retired woman who is going to arrange birthday party to her daughters son Wallace Coleman.

.. image:: https://www.dropbox.com/s/mucdlbvj85y57vm/wallace_card%20copy.png?dl=1
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

To make everything go as smoothly as possible, Evelyn is going to use ContriBoard to collect all the important notes in one place.
Evelyn used to work as a secretary before retiring, so she is able to keep track of many things and use recent technology effectively.
She had heard about ContriBoard by her neighbour Dave Lawson, who had recommended it.

.. image:: https://www.dropbox.com/s/1sob7ixq0wvyfrl/dave_card%20copy5.png?dl=1
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

Now it's time to start our journey!

Let's take a look at this journey map to get on the right track!

.. image:: https://www.dropbox.com/s/lopv5zjj3pvgba9/user_journeys-02.png?dl=1 
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

Evelyn had created a user account for Contriboard a few weeks ago when Dave Lawson was visiting her. 
Dave helped Evelyn creating the account and password. They also created a board called "Birthday Party Arrangements"

.. code:: robotframework



	*** Settings ***
	Documentation     A test suite containing tests related to the first customer journey map.
	...
	...               These tests are data-driven by their nature. They use a single
	...               keyword, specified with Test Template setting, which is called
	...               with different arguments to cover different scenarios.
	...
	...               This suite also demonstrates using setups and teardowns in
	...               different levels.
	Suite Setup       Open Browser To Login Page
	Suite Teardown    Close Browser
	Test Setup        Go To Login Page
	#Test Template     Login With Invalid Credentials Should Fail
	Resource          resource.txt


Problems with logging in
------------------------

Evelyn has forgotten her user account and at first tries logging in by using another account name.


.. code:: robotframework


	*** Test Cases ***

	Invalid Login 
    		Input Username    invalid
    		Input Password    ${VALID PASSWORD}
    		Submit Credentials
    		Login Should Have Failed


After this Evelyn remembers the corrent account name but mistypes the password...


.. code:: robotframework

        *** Test Cases ***
	Ivalid Password
    		Input Username    ${VALID USER}
    		Input Password    invalid
    		Submit Credentials
    		Login Should Have Failed


Evelyn gets a little bit confused by why the login is not working. She tries logging in with different account
and password



.. code:: robotframework

        *** Test Cases ***
	Invalid Username And Password
    		Input Username    muusipeikko
    		Input Password    sikaposse
    		Submit Credentials
    		Login Should Have Failed



Phone ringing
-------------


RING RING! The phone is ringing!

Evelyn goes to answer the phone and Wallace who happens to be visiting his grand mother takes her place on the computer
Wallace plays with the computer and tries writing some crap account names on the login screen.
Amazingly he also realizes to press Enter after every try

.. code:: robotframework

        *** Test Cases ***
	Empty Username
    		Input Username    ${EMPTY}   
    		Input Password    invalid
    		Submit Credentials
    		Login Should Have Failed

Evelyn's phone call takes about 5 minutes so Wallace has plenty of time to play with the login screen


.. code:: robotframework

        *** Test Cases ***
	Empty Password
    		Input Username    ${VALID USER}
    		Input Password    invalid
    		Submit Credentials
    		Login Should Have Failed


Wallace hears Evelyn ending the call! He panics and clears the login form, and presses enter by accident...
He makes his quick escape to the backyard.


.. code:: robotframework

        *** Test Cases ***
	Empty User Name And Password
    		Input Username    ${EMPTY}     
    		Input Password    ${EMPTY}   
   		Submit Credentials
    		Login Should Have Failed

Logged in at Last!
------------------

By the time Evelyn comes back, Wallace is already gone. There's only an empty login form to Contriboard visible on the computer screen.
Because of the empty login form Evelyn suddenly remembers the correct login credentials.

.. code:: robotframework

        *** Test Cases ***
	Valid Login
    		Input Username    evelyn.holmes@n4sjamk.org	
    		Input Password    EveHo100$
    		Submit Credentials
    		Welcome Page Should Be Open
    		Sleep  2

How should I use it ?
---------------------

After logging in Evelyn tries clicking some buttons in order to remember how Contriboard was used. Everything Dave had told her were only mere foggy memories now. 
!Maybe I should try what happens from that button?"


.. code:: robotframework

	*** Test Cases ***
        Living in Workspace
		Go To    ${LOGIN URL}
    		Login Page Should Be Open
		Input Username    evelyn.holmes@n4sjamk.org       
                Input Password    EveHo100$
                Submit Credentials
                Welcome Page Should Be Open
                Sleep  2
                Click Element  xpath=//*[@id="sidebar-container"]/div[1]/div[4]/div[1]         
                Sleep  2
		Click Element  xpath=//*[@id="sidebar-container"]/div[1]/div[4]/div[1]
		Sleep  2
		Mouse Over  xpath=//*[@id="sidebar-container"]/div[1]/div[3]/div/nav/ul/a[2]/li
		Sleep  2
		Mouse Over  xpath=//*[@id="sidebar-container"]/div[1]/div[3]/div/nav/ul/a[1]/li
		Sleep  2
		Mouse Over  xpath=//*[@id="sidebar-container"]/div[1]/div[5]
		Sleep  1
		Click Button  xpath=//*[@id="topbar-container"]/div/div/div/div[3]/button
		Sleep  1
		Input Text  headingInput  Hire the Clown
	 	Click Button  Create
		Sleep  1
		Click Element  xpath=//*[@id="545b6355905bc10f00a94f0f"]/div[1]/div[2]/i
		Click Element  xpath=//*[@id="topbar-container"]/div/div/div/div[2]/div/div[1]
		Click Buttun  Delete
		
How should I use it ?
---------------------

Let's see how you would use it :)



