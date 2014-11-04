.. default-role:: code

=========================================================
  ContriBoard Acceptance Testing for Customer Journey 1
=========================================================

Customer: Evelyn Scott
Role: Common user


.. contents:: Table of contents
   :local:
   :depth: 2


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

Focus User Group
----------------

. image:: https://www.dropbox.com/s/9tkaawsvn2gmw7m/evelyn_card%20copy.png?dl=0 
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right










.. code:: robotframework



	*** Settings ***
	Documentation     A test suite containing tests related to invalid login.
	...
	...               These tests are data-driven by they nature. They use a single
	...               keyword, specified with Test Template setting, that is called
	...               with different arguments to cover different scenarios.
	...
	...               This suite also demonstrates using setups and teardowns in
	...               different levels.
	Suite Setup       Open Browser To Login Page
	Suite Teardown    Close Browser
	Test Setup        Go To Login Page
	#Test Template     Login With Invalid Credentials Should Fail
	Resource          resource.txt

Evelyn Scot has forget her user account and tryes first login in using another account name.


.. code:: robotframework


	*** Test Cases ***

	Invalid Login 
    		Input Username    invalid
    		Input Password    ${VALID PASSWORD}
    		Submit Credentials
    		Login Should Have Failed

Evelyn remembers corrent account but does typo with password..


.. code:: robotframework

        *** Test Cases ***
	Ivalid Password
    		Input Username    ${VALID USER}
    		Input Password    invalid
    		Submit Credentials
    		Login Should Have Failed

Evelyn Is little bit out of idea why login is not working. She tries to login with another account
and password


.. code:: robotframework

        *** Test Cases ***
	Invalid Username And Password
    		Input Username    muusipeikko
    		Input Password    sikaposse
    		Submit Credentials
    		Login Should Have Failed


Evelyn goes to the phone and 3 year old son Joseph takes a place from computer
Joseph plays with a computer and writes some crap account names on login screen 
Amazingly he can also press Enter

.. code:: robotframework

        *** Test Cases ***
	Empty Username
    		Input Username    ${EMPTY}   
    		Input Password    invalid
    		Submit Credentials
    		Login Should Have Failed

Evelyns phone call takes a 5 minutes so Josep has plenty of time to play with login screen


.. code:: robotframework

        *** Test Cases ***
	Empty Password
    		Input Username    ${VALID USER}
    		Input Password    invalid
    		Submit Credentials
    		Login Should Have Failed


At last Evelyn is comes back and Joseph has cleared all values from login screen

.. code:: robotframework

        *** Test Cases ***
	Empty User Name And Password
    		Input Username    ${EMPTY}     
    		Input Password    ${EMPTY}   
   		Submit Credentials
    		Login Should Have Failed


Because of empty login screen Evelyn remembers now correct account and password

.. code:: robotframework

        *** Test Cases ***
	Valid Login
    		Input Username    testuser@tester.org
    		Input Password    testuseri
    		Submit Credentials
    		Welcome Page Should Be Open

