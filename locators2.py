from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()

# XPATH //tag[@attr='']
# CSS_SELECTOR  tag[attr=''], .classname,  #id

driver.find_element(By.LINK_TEXT, "Forgot password?").click() #make sure this is a link , when you inspect there should be tag a
driver.find_element(By.XPATH, "//div/form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.XPATH, "//div/form/div[2]/input").send_keys("Hello@1234")

# alternate way using CSS SELECTOR
driver.find_element(By.CSS_SELECTOR, "div form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//div/form/div[3]/input").send_keys("Hello@1234")
# driver.find_element(By.XPATH, '//button[text()="Save New Password"]').click()   # when there is no attribute for this button class
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.close()

# NOTES: link text , traversing through tags,
# button class with text (comes handy when you have no other attributes  in html page, though XPATH has text(), it is not an attribute from html page)