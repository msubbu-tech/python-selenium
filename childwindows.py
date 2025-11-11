from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# NOTES:

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Click Here").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() # child window gets closed

driver.switch_to.window(handles[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
