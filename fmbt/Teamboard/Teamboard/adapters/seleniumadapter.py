#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Selenium adapter for Teamboard testmodel

@author: Antti Minkkinen
'''

import os
import random
from time import sleep, time, strftime, gmtime
from glob import glob
from utils import TypeHelper

from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

b = webdriver.Firefox()

url = 'http://teamboard.n4sjamk.org/'
b.get(url)

'''
globals
'''
screenCount = 0

resultsPath = "../../fmbt-testresults"

pollTime = 0.3      #page change poll delay, used as delay in other actions too
                    #the more ram in testmachine the shorter pollTime can be used
                    
timeoutTime = 2.0   #max time between page loads

account = ""

stateAssets = {
                "login"               : ["text", ["h2", "Login"]],
                "register"            : ["text", ["h2", "Register"]],
                "boardmenu"           : ["text", ["h2", "Workspace"]],
                "removeboard_dialog"  : ["text", ["h3", "Remove board?"]],
                "addboard_dialog"     : ["text", ["h3", "Create board"]],
                "board"               : ["text", ["h2", "Board:"]],
                "createticket_dialog" : ["text", ["label", "Color"]],
                "editticket_dialog"   : ["text", ["label", "Color"]],
                "editboard_dialog"    : ["text", ["h3", "Edit board"]]
               }

def rs():
    global screenCount
    # wipe screens
    if screenCount > 20:
        wipeScreens()
        screenCount = 0
    screenCount += 1
    stamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    b.save_screenshot(resultsPath + "/"+stamp+".png")

'''
init(): called before starting model testing
'''
def init():
    b.maximize_window()
    TypeHelper.initWords()

    global account
    if os.path.isfile('account'):
        f = open('account','r')
        account = f.readline()
    wait(2.0)

'''
restart browser to release memory
'''
def reinitDriver():
    global b
    b.quit()
    b = webdriver.Firefox()
    b.get(url)
    b.maximize_window()

'''
cleanup(): called after model execution has finished
'''
def cleanup():
    #cleanup stuff here (zip testresults etc.)
    return


'''
utility functions
'''
def isElement(css):
    try:
        if b.find_element_by_css_selector(css).is_displayed():
            return True
        else:
            return False
    except:
        return False

def findElementByText(elementCss, text):
    if isElement(elementCss):
        elements = b.find_elements_by_css_selector(elementCss)
        for e in elements:
            if text not in e.text:
                elements.remove(e)
        elem = random.choice(elements)
        return elem
    return False

def clickDialogButton(button = 0):
    buttonSets = b.find_elements_by_css_selector("div.modal-footer")
    for buttonSet in buttonSets:
        if buttonSet.is_displayed():
            buttons = buttonSet.find_elements_by_css_selector("button.btn") + buttonSet.find_elements_by_css_selector("label.btn")
            btn = buttons[button]
            btn.click()
            return True

def clickRadioButton(button = 0):
    buttonSets = b.find_elements_by_css_selector("div.radiogroup")
    for buttonSet in buttonSets:
        if buttonSet.is_displayed():
            btn = buttonSet.find_elements_by_css_selector("label.radioselect")[button]
            btn.click()
            return True
    
def checkAlert():
    try:
        WebDriverWait(b,pollTime).until(EC.alert_is_present())
        if EC.alert_is_present() == False:
            return False
        else:
            return True
    except:
        return False

def confirmAlert():
    if checkAlert():
        Alert(b).accept()
    
def confirmResponse():
    if isElement("div#dialog-response"):
        clickDialogButton(0)
 

def getAccount():
    return account

def wipeScreens():
    for f in glob (resultsPath + '/*.png'):
        os.unlink (f)
    for f in glob (resultsPath + '/*.xwd'):
        os.unlink (f)

def wait(time=pollTime):
    sleep(time)
    
def homePage():
    rs()
    b.get(url)

def refreshPage():
    b.refresh()
    
def clearText():
    return

def resetCursor():
    return


'''
login
'''
def clickSignin():
    rs()
    b.find_element_by_css_selector("button.btn[type='submit']").click()
    wait()

def clickCreateaccount():
    rs()
    if isElement("a[href='/register']"):
        b.find_element_by_css_selector("a[href='/register']").click()

def typeLoginInfo():
    global account
    if len(account) < 3:
        return
    rs()
    b.find_element_by_css_selector("input[name='email']").send_keys(account)
    b.find_element_by_css_selector("input[name='password']").send_keys(account)
    

def deleteAccount(): #doesn't do anything on screen but deletes a file from disk
    global account
    account = ""
    if os.path.isfile("account"):
        os.remove("account")
    reinitDriver()
    wait(2.0)

def checkUnauthorized():
    rs()
    if isElement("p.ng-binding") and b.find_element_by_css_selector("p.ng-binding").text() == "Unauthorized":
        return True
    else:
        return False
    

'''
register
'''
def typeRegisterInfo():
    global account
    if account:
        return
    account = TypeHelper.getUsername()
    f = open('account','w')
    f.write(account)
    f.close()
    
    rs()
    b.find_element_by_css_selector("input[name='email']").send_keys(account)
    b.find_element_by_css_selector("input[name='password']").send_keys(account)
    
def clickRegister():
    rs()
    b.find_element_by_css_selector("button.btn[type='submit']").click() 
    
def clickLogintext():
    rs()
    if isElement("a[href='/login']"):
        b.find_element_by_css_selector("a[href='/login']").click()

  

'''
boardmenu
'''
def clickBoard():
    rs()
    #random board
    if isElement("img.board"):
        boards = b.find_elements_by_css_selector("img.board")
        random.choice(boards).click()

def clickRemoveBoard():
    rs()
    if isElement("button.btn-removeboard"):
        crosses = b.find_elements_by_css_selector("button.btn-removeboard")
        random.choice(crosses).click()

def clickAddBoard():
    rs()
    b.find_element_by_css_selector("span.glyphicon-plus").click()

def clickLogout():
    rs()
    elem = b.find_element_by_css_selector("span.glyphicon-log-out")
    if elem != False:
        elem.click()
    
def clickPublicHeading():
    rs()
    elem = findElementByText("span[ng-if]", "Public")
    if elem != False:
        elem.click()

def clickPrivateHeading():
    rs()
    elem = findElementByText("span[ng-if]", "Private")
    if elem != False:
        elem.click()

def scrollUp():
    # not implemented
    return

def scrollDown():
    # not implemented
    return

def checkPrivateBoard():
    try:
        elem = findElementByText("span[ng-if]", "Private")
        if elem != False:
            return True
    except:
        return False
    
def checkPublicBoard():
    try:
        elem = findElementByText("span[ng-if]", "Public")
        if elem != False:
            return True
    except:
        return False

'''
removeboard_dialog
'''
def clickRemoveBoardDialogRemove():
    rs()
    clickDialogButton(1)
    
def clickRemoveBoardDialogCancel():
    rs()
    clickDialogButton(0)


'''
addboard_dialog
'''
def clickAddBoardDialogCreate():
    rs()
    clickDialogButton(1)

def clickAddBoardDialogCancel():
    rs()
    clickDialogButton(0)

def clickPublic():
    rs()
    clickRadioButton(1)

def clickPrivate():
    rs()
    clickRadioButton(0)

def typeBoardName():
    rs()
    b.find_element_by_css_selector("input#headingInput").send_keys(TypeHelper.getBoardName())

def clickCancel():
    rs()
    clickDialogButton(0)


'''
editboard
'''
def clickApply():
    rs()
    clickDialogButton(1)


'''
board
'''
def clickAddTicket():
    rs()
    b.find_element_by_css_selector("span.glyphicon-plus").click()

def clickTicket():
    rs()
    b.find_element_by_css_selector("div.ticket").click()

def clickEdit():
    rs()
    b.find_element_by_css_selector("button.btn-editticket").click()

def dragTicket():
    rs()
    tickets = b.find_elements_by_css_selector("div.ticket")
    if len(tickets)<1:
        return
    ticket = random.choice(tickets)

    board = b.find_element_by_css_selector("div#board")
    xdest = random.randint(0, board.size.get('width') - ticket.size.get('width'))
    ydest = random.randint(0, board.size.get('height') - ticket.size.get('height'))
    
    AC(b).click_and_hold(ticket).move_to_element_with_offset(board, xdest, ydest).release(ticket).perform()
    
def clickSnap():
    rs()
    b.find_element_by_css_selector("span.glyphicon-magnet").click()

def clickRemoveTicket():
    rs()
    b.find_element_by_css_selector("span.glyphicon-remove").click()
    
def clickWorkspace():
    rs()
    elem = b.find_element_by_css_selector("span.glyphicon-th")
    if elem != False:
        elem.click()


'''
createticket_dialog
'''
def clickCreate():
    rs()
    clickDialogButton(1)

def clickCancelTicket():
    rs()
    clickDialogButton(0)

def typeTicketName():
    rs()
    b.find_element_by_css_selector("input#headingInput").send_keys(TypeHelper.getTicketName())
    b.find_element_by_css_selector("div#contentInput div.form-control").click()
    b.find_element_by_css_selector("div#contentInput div[contenteditable]"). send_keys(TypeHelper.getTicketContent())

def clickColor():
    color = random.randint(0,3)
    clickRadioButton(color)


'''
editticket_dialog
'''
def clickClose():
    rs()
    clickDialogButton(0)


def clickApplyTicket():
    rs()
    clickDialogButton(1)

def typeTicketContent():
    rs()
    b.find_element_by_css_selector("div#contentInput div.form-control").click()
    b.find_element_by_css_selector("div#contentInput div[contenteditable]"). send_keys(TypeHelper.getTicketContent())


'''
functions to check if elements are present on screen
'''
def checkRemoveBoard():
    rs()
    result = isElement("button.btn-removeboard")
    if result:
        return True
    else:
        return False

def checkBoard():
    result = isElement("img.board")
    if result:
        return True
    else:
        return False

def checkTicket():
    rs()
    result = isElement("div.ticket")
    if result:
        return True
    else:
        return False

'''
checkState(stateToCheck):
    called when we need to verify the current state
    
    return True if state is same as param or False if not
'''
def checkState(stateToCheck):
    rs()
    element = stateAssets[stateToCheck][1][0]
    text    = stateAssets[stateToCheck][1][1]
    try:
        if isElement(element) and text in b.find_element_by_css_selector(element).text:
            return True
    except:
        return False
        
    return False

'''
verifyStateChangeTo(newState):
    waits until state has changed to newState
    
    return True if state changed or False if timeout
'''
def verifyStateChangeTo(newState):
    if len(newState) < 1:
        return True
    rs()
    startTime = time()
    while time() - startTime < timeoutTime:
        try:
            if stateAssets[newState][0] == "text":
                element = stateAssets[newState][1][0]
                text    = stateAssets[newState][1][1]
                if isElement(element):
                    el = b.find_element_by_css_selector(element)
                    if text in el.text:
                        return True
        except:
            wait()
            continue
    return False
