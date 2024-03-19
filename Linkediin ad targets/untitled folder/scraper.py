import os
import certifi
import undetected_chromedriver as uc

def open_google():
    # Set the environment variable for SSL certificate
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

    # Setup undetected ChromeDriver
    options = uc.ChromeOptions()
    options.add_argument('--headless')  # Run in background if needed
    driver = uc.Chrome(options=options)

    # Open Google
    driver.get("https://www.google.com")

    # Print the title of the page
    print("Title of the page is:", driver.title)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    open_google()
