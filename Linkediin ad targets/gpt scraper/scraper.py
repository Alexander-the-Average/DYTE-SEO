from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time


def open_google():
    # Setup undetected ChromeDriver
    options = uc.ChromeOptions()
    options.add_argument('--headless')  # Run in background if needed
    driver = uc.Chrome(options=options)

    # Open Google
    driver.get("https://www.google.com")

    # Print the title of the page
    print("Title of the page is:", driver.title)
    time.sleep(100)
    

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    open_google()
