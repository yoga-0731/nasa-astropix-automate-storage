from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from datetime import datetime

FILEPATH = os.environ.get('FILEPATH')

# PARENT_DIRECTORY = os.environ.get('PARENT_DIR')
# NEW_DIRECTORY = "NASA Astropix"
# path = os.path.join(PARENT_DIRECTORY, NEW_DIRECTORY)
# os.mkdir(path)

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # Added to prevent closing of browser
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://apod.nasa.gov/apod/astropix.html")
image_of_the_day = driver.find_element(By.XPATH, '/html/body/center[1]/p[2]/a/img').get_attribute('src')
data = requests.get(image_of_the_day).content

with open(fr"{FILEPATH}\{datetime.today().date()}.png", mode="wb") as file:
    file.write(data)

driver.quit()
