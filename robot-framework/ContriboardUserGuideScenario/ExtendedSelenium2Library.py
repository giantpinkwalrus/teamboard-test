from Selenium2Library import Selenium2Library

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Selenium2Library import utils
from Selenium2Library.locators import ElementFinder

class ExtendedSelenium2Library(Selenium2Library):

	def double_click_element_at_coordinates(self, locator, xoffset, yoffset):
		self._info("Double clicking element '%s' in coordinates '%s', '%s'." % (locator, xoffset, yoffset))
		element = self._element_find(locator, True, True)
		ActionChains(self._current_browser()).move_to_element(element).move_by_offset(xoffset, yoffset).double_click().perform()

	def get_markdown_text_from_file(self, locator):
		with open('markdown.txt') as f:
			content = f.readlines()
			self._info("Typing text '%s' into text field '%s'" % ("from file", locator))
			self._input_text_into_text_field(locator, content)