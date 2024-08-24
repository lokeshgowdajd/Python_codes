from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

service = Service(executable_path=r"C:\Users\lokesh gowda.LAPTOP-JLPKIQ6N\Documents\driver\files\msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()
time.sleep(10)

try:

    url = "http://127.0.0.1:5000" 
    driver.get(url)
    time.sleep(5)

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')

    username_input.send_keys("admin")
    time.sleep(5)
    password_input.send_keys("secret")  
    time.sleep(5)

    login_button = driver.find_element(By.XPATH, "/html/body/form/button") 
    login_button.click()
    
    try:
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Hello, admin! You have successfully logged in.')]"))
        )
        print("Test passed: Login successful, redirected to the home page.")
    except TimeoutException:
        invalid_credentials_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Invalid credentials. Please try again.')]"))
        )
        if invalid_credentials_message:
            print("Test failed: Invalid credentials message displayed.") 

except NoSuchElementException as e:
    print(f"Test failed: Element not found - {e}")
except TimeoutException as e:
    print(f"Test failed: Timeout occurred - {e}")
finally:
    # Close the browser
    time.sleep(10)
    driver.quit()
