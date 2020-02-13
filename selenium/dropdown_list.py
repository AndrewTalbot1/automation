import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Dropdown_List_Field_days_in_a_week(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_sunday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Sunday')
        assert 'Day selected :- Sunday' in driver.page_source

    def test_monday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Monday')
        assert 'Day selected :- Monday' in driver.page_source

    def test_tuesday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Tuesday')
        assert 'Day selected :- Tuesday' in driver.page_source

    def test_wednesday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Wednesday')
        assert 'Day selected :- Wednesday' in driver.page_source

    def test_thursday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Thursday')
        assert 'Day selected :- Thursday' in driver.page_source

    def test_friday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Friday')
        assert 'Day selected :- Friday' in driver.page_source

    def test_saturday(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = Select(driver.find_element_by_id('select-demo'))
        python_button.select_by_visible_text('Saturday')
        assert 'Day selected :- Saturday' in driver.page_source

    def tearDown(self):
        self.driver.close()

class Multi_Select_List(unittest.TestCase):

    pass

    if __name__ == "__main__":
        unittest.main()


