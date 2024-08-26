from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path=r"C:\Users\lokesh gowda.LAPTOP-JLPKIQ6N\Documents\driver\files\msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.maximize_window()
time.sleep(10)



url = "http://127.0.0.1:5000" 
driver.get(url)

axe = Axe(driver)

axe.inject()
results = axe.run()
axe.write_results(results, 'accessibility_report.json')
print(results)

driver.quit()
