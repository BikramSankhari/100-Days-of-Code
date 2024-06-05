from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\My Softwares\Chrome Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")
store = driver.find_element(by=By.ID, value="store")

while True:
    cookie.click()
# game_end = time() + 60
#
# while time() < game_end:
#     end = time() + 5
#     while time() < end:
#         cookie.click()
#
#     store_items = store.find_elements(by=By.CSS_SELECTOR, value="div")
#     store_items.reverse()
#     for item in store_items:
#         try:
#             if item.get_attribute("class") != "grayed":
#                 item.click()
#                 break
#         except:
#             continue

driver.quit()
