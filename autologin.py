from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('http://netaccess.iitm.ac.in/account/login')
username = driver.find_element(By.ID, 'username')
username.send_keys('CS22B088')
password = driver.find_element(By.ID, 'password')
password.send_keys('h["V-9Gl.4{')
password.submit()
driver.get('https://netaccess.iitm.ac.in/account/approve')
button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/label/input")
button.click()
button = driver.find_element("id", 'approveBtn')
button.click()
time.sleep(3)
driver.quit()