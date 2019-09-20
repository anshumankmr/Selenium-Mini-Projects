import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#The selenium.webdriver module provides all the 
# WebDriver implementations. Currently supported 
# WebDriver implementations are Firefox, Chrome, 
# IE and Remote. The Keys class provide keys in the 
# keyboard like RETURN, F1, ALT etc.
class PythonOrgSearch (unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://www.python.org")
		self.assertIn("Python",driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys(Keys.RETURN)
		assert "No RESULTS found " not in driver.page_source
	def tearDown(self):
		self.driver.close()
if __name__ == "__main__":
	unittest.main()
