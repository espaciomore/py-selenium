import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from wikipedia_page import WikipediaPage

class WikipediaTest(unittest.TestCase):

	page = None

	def setUp(self):
		driver = webdriver.Chrome()
		self.page = WikipediaPage(driver=driver)
		self.page.get()

	def test_search_wikipedia(self):
		self.page.linkEnglish().click()
		self.page.inputSearch().send_keys("Python" + Keys.RETURN)
		self.page.linkPython().click()
		assert "Python (programming language)" in self.page.titlePython().text

	def tearDown(self):
		self.page.close()

if __name__ == "__main__":
    unittest.main()