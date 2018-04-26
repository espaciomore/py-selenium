class PageObject(object):

	def __init__(self, driver):
		self._driver = driver

	def close(self):
		self._driver.close()
