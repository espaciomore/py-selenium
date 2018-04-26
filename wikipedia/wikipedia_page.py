from page_object import PageObject

from page_factory_support import cacheable, callable_find_by as find_by

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaPage(PageObject):

	linkEnglish = find_by(By.ID, "js-link-box-en")
	inputSearch = find_by(id_="searchInput")
	linkPython = find_by(link_text="Python (programming language)")
	titlePython = find_by(xpath="//h1[text()='Python (programming language)']")

	def get(self):
		self._driver.get("https://www.wikipedia.org/")
		WebDriverWait(self._driver, 10).until( EC.title_is("Wikipedia") )