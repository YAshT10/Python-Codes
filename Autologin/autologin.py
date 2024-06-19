from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
print("Enter your Username")
usr=input()
print("Enter your Password")
pwd=input()
driver.get('http://netaccess.iitm.ac.in/account/login')
username = driver.find_element(By.ID, 'username')
username.send_keys(usr)#username
password = driver.find_element(By.ID, 'password')
password.send_keys(pwd)#passcode
password.submit()
driver.get('https://netaccess.iitm.ac.in/account/approve')
button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/div[2]/label/input")
button.click()
button = driver.find_element("id", 'approveBtn')
button.click()
time.sleep(3)
driver.quit()
