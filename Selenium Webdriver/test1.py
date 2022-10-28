from tkinter import Button
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

events_list = {}

CHROME_DRIVER_PATH = "C:/Users/bkoro/OneDrive/Documents/Repos/Python_Programs/Dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME,  "fName")
fname.send_keys("Banny")
lname = driver.find_element(By.NAME,  "lName")
lname.send_keys("Roj")
e_mail = driver.find_element(By.NAME,  "email")
e_mail.send_keys("banny6x@gmail.com")
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

driver.close()
driver.quit()
