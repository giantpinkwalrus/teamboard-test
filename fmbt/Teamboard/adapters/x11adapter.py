#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
x11 Adaptercode for model based testing of Teamboard
Uses x11 to send events and receive screenshots

Image assets for image recognition are located in assets folder

   Preconditions for use:
   - Machine has Firefox running
   - Firefox has its homepage set to Teamboard
   - Firefox window has focus before running

@author: Antti Minkkinen
'''
import fmbtx11
import os
import random
from time import sleep
from glob import glob
from utils import TypeHelper

'''
globals
'''
d = fmbtx11.Screen(":0")
screenCount = 0

resultsPath = "../../fmbt-testresults"

pollTime = 0.5      #page change poll delay, used as delay in other actions too
                    #the more ram in testmachine the shorter pollTime can be used
                    
timeoutTime = 5.0   #max time between page loads

account = ""

stateAssets = {
                "login" : "assets/notregistered.png",
                "register" : "assets/alreadyregistered.png",
                "boardmenu" : "assets/addboard.png",
                "removeboard_dialog" : "assets/removedialog.png",
                "addboard_dialog" : "assets/create.png",
                "board" : "assets/addticket.png",
                "createticket_dialog" : "assets/apply_ticket.png",
                "editticket_dialog" : "assets/apply_ticket.png",
                "editboard_dialog" : "assets/apply.png"
               }

def rs():
    global screenCount, d
    # wipe screens
    if screenCount > 20:
        wipeScreens()
        screenCount = 0
    screenCount += 1
    return d.refreshScreenshot()

'''
init(): called before starting model testing
'''
def init():
    TypeHelper.initWords()

    global account
    if os.path.isfile('account'):
        f = open('account','r')
        account = f.readline()
    
    wipeScreens()
    if not os.path.exists(resultsPath):
        os.makedirs(resultsPath)
    d.setScreenshotDir(resultsPath)
    d.enableVisualLog(resultsPath + "/testlog.html")
    homePage()

'''
cleanup(): called after model execution has finished
'''
def cleanup():
    #cleanup stuff here (zip testresults etc.)
    return


'''
utility functions
'''
def getAccount():
    return account

def wipeScreens():
    for f in glob (resultsPath + '/*.png'):
        os.unlink (f)
    for f in glob (resultsPath + '/*.xwd'):
        os.unlink (f)

def wait(time=1.0):
    sleep(time)
    
def homePage():
    rs()
    d.connection().sendKeyDown("Alt_L")
    d.connection().sendPress("Home")
    d.connection().sendKeyUp("Alt_L")

def refreshPage():
    d.connection().sendPress("F5")
    wait()

def typeDelay(msg):
    for x in xrange(0, len(msg)):
        d.pressKey(msg[x], hold=0.05)
    
def clearText():
    wait(0.3)
    if checkHasFocus():
        d.connection().sendKeyDown('Control_L')
        wait(0.1)
        d.pressKey('a')
        wait(0.1)
        d.connection().sendKeyUp('Control_L')
        wait(0.1)
        d.pressKey('BackSpace')

def resetCursor():
    d.connection().sendTouchMove(300,10)


'''
login
'''
def clickSignin():
    rs()
    d.tapBitmap("assets/signin.png")

def clickCreateaccount():
    rs()
    d.tapBitmap("assets/notregistered.png", tapPos=(1.5,0.5))
    d.connection().sendTouchMove(300,10)

def typeLoginInfo():
    global account
    if len(account) < 3:
        return
    rs()
    d.tapBitmap("assets/email.png")
    clearText()
    typeDelay(account)
    d.tapBitmap("assets/pass.png")
    clearText()
    typeDelay(account)

def deleteAccount(): #doesn't do anything on screen but deletes a file from disk
    global account
    account = ""
    if os.path.isfile("account"):
        os.remove("account")

def checkUnauthorized():
    rs()
    result = d.verifyBitmap("assets/unauthorized.png")
    return result
    

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
    d.tapBitmap("assets/email.png")
    clearText()
    typeDelay(account)
    d.tapBitmap("assets/pass.png")
    clearText()
    typeDelay(account)
    
def clickRegister():
    rs()
    d.tapBitmap("assets/register.png")  
    
def clickLogintext():
    rs()
    d.tapBitmap("assets/alreadyregistered.png", tapPos=(1.1,0.5))
    resetCursor()
  

'''
boardmenu
'''
def clickBoard():
    s = rs()
    #random board
    d.oirEngine().addScreenshot(s)
    itemlist = d.oirEngine().findBitmap(s, "assets/crossboard.png")
    if len(itemlist) < 1:
        return
    item = random.choice(itemlist)
    x = item.coords()[0] + 50
    y = item.coords()[1] - 50
    
    d.tap((x,y))  

def clickRemoveBoard():
    s = rs()
    d.oirEngine().addScreenshot(s)
    itemlist = d.oirEngine().findBitmap(s, "assets/crossboard.png")
    if len(itemlist) < 1:
        return
    item = random.choice(itemlist)
    x = item.coords()[0]
    y = item.coords()[1]
    
    d.tap((x,y))  

def clickAddBoard():
    rs()
    d.tapBitmap("assets/addboard.png")

def clickLogout():
    rs()
    d.tapBitmap("assets/logout.png")
    homePage()
    wait(2.0)
    
def clickPublicHeading():
    rs()
    d.tapBitmap("assets/public_heading.png")

def clickPrivateHeading():
    rs()
    d.tapBitmap("assets/private_heading.png")

def scrollUp():
    coord = (d.screenSize()[0]-20, 100)
    d.tap(coord)
    d.connection().sendPress("Page_Up")

def scrollDown():
    coord = (d.screenSize()[0]-20, 100)
    d.tap(coord)
    d.connection().sendPress("Page_Down")

def checkPrivateBoard():
    #rs()
    return d.verifyBitmap("assets/private_heading.png")
    
def checkPublicBoard():
    #rs()
    return d.verifyBitmap("assets/public_heading.png")

'''
removeboard_dialog
'''
def clickRemoveBoardDialogRemove():
    rs()
    d.tapBitmap("assets/removedialog.png")
    
def clickRemoveBoardDialogCancel():
    rs()
    d.tapBitmap("assets/cancel.png")


'''
addboard_dialog
'''
def clickAddBoardDialogCreate():
    rs()
    d.tapBitmap("assets/create.png")

def clickAddBoardDialogCancel():
    rs()
    d.tapBitmap("assets/cancel.png")

def clickPublic():
    rs()
    d.tapBitmap("assets/public.png")

def clickPrivate():
    rs()
    d.tapBitmap("assets/private.png")

def typeBoardName():
    rs()
    d.tapBitmap("assets/textinput_heading.png", tapPos=(0.1,2.5))
    clearText()
    typeDelay(TypeHelper.getBoardName())

def clickCancel():
    rs()
    d.tapBitmap("assets/cancel.png")


'''
editboard
'''
def clickApply():
    rs()
    d.tapBitmap("assets/apply.png")


'''
board
'''
def clickAddTicket():
    rs()
    d.tapBitmap("assets/addticket.png")

def clickTicket():
    rs()
    d.tapBitmap("assets/editticket.png", tapPos=(-1.5, 1.0))
    wait(1.0)

def clickEdit():
    rs()
    d.tapBitmap("assets/editticket.png")
    wait(0.5)

def dragTicket():
    s = rs()
    d.oirEngine().addScreenshot(s)
    itemlist = d.oirEngine().findBitmap(s, "assets/editticket.png")
    if len(itemlist) < 1:
        return
    item = random.choice(itemlist)
    point = item.coords()
    x1 = point[0]-30
    y1 = point[1]
    
    screenSize = d.screenSize()
    x2 = random.randint(100, screenSize[0]-100)
    y2 = random.randint(100, screenSize[1]-100)
    
    d.drag((x1, y1), (x2, y2))
    resetCursor()
    
def clickSnap():
    rs()
    d.tapBitmap("assets/snap.png")

def clickRemoveTicket():
    rs()
    d.tapBitmap("assets/removeticket.png")
    
def clickWorkspace():
    rs()
    d.tapBitmap("assets/workspace.png")


'''
createticket_dialog
'''
def clickCreate():
    rs()
    d.tapBitmap("assets/create.png")

def clickCancelTicket():
    rs()
    d.tapBitmap("assets/cancel_ticket.png")

def typeTicketName():
    rs()
    d.tapBitmap("assets/textinput_heading.png", tapPos=(0.2,2.5))
    wait(0.5)
    clearText()
    typeDelay(TypeHelper.getTicketName())

def clickColor():
    i = random.randint(0,3)
    s = rs()
    d.oirEngine().addScreenshot(s)
    coordlist = d.oirEngine().findBitmap(s, "assets/color.png")
    if len(coordlist) < 1:
        return
    first = coordlist[0].coords()
    x = i*142+50+first[0]
    y = first[1]+50
    d.connection().sendTap(x, y)


'''
editticket_dialog
'''
def clickClose():
    rs()
    d.tapBitmap("assets/close.png")


def clickApplyTicket():
    rs()
    d.tapBitmap("assets/apply_ticket.png")

def typeTicketContent():
    rs()
    d.tapBitmap("assets/textinput_content.png", tapPos=(0.2,4.5))
    count = random.randint(2,5)
    i = 0
    while i < count:
        i += 1
        typeDelay(TypeHelper.getTicketContent())


'''
functions to check if elements are present on screen
'''
def checkHasFocus():
    rs()
    return d.verifyBitmap("assets/textinput_focus.png")

def checkRemoveBoard():
    rs()
    result = d.verifyBitmap("assets/crossboard.png")
    if result:
        return True
    else:
        return False

def checkBoard():
    rs()
    result = d.verifyBitmap("assets/crossboard.png")
    if result:
        return True
    else:
        return False

def checkCreate():
    rs()
    result = d.verifyBitmap("assets/create.png")
    if result:
        return True
    else:
        return False

def checkTicket():
    rs()
    result = d.verifyBitmap("assets/editticket.png")
    if result:
        return True
    else:
        return False

def checkRemoveTicket():
    rs()
    result = d.verifyBitmap("assets/removeticket.png")
    if result:
        return True
    else:
        return False

def checkUp():
    # TODO doesn't work in current version
    return False

def checkDown():
    # TODO doesn't work in current version
    return False

'''
checkState(stateToCheck):
    called when we need to verify the current state
    
    return True if state is same as param or False if not
'''
def checkState(stateToCheck):
    rs()
    if d.verifyBitmap(stateAssets[stateToCheck]):
        return True
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
    result = d.waitBitmap(stateAssets[newState], pollDelay=pollTime, waitTime=timeoutTime)
    return result
