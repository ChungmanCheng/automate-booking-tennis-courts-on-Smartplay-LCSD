from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Get login credentials from .env
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0"
BOOKING_URL = "https://www.smartplay.lcsd.gov.hk/home"

def book_tennis_court():
    # Set up Firefox options
    firefox_options = Options()
    firefox_options.set_preference("general.useragent.override", USER_AGENT)
    firefox_options.set_preference("dom.webdriver.enabled", False)  # Disable automation flags
    
    # Specify the path to the GeckoDriver (replace with your correct path)
    webdriver_service = Service(executable_path='/usr/bin/geckodriver')  # Change this to the correct path
    
    # Initialize the WebDriver with Firefox
    driver = webdriver.Firefox(service=webdriver_service, options=firefox_options)

    try:
        # Go to the Smartplay booking page
        driver.get(BOOKING_URL)
        print("Opened website...")

        # Fill in login details
        driver.find_element(By.NAME, "pc-login-username").send_keys(USERNAME)
        driver.find_element(By.NAME, "pc-login-password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//div[@name='pc-login-btn']//div[@role='button']").click()

        # Wait for the '關閉' button to be clickable
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='關閉']"))
        )
        while close_button:
            close_button.click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@name='pc-login-btn']//div[@role='button']"))
            ).click()
            close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='關閉']")))

        # Navigate to booking section
        # driver.find_element(By.XPATH, "//li[@role='button']//span[text()='設施']").click()

        # Select tennis court option
        # driver.find_element(By.XPATH, "//a[text()='Tennis Court']").click()

        # Select date and search (adjust selectors based on the site)
        # driver.find_element(By.ID, "date-picker").send_keys("2025-01-30")
        # driver.find_element(By.ID, "search").click()

        # Book available slot
        # driver.find_element(By.XPATH, "//button[text()='Book Now']").click()

        print("Booking completed!")

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()

# Run the function
if __name__ == "__main__":
    book_tennis_court()
