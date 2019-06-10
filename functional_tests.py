from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
         self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Open the homepage of the app
        self.browser.get('http://localhost:8000')

        #Page title and header should mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test')

        #Enter a to-do item straight away

        #Type "Buy peacock feathers" into a text box

        #Hit enter - page updates and the page now lists
        #"1: Buy peacock feathers" as an item in a to-do list

        #Text box is still present on the page 
        #Type "Use peacock feathers to make a fly"

        #Page updates again and should now show both items

        #Site has generated a unique URL for the list
        #Should be explanatory text for this.

        #When the URL is visited, the saved itesm are there.

if __name__ == '__main__':
    unittest.main()