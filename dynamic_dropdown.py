from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# NOTES: find_elements, get_attribute()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
# wait for the options to appear
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']") # matches 3 elemets
# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element(By.ID, "autosuggest").text) #this will not retrieve the text as it is dynamically loaded
# by the script.  when the page loaded it was not there.
# assert driver.find_element(By.ID, "autosuggest").text == "India" will throw error

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"