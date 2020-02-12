import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Single_Input_Field(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_single_input_field(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("user-message")
        elem.clear()
        elem.send_keys("Here is a test message1234567890!@#$%^&*()")
        assert "" in driver.page_source

    def tearDown(self):
        self.driver.close()


class Double_Input_Field(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_two_input_field_one_number_1(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("sum1")
        elem.clear()
        elem.send_keys('1')
        elem2 = driver.find_element_by_id("sum2")
        elem2.clear()
        elem2.send_keys('')
        assert "" in driver.page_source

    def test_two_input_field_one_number_2(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("sum1")
        elem.clear()
        elem.send_keys('')
        elem2 = driver.find_element_by_id("sum2")
        elem2.clear()
        elem2.send_keys('1')
        assert "" in driver.page_source

    def test_two_input_field_two_numbers_plus(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("sum1")
        elem.clear()
        elem.send_keys('2')
        elem2 = driver.find_element_by_id("sum2")
        elem2.clear()
        elem2.send_keys('2')
        assert "4" in driver.page_source

    def test_two_input_field_two_numbers_plus_negative(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("sum1")
        elem.clear()
        elem.send_keys('0')
        elem2 = driver.find_element_by_id("sum2")
        elem2.clear()
        elem2.send_keys('-2')
        assert "-2" in driver.page_source

    def test_two_input_field_two_numbers_negative_negative(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("sum1")
        elem.clear()
        elem.send_keys('-2')
        elem2 = driver.find_element_by_id("sum2")
        elem2.clear()
        elem2.send_keys('-2')
        assert "-4" in driver.page_source

    def test_two_input_field_two_letters(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_id("sum1")
        elem.clear()
        elem.send_keys('a')
        elem2 = driver.find_element_by_id("sum2")
        elem2.clear()
        elem2.send_keys('b')
        assert "" in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()