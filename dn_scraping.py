"""
Created on Fri Sep  6 15:44:08 2024

@author: Viola
"""
# It may doesn't work becouse the website has been updated
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


# Initialize web driver
chrome_options=Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.ilgiornale.it/')


# Wait until the cookie consent button is visible and clickable, then click it
cookie_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]/span'))
)
cookie_button.click()

# Wait until the pop-up is visible 
modal = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-container"]'))
)

# Find the element you want to click on 
dismiss_button = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
dismiss_button.click()

# Scroll down by 1000 pixels
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)  # Give time for the page to scroll

# Wait for the next element to be clickable after scrolling
article_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/section[2]/div/section[1]/div/article/div/div[1]/div[2]/a'))
)
article_link.click()

# Find the find button and click on it
find_button=driver.find_element(By.XPATH,'//*[@id="header-website"]/div[1]/div[2]/div[3]/button[1]/i')
find_button.click()

# Type on the search bar and send
search=driver.find_element(By.XPATH, '//*[@id="header-website"]/div[1]/div[3]/div[1]/form/input')
search.send_keys('Brescia')
search.send_keys(Keys.ENTER)

# Scroll down by 1000 pixels
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)  # Give time for the page to scroll

# Find the find button and click on it
find_video=driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div[3]/div/article[6]/a/picture/span')
find_video.click()

# Close the driver after you're done
 driver.quit()
