import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://automationplayground.com/crm/login.html")
time.sleep(5)

driver.find_element(By.ID, "email-id").send_keys("confixhub@yopmail.com")
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("Qwerty")
time.sleep(5)
driver.find_element(By.ID, "remember").click()
time.sleep(5)
driver.find_element(By.ID, "submit-id").click()
time.sleep(5)
driver.find_element(By.ID, "new-customer").click()
time.sleep(5)
driver.find_element(By.ID, "EmailAddress").send_keys("johndoe@yopmail.com")
time.sleep(5)
driver.find_element(By.ID, "FirstName").send_keys("John")
time.sleep(5)
driver.find_element(By.ID, "LastName").send_keys("Doe")
time.sleep(5)
driver.find_element(By.ID, "City").send_keys("Enugu")
time.sleep(5)
driver.find_element(By.ID, "StateOrRegion").send_keys("Iowa")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name='gender'][value='male']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name='promos-name']").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "nav-link").click()
time.sleep(5)
