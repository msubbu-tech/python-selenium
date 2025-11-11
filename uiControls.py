from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# NOTES: find_elements, get_attribute(), alert, display text, radio button, checkbox

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected(), "checkbox was not selected"
        break

radio_button = driver.find_elements(By.XPATH, "//input[@type='radio']")[2]
radio_button.click()
assert radio_button.is_selected(), "radio button was not selected"

# display text
assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()

# alerts
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Subbu")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
alert.accept() # to click OK
# alert.dismiss() - to click cancel
