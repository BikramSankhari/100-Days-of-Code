from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\My Softwares\Chrome Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://in.linkedin.com/")
driver.maximize_window()
email = driver.find_element(by=By.NAME, value="session_key")
email.click()
email.send_keys("popww619@gmail.com")

password = driver.find_element(by=By.NAME, value="session_password")
password.click()
password.send_keys("linkeDin@1234")

submit_button = driver.find_element(by=By.CLASS_NAME, value="sign-in-form__submit-btn--full-width")
submit_button.click()

driver.find_element(by=By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a').click()

search_box = driver.find_element(by=By.CSS_SELECTOR, value="#global-nav-search input")
search_box.click()
search_box.send_keys("Python Developer")
search_box.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div/button').click()
while True:
    pass
driver.quit()