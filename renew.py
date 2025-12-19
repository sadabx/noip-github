import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION ---
SESSION_COOKIE = os.environ['NOIP_COOKIE']
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN') # Use .get() so it doesn't crash if missing
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Telegram secrets missing. Skipping alert.")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, json=payload)
        print("📲 Telegram notification sent!")
    except Exception as e:
        print(f"❌ Failed to send Telegram alert: {e}")

def renew():
    # Setup Invisible Browser
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print("Opening No-IP...")
        driver.get("https://www.noip.com")
        
        print("Injecting Session Cookie...")
        driver.add_cookie({
            'name': 'laravel_session',
            'value': SESSION_COOKIE,
            'domain': '.noip.com',
            'path': '/'
        })

        print("Navigating to Dashboard...")
        driver.get("https://my.noip.com/dynamic-dns")
        time.sleep(5)

        # CHECK 1: Are we logged in?
        if "login" in driver.current_url:
            raise Exception("Login failed. The cookie has likely expired.")

        # CHECK 2: Look for buttons
        print("Checking for hosts to renew...")
        confirm_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Confirm')]")
        
        if len(confirm_buttons) > 0:
            count = 0
            for btn in confirm_buttons:
                btn.click()
                count += 1
                time.sleep(2)
            
            success_msg = f"✅ Success! Renewed {count} host(s) on No-IP."
            print(success_msg)
            # Optional: Uncomment below if you want success messages too
            # send_telegram(success_msg) 
            
        else:
            print("✅ Login successful. No hosts needed renewal today.")

    except Exception as e:
        error_msg = f"⚠️ No-IP Bot Failed!\nError: {str(e)}\n\n👉 Please update your GitHub Secret 'NOIP_COOKIE' manually."
        print(error_msg)
        send_telegram(error_msg)
        raise e # Re-raise to mark the GitHub Action as 'Failed' in the UI too

    finally:
        driver.quit()

if __name__ == "__main__":
    renew()
