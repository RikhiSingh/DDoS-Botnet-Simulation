from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the webdriver
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