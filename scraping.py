import requests
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd  # Import pandas for DataFrame

sys.stdout.reconfigure(encoding='utf-8')

# Initialize the webdriver
driver = webdriver.Chrome()

# Base URL for the pages
base_url = "https://app.turath.io/book/86"

# Open a file to save all texts
with open('quran_texts.txt', 'w', encoding='utf-8') as file:
    for page_number in range(19, 22):  # Adjust the range as needed
        page_id = f"pg-{page_number}"
        driver.get(base_url)

        # Wait until the page with the specific ID is loaded
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, page_id)))

        # Get the page source and parse it
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')

        # Find the div with the specific ID
        page_div = soup.find('div', {'id': page_id})

        # Check if the div exists
        if page_div:
            text = page_div.text.strip()
            word_count = len(text.split())
            
            # Save text only if it contains at least 8 words
            if word_count >= 8:
                file.write(f"Page {page_number}\n")
                file.write(text + "\n\n")
            else:
                file.write(f"Page {page_number} has less than 8 words\n\n")
        else:
            file.write(f"Page {page_number} not found\n\n")

# Close the driver
driver.quit()


































       