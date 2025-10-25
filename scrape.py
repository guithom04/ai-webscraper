from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def scrape_website(website):
    print("Launching Chrome Browser")

    # ✅ ChromeDriver path — check this with: which chromedriver
    chrome_driver_path = "/usr/bin/chromedriver"

    # ✅ Chrome options
    options = Options()
    options.add_argument("--headless")   # run without GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ Launch browser
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page Loaded...")
        time.sleep(2)

        html = driver.page_source
        return html

    finally:
        driver.quit()
    
