import os
import random
from time import sleep, time, strftime, gmtime
from glob import glob

from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, text/csv, application/octet-stream, text/json, application/vnd.ms-excel, text/comma-separated-values")


driver = webdriver.Firefox(firefox_profile=fp)

#url = 'http://sut-cb.n4sjamk.org'
url = 'localhost:8000'
driver.get(url)

#globals

screenCount = 0

resultsPath = "../../fmbt_testresults"

pollTime = 0.3

timeoutTime = 2.0

email = "testbaboon@test.com"
password = "t3stmonkey"

custombackground = "http://bit.ly/1cMN0rG"

stateAssets = {
	"login" 	: ["//input[@value='Login']"],
	"register" 	: ["//input[@value='Register']"],
	"boardmenu" : ["//div[@class='view view-workspace']"],
	"board" 	: ["//div[@class='board']"],
	"board_edit_dialog" 	: ["//form[@class='dialog dialog-edit-board']"],
	"delete_board_dialog" 	: ["//form[@class='dialog dialog-remove-board']"],
	"export_dialog" 	: ["//form[@class='dialog dialog-edit-board']"],
	"share_dialog" 	: ["//button[@class='btn-secondary']"],
	"shared_dialog" 	: ["//button[@class='btn-neutral']"],
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
	driver.set_window_size(1920, 1200)
	driver.maximize_window()

def reinitDriver():
	global driver
	driver.quit()
	driver = webdriver.Firefox()
	driver.get(url)
	driver.set_window_size(1920, 1200)
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
	driver.find_element_by_xpath("//input[@type='email']").clear()
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
	driver.find_element_by_xpath("//input[@type='email']").clear()
	driver.find_element_by_xpath("//input[@type='email']").send_keys(email)

def typeRegisterPassword():
	rs()
	driver.find_element_by_xpath("//input[@type='password']").send_keys(password)

def typePasswordAgain():
	rs()
	driver.find_element_by_xpath("//input[@name='passwordAgain']").send_keys(password)

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
	if isElement("//span[@class='fa fa-fw fa-pencil']"):
		editboards = driver.find_elements_by_xpath("//span[@class='fa fa-fw fa-pencil']")
		random.choice(editboards).click()
		wait()

def deleteBoard():
	rs()
	if isElement("//span[@class='fa fa-fw fa-trash']"):
		trashboards = driver.find_elements_by_xpath("//span[@class='fa fa-fw fa-trash']")
		random.choice(trashboards).click()
		wait()

def openBoard():
	rs()
	if isElement("//div[@class='minimap']"):
		boards = driver.find_elements_by_xpath("//div[@class='minimap']")
		random.choice(boards).click()
		wait()

#board

def createTicket():
	rs()
	board = driver.find_element_by_xpath("//div[@class='board']")
	AC(driver).double_click(board).perform()
	wait()

def editTicket():
	rs()
	if isElement("//div[@class='ticket']"):
		tickets = driver.find_elements_by_xpath("//div[@class='ticket']")
		ticket = random.choice(tickets)
		AC(driver).double_click(ticket).perform()
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
	driver.find_element_by_xpath("//span[@class='fa fa-fw fa-globe']").click()
	wait()

def moveTicket():
	rs()
	tickets = driver.find_elements_by_xpath("//div[@class='ticket']")
		
	if len(tickets)<1:
		return
	ticket = random.choice(tickets)

	board = driver.find_element_by_xpath("//div[@class='board']")
	xdest = random.randint(0, board.size.get('width') - ticket.size.get('width'))
	ydest = random.randint(0, board.size.get('height') - ticket.size.get('height'))
	AC(driver).click_and_hold(ticket).move_to_element_with_offset(board, xdest, ydest).release(ticket).perform()
	wait()

#boardedit

def clickDone():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-primary']").click()
	wait()

def typeBoardName():
	rs()
	driver.find_element_by_xpath("//input[@placeholder='Board Name']").clear()
	driver.find_element_by_xpath("//input[@placeholder='Board Name']").send_keys("Boardname")
	wait()

def increaseWidth():
	rs()
	width = driver.find_element_by_xpath("//input[@placeholder='Board Width']").get_attribute("value")
	if width < 10:
		driver.find_element_by_xpath("//input[@placeholder='Board Width']").send_keys(Keys.ARROW_UP)
		wait()

def increaseHeight():
	rs()
	height = driver.find_element_by_xpath("//input[@placeholder='Board Height']").get_attribute("value")
	if height < 10:
		driver.find_element_by_xpath("//input[@placeholder='Board Height']").send_keys(Keys.ARROW_UP)
		wait()

def decreaseWidth():
	rs()
	width = driver.find_element_by_xpath("//input[@placeholder='Board Width']").get_attribute("value")
	if width > 1:
		driver.find_element_by_xpath("//input[@placeholder='Board Width']").send_keys(Keys.ARROW_DOWN)
		wait()

def decreaseHeight():
	rs()
	height = driver.find_element_by_xpath("//input[@placeholder='Board Height']").get_attribute("value")
	if height > 1:
		driver.find_element_by_xpath("//input[@placeholder='Board Height']").send_keys(Keys.ARROW_DOWN)
		wait()

def selectEmptyBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("NONE")
	wait()

def selectCustomBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("CUSTOM")
	driver.find_element_by_xpath("//input[@placeholder='URL']").clear()
	driver.find_element_by_xpath("//input[@placeholder='URL']").send_keys(custombackground)
	wait()

def selectPlayBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("PLAY")
	wait()

def selectSwotBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("SWOT")
	wait()

def selectScrumBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("SCRUM")
	wait()

def selectKanbanBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("KANBAN")
	wait()

def selectKeendroptryBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("KEEP_DROP_TRY")
	wait()

def selectCustomerjourneymapBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("CUSTOMER_JOURNEY_MAP")
	wait()

def selectBusinessmodelcanvasBackground():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("BUSINESS_MODEL_CANVAS")
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
	for csv in glob ("/home/*/Downloads/board*.csv"):
		os.remove(csv)
	for txt in glob ("/home/*/Downloads/board*.txt"):
		os.remove(txt)
	for json in glob ("/home/*/Downloads/board*.json"):
		os.remove(json)
	wait()

def clickExport():
	rs()
	driver.find_element_by_xpath("//a[@class='btn btn-secondary']").click()
	wait()

def selectCsvExport():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("csv")
	wait()

def selectJsonExport():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("json")
	wait()

def selectPlaintextExport():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("plaintext")
	wait()

def selectImageExport():
	rs()
	select = Select(driver.find_element_by_xpath("//select"))
	select.select_by_value("image")
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

#shared

def clickDoneShared():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-primary']").click()
	wait()

def clickHide():
	rs()
	driver.find_element_by_xpath("//button[@class='btn-neutral']").click()
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
	driver.find_element_by_xpath("//textarea").clear()
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

# checks

def checkTicket():
    rs()
    result = isElement("//div[@class='ticket']")
    if result:
        return True
    else:
        return False

def checkBoard():
	rs()
	result = isElement("//div[@class='minimap']")
	if result:
		return True
	else:
		return False


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