import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Input_Form(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_input(self):
        driver = self.driver
        driver.get('https://www.seleniumeasy.com/test/input-form-demo.html')
        self.assertIn('Selenium', driver.title)
        elem = driver.find_element_by_name('first_name')
        elem.clear()
        elem.send_keys('First Name Tester')

        elem2 = driver.find_element_by_name('last_name')
        elem2.clear()
        elem2.send_keys('Last Name Tester')

        elem3 = driver.find_element_by_name('email')
        elem3.clear()
        elem3.send_keys('testemail@email.com')

        elem4 = driver.find_element_by_name('phone')
        elem4.clear()
        elem4.send_keys('123 456 6543')

        elem5 = driver.find_element_by_name('address')
        elem5.clear()
        elem5.send_keys('my home address')

        elem6 = driver.find_element_by_name('city')
        elem6.clear()
        elem6.send_keys('my city')

        python_button = Select(driver.find_element_by_name('state'))
        python_button.select_by_visible_text('Alabama')

        elem6 = driver.find_element_by_name('zip')
        elem6.clear()
        elem6.send_keys('12345')

        elem7 = driver.find_element_by_name('website')
        elem7.clear()
        elem7.send_keys('mywebsite.com')

        radio_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "radio", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//input')
        radio_button.click()

        comments = driver.find_element_by_name('comment')
        comments.clear()
        comments.send_keys('Here are all my comments I would like to submit')

        submit_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " ))]')
        submit_button.click()
        
if __name__ == "__main__":
    unittest.main()