import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Single_Checkbox_Field(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_single_checkbox_field(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_id('isAgeSelected')
        python_button.click()
        assert "Success" in driver.page_source

    def tearDown(self):
        self.driver.close()

class Multiple_checkbox_Field(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_multiple_checkbox_field_1(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "cb1-element", " " ))]')
        python_button.click()
        assert python_button.is_selected() is True

    def test_multiple_checkbox_field_2(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "cb1-element", " " ))]')
        python_button.click()
        assert python_button.is_selected() is True

    def test_multiple_checkbox_field_3(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "checkbox", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "cb1-element", " " ))]')
        python_button.click()
        assert python_button.is_selected() is True

    def test_multiple_checkbox_field_4(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "cb1-element", " " ))]')
        python_button.click()
        assert python_button.is_selected() is True

    def test_multiple_checkbox_field_Check_all(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_id('check1')
        python_button.click()
        assert "true" in driver.page_source

    def test_multiple_checkbox_field_Uncheck_all(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_id('check1')
        python_button.click()
        python_button = driver.find_element_by_id('check1')
        python_button.click()
        assert "false" in driver.page_source

    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    unittest.main()