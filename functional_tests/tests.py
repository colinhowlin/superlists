from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
         self.browser.quit()
         
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
                
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Open the homepage of the app
        self.browser.get(self.live_server_url)

        #Page title and header should mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        #Enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #Type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        #Hit enter - page updates and the page now lists
        #"1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Buy peacock feathers')
        
        #Text box is still present on the page 
        #Type "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        #Page updates again and should now show both items
        self.wait_for_row_in_list_table('1. Buy peacock feathers')
        self.wait_for_row_in_list_table('2. Use peacock feathers to make a fly')

        #Site has generated a unique URL for the list
        #Should be explanatory text for this.
        self.fail('finish the test!')

        #When the URL is visited, the saved items are there.
