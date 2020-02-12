import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Single_Radio_Button(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_single_radio_button_male(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "radio-inline", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        assert python_button.is_selected() is True

    def test_single_radio_button_female(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        assert python_button.is_selected() is True

    def test_single_radio_button_male_2(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "radio-inline", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_id('buttoncheck')
        python_button2.click()
        assert "Radio button 'Male' is checked" in driver.page_source

    def test_single_radio_button_female_2(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_id('buttoncheck')
        python_button2.click()
        assert "Radio button 'Female' is checked" in driver.page_source

    def tearDown(self):
        self.driver.close()

class Multiple_Radio_Button(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_group_radio_button_male(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        assert "Male" in driver.page_source

    def test_group_radio_button_female(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        assert "Female" in driver.page_source


    def test_group_radio_button_male_0_to_5(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button2.click()
        assert python_button.is_selected() is True
        assert python_button2.is_selected() is True

    def test_group_radio_button_male_0_to_5_getvalue(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button2.click()
        python_button3 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        python_button3.click()
        assert "Sex : Male" in driver.page_source
        assert "Age group: 0 - 5" in driver.page_source

    def test_group_radio_button_male_5_to_15(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button2.click()
        assert python_button.is_selected() is True
        assert python_button2.is_selected() is True

    def test_group_radio_button_male_5_to_15_getvalue(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button2.click()
        python_button3 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        python_button3.click()
        assert "Sex : Male" in driver.page_source
        assert "Age group: 5 - 15" in driver.page_source

    def test_group_radio_button_male_15_to_50(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "radio-inline", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//input')
        python_button2.click()
        assert python_button.is_selected() is True
        assert python_button2.is_selected() is True

    def test_group_radio_button_male_15_to_50_getvalue(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "radio-inline", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//input')
        python_button2.click()
        python_button3 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        python_button3.click()
        assert "Sex : Male" in driver.page_source
        assert "Age group: 15 - 50" in driver.page_source

    def test_group_radio_button_female_0_to_5(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button2.click()
        assert python_button.is_selected() is True
        assert python_button2.is_selected() is True

    def test_group_radio_button_female_0_to_5_getvalue(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        python_button2.click()
        python_button3 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        python_button3.click()
        assert "Sex : Female" in driver.page_source
        assert "Age group: 0 - 5" in driver.page_source

    def test_group_radio_button_female_5_to_15(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button2.click()
        assert python_button.is_selected() is True
        assert python_button2.is_selected() is True

    def test_group_radio_button_female_5_to_15_getvalue(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//div[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button2.click()
        python_button3 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        python_button3.click()
        assert "Sex : Female" in driver.page_source
        assert "Age group: 5 - 15" in driver.page_source

    def test_group_radio_button_female_15_to_50(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "radio-inline", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//input')
        python_button2.click()
        assert python_button.is_selected() is True
        assert python_button2.is_selected() is True

    def test_group_radio_button_female_15_to_50_getvalue(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
        self.assertIn('Selenium', driver.title)
        python_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-body", " " ))]//div[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//input')
        python_button.click()
        python_button2 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "radio-inline", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//input')
        python_button2.click()
        python_button3 = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
        python_button3.click()
        assert "Sex : Female" in driver.page_source
        assert "Age group: 15 - 50" in driver.page_source

    def tearDown(self):
        self.driver.close()
    

if __name__ == "__main__":
    unittest.main()