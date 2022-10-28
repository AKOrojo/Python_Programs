from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

events_list = {}

CHROME_DRIVER_PATH = "C:/Users/bkoro/OneDrive/Documents/Repos/Python_Programs/Dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")
times = driver.find_elements(
    By.CSS_SELECTOR, '.event-widget time')

events = driver.find_elements(
    By.CSS_SELECTOR, '.event-widget li a')

events_list = {
    n: {"times": times[n].text, "names": events[n].text}for n in range(len(times))}
print(events_list)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
responses = driver.find_element(
    By.CSS_SELECTOR, '#articlecount a')
responses.click()

search = driver.find_element(By.NAME,  "search")
search.send_keys("PYTHON")
search.send_keys(Keys.Enter)
driver.close()
driver.quit()
