import os
import random
from time import sleep, time, strftime, gmtime
from glob import glob

from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

url = 'localhost:8000'
driver.get(url)

#globals

screenCount = 0

resultsPath = "../../fmbt_testresults"

pollTime = 0.3

timeout = 2.0

email = "testbaboon@test.com"
password = "t3stmonkey"

account = (email)+(password)

stateAssets = {
	"login" 	: ["//input[@value='Login']"],
	"register" 	: ["//input[@value='Register']"],
	"boardmenu" : ["//div[@class='view view-workspace']"],
	"board" 	: ["//div[@class='board']"],
	"board_edit_dialog" 	: ["//form[@class='dialog dialog-edit-board']"],
	"delete_board_dialog" 	: ["//form[@class='dialog dialog-remove-board']"],
	"export_dialog" 	: ["//form[@class='dialog dialog-edit-board']"],
	"share_dialog" 	: ["//form[@class='dialog dialog-edit-board']"],
	"ticket_edit_dialog" 	: ["//form[@class='dialog edit-ticket-dialog']"]
}

def rs():
	global screenCount
	if screenCount >20:
		wipeScreens ()
		screenCount = 0
	screenCount += 1
	stamp = strftime("%Y-%m%d_%H-%M-%S", gmtime())
	driver.save_screenshot(resultsPath + "/"+stamp+".png")

def wipeScreens():
    for f in glob (resultsPath + '/*.png'):
        os.unlink (f)
    for f in glob (resultsPath + '/*.xwd'):
        os.unlink (f)

def init():
	driver.maximize_window()

def reinitDriver():
	global driver
	driver.quit()
	driver = webdriver.Firefox()
	driver.get(url)
	driver.maximize_window()

def cleanup():
	return

#utility funtions

def isElement(xpath):
	try:
		if driver.find_element_by_xpath(xpath).is_displayed():
			return True
		else:
			return False
	except:
		return False

def checkAlert():
	try:
		WebDriverWait(driver,pollTime).until(EC.alert_is_present())
		if Ec.alert_is_present() == False:
			return False
		else:
			return True
	except:
		return False

def confirmAlert():
		if checkAlert():
				Alert(driver).accept()

def getAccount():
	return account

def wait(time=pollTime):
	sleep(time)

def homePage():
	rs()
	driver.get(url)

def refreshPage():
	driver.refresh()

def clearText():
	return

def resetCursor():
	return

#login

def clickLogin():
	rs()
	driver.find_element_by_xpath("//input[@class='btn-primary']").click()
	wait()

def clickCreateAccount():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-secondary']").click()
	wait()

def typeEmail():
	rs()
	driver.find_element_by_xpath("//input[@type='email']").send_keys(email)

def typePassword():
	rs()
	driver.find_element_by_xpath("//input[@type='password']").send_keys(password)

#register

def clickRegister():
	rs()
	driver.find_element_by_xpath("//input[@class='btn-primary']").click()
	wait()

def clickLoginAccount():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-secondary']").click()
	wait()

def typeRegisterEmail():

	rs()
	driver.find_element_by_xpath("//input[@type='email']").send_keys(email)

def typeRegisterPassword():
	rs()
	driver.find_element_by_xpath("//input[@type='password']").send_keys(password)

#boardmenu

def clickLogout():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-user']").click()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-sign-out']").click()
	wait()

def createBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-plus']").click()
	wait()

def editBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-pencil']").click()
	wait()

def deleteBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-trash']").click()
	wait()

def openBoard():
	rs()
	driver.find_element_by_xpath("//div[@class='minimap']").click()
	wait()

#board

def createTicket():
	rs()
	driver.find_element_by_xpath("//div[@class='board']").click()
	wait()

def editTicket():
	rs()
	driver.find_element_by_xpath("//div[@class='ticket']").click()
	wait()

def closeBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-arrow-left']").click()
	wait()

def editBoardFromBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-pencil']").click()
	wait()

def exportBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-download']").click()
	wait()

def shareBoard():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-share-alt']").click()
	wait()

def clickMagnet():
	rs()
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-magnet']").click()
	wait()

def clickGlobe():
	rs()
	driver.find_element_by_xpath("//span[@class=)'fa fa-fw fa-globe']").click()
	wait()

def moveTicket():
	rs()
	driver.find_element_by_xpath("//div[@class='ticket']").click()
	wait()

#boardedit

def clickDone():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-primary']").click()
	wait()

def typeBoardName():
	rs()
	driver.find_element_by_xpath("//input[@placeholder='Board Name']").send_keys("boardname")
	wait()

def typeWidth():
	rs()
	driver.find_element_by_xpath("//input[@placeholder='Board Width']").send_keys("10")
	wait()

def typeHeight():
	rs()
	driver.find_element_by_xpath("//input[@placeholder='Board Height']").send_keys("10")
	wait()

def selectBackground():
	rs()
	driver.find_element_by_xpath("//select").click()
	driver.find_element_by_xpath("//option[@value='KANBAN']").click
	wait()

#deleteboard

def confirmDelete():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-danger']").click()
	wait()

def cancelDelete():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-neutral']").click()
	wait()

#export

def clickDoneExport():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-primary']").click()
	wait()

def clickExport():
	rs()
	driver.find_element_by_xpath("a[@class='btn btn-secondary']").click()
	wait()

def selectExport():
	rs()
	driver.find_element_by_xpath("//select").click()
	driver.find_element_by_xpath("//option[@value='JSON']").click()
	wait()

#share

def clickDoneShare():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-primary']").click()
	wait()

def clickShare():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-secondary']").click()
	wait()

#ticketedit


def clickRed():
	rs()
	driver.find_element_by_xpath("//div[@style='background-color:#eb584a;']").click()
	wait()

def clickBlue():
	rs()
	driver.find_element_by_xpath("//div[@style='background-color:#4f819a;']").click()
	wait()

def clickPurple():
	rs()
	driver.find_element_by_xpath("//div[@style='background-color:#724a7f;']").click()
	wait()

def clickYellow():
	rs()
	driver.find_element_by_xpath("//div[@style='background-color:#dcc75b;']").click()
	wait()

def typeTicket():
	rs()
	driver.find_element_by_xpath("//textarea").send_keys("ticket")
	wait()

def deleteTicket():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-danger']").click()
	wait()

def ticketDone():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-primary']").click()
	wait()


#State check

def checkState(stateToCheck):
    rs()
    element = stateAssets[stateToCheck][0]
    try:
        if isElement(element):
            return True
    except:
        return False
        
    return False