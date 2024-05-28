from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open your portfolio site
driver.get('hhttps://rsxc.github.io')

# Allow the page to load
time.sleep(2)

# Locate the input box can use ID 
input_box = driver.find_element(By.ID, 'input-box-id')
input_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter text"]') 

# Type "hello" into the input box
input_box.send_keys('hello')

# Locate the button and click it (adjust the selector as necessary)
button = driver.find_element(By.ID, 'ask-raghav-button-id')  # Use the appropriate selector
button.click()

# Allow some time to observe the result
time.sleep(5)

# Close the browser
driver.quit()
