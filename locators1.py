from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# Topics covered
# send_keys(), click(), clear(), .text, select class and its methods


# XPATH //tag[@attr='']
# CSS_SELECTOR  tag[attr=''], .classname,  #id
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("cutesubbu1992@gmail.com")
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("cutesubbu1992@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='exampleCheck1']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
# dropdown.select_by_visible_text("Male")
# dropdown.select_by_value(" ") if value attribute is defined

# when multiple matches are there for an XPATH, use index. starts from 1
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

assert 'success' in driver.find_element(By.CLASS_NAME, "alert-success").text
time.sleep(10)
driver.close