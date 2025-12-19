import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Get secrets
SESSION_COOKIE = os.environ['NOIP_COOKIE']

def renew():
    # Setup Invisible Browser
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Fake user agent to look like a real PC
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    print("Opening No-IP...")
    # 1. Go to the domain first (needed to set cookies)
    driver.get("https://www.noip.com")
    
    # 2. Add the VIP Cookie (Updated to 'laravel_session')
    print("Injecting Session Cookie...")
    driver.add_cookie({
        'name': 'laravel_session',  # <--- CHANGED THIS TO MATCH YOUR SCREENSHOT
        'value': SESSION_COOKIE,
        'domain': '.noip.com',
        'path': '/'
    })

    # 3. Refresh to apply the cookie and go to dashboard
    print("Navigating to Dashboard...")
    driver.get("https://my.noip.com/dynamic-dns")
    time.sleep(5)

    # 4. Check if it worked
    if "login" in driver.current_url:
        print("❌ Cookie failed. Session might have expired or name is wrong.")
        driver.quit()
        return

    # 5. Look for Confirm Buttons
    print("Checking for hosts to renew...")
    try:
        confirm_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Confirm')]")
        
        if len(confirm_buttons) > 0:
            for btn in confirm_buttons:
                btn.click()
                print("✅ Confirmed a host!")
                time.sleep(2)
        else:
            print("✅ Login successful, but no hosts need confirmation today.")
            
    except Exception as e:
        print(f"Error checking hosts: {e}")

    driver.quit()
    print("Done!")

if __name__ == "__main__":
    renew()
