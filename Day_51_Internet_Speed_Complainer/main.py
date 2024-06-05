import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition

chrome_driver_path = "C:\My Softwares\Chrome Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 500)
driver.get("https://www.speedtest.net/")
go = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
# driver.find_element(by=By.CSS_SELECTOR, value=".start-button a").click()
driver.execute_script("arguments[0].click();", go)

# ds = wait.until(condition.presence_of_element_located((By.CSS_SELECTOR, ".result-data .download-speed")))
time.sleep(120)
ds = driver.find_element(by=By.CSS_SELECTOR, value=".result-data .download-speed")
print(f"Here {ds.text}")

while True:
    pass
