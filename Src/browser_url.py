# browser_url.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json

def get_current_url():
    """Retrieve the current URL from the default browser."""
    # Setup Chrome WebDriver with remote debugging
    options = webdriver.ChromeOptions()
    options.add_argument('--remote-debugging-port=9222')  # Connect to the existing Chrome instance

    # Initialize WebDriver
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        # Connect to the Chrome instance using the remote debugging port
        response = requests.get('http://localhost:9222/json')
        tabs = json.loads(response.text)
        current_url = tabs[0]['url']  # Get the URL of the first tab

        print(f"Current URL: {current_url}")
        return current_url
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to test it
get_current_url()