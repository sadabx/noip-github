import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Get secrets from GitHub Environment
USERNAME = os.environ['NOIP_USERNAME']
PASSWORD = os.environ['NOIP_PASSWORD']

def renew():
    # Setup Headless Chrome (Invisible Browser)
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    print("Opening No-IP...")
    driver.get("https://www.noip.com/login")
    time.sleep(3)

    # Login Process
    print("Logging in...")
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    
    # Find and click the Login button
    # Note: Class names might change, using generic selector usually works best
    login_btn = driver.find_element(By.ID, "clogs-captcha-button")
    login_btn.click()
    time.sleep(5)

    # Check for "Confirm" buttons
    # No-IP usually shows a specific "Confirm" button for expiring hosts
    print("Checking for hosts to renew...")
    driver.get("https://my.noip.com/dynamic-dns")
    time.sleep(5)

    try:
        # This selector looks for the specific "Confirm" button No-IP uses
        # Note: If no hosts are expiring, this button won't exist, which is fine.
        confirm_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Confirm')]")
        
        if len(confirm_buttons) > 0:
            for btn in confirm_buttons:
                btn.click()
                print("Confirmed a host!")
                time.sleep(2)
        else:
            print("No hosts need confirmation today.")
            
    except Exception as e:
        print(f"Error checking hosts: {e}")

    driver.quit()
    print("Done!")

if __name__ == "__main__":
    renew()
