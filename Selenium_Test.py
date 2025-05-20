import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://automationplayground.com/crm/login.html") # Test URL
time.sleep(5)

#Log in page
driver.find_element(By.ID, "email-id").send_keys("confixhub@yopmail.com")#Email text field
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("Qwerty")#Password text field
time.sleep(2)
driver.find_element(By.ID, "remember").click()#Click Remember me Button
time.sleep(2)
driver.find_element(By.ID, "submit-id").click()#Click Submit Button
time.sleep(2)
driver.find_element(By.ID, "new-customer").click()#Click Add Customer button on the landing page
time.sleep(2)

#Add Customer Form
driver.find_element(By.ID, "EmailAddress").send_keys("johndoe@yopmail.com")# input valid Email Address
time.sleep(2)
driver.find_element(By.ID, "FirstName").send_keys("John")#Input FirstName
time.sleep(2)
driver.find_element(By.ID, "LastName").send_keys("Doe")#input LastName
time.sleep(2)
driver.find_element(By.ID, "City").send_keys("Enugu")#input City
time.sleep(2)
driver.find_element(By.ID, "StateOrRegion").send_keys("Iowa")# Select an option from the 'State' drop-down
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='gender'][value='male']").click() #Select 'gender' button
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='promos-name']").click() # Click on "Add to promotional list" Button
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn-primary").click()# Click 'Submit' button
time.sleep(2)
driver.find_element(By.CLASS_NAME, "nav-link").click()# Click 'Sign out' button
time.sleep(2)
