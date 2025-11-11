from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# NOTES: mouse hovering

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# action.double_click(driver.find_element(By.LINK_TEXT, "Reload")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


# note - when to use line #18
# if reload is performed after context click , then use move to element , do click

# note - when to use line #17
# straight away clicking the reload option after hovering.

# double click check boxes,- one to pratice