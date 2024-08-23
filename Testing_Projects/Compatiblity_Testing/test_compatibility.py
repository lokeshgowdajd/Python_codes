from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestCompatibility(unittest.TestCase):

    def setUp(self):
        # Define the browsers to test
        self.browsers = {
            'chrome': lambda: webdriver.Chrome(options=self.get_chrome_options()),
            'firefox': lambda: webdriver.Firefox(options=self.get_firefox_options()),
            'edge': lambda: webdriver.Edge(options=self.get_edge_options()),       
            # Add other browsers if needed
        }
        self.url = "http://127.0.0.1:8080"  # Replace with your web application's URL

    def get_chrome_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return options

    def get_firefox_options(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        return options

    def get_edge_options(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        return options
    

    def test_compatibility(self):
        for browser_name, browser_class in self.browsers.items():
            with self.subTest(browser=browser_name):
                print(f"Running test on {browser_name}")
                driver = browser_class()
                time.sleep(5)  # Increased delay to ensure the server is ready
                driver.get(self.url)
                try:
                    # Print the page source for debugging
                    print(driver.page_source)
                    # Perform some basic checks
                    self.assertIn("Welcome to the Home Page!", driver.page_source)
                finally:
                    time.sleep(20)
                    driver.quit()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
