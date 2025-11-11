from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# NOTES: chaining of web elements, implicit wait, explicit wait, stale element reference exception
veggies=[]
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")
driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@type='submit']")
time.sleep(5)
berries = driver.find_elements(By.XPATH, "//div[@class='products']/div") # returns list of web elements or empty list,
# implict wait is not for find_elements method as for the return type is list. selenium doesn't bother if list is true or false.
assert len(berries) == 3

for berrie in berries:
    # berrie.find_element(By.XPATH, "//button[text()='ADD TO CART']").click() #chaining of web elements.
    berrie.find_element(By.XPATH, "div/button").click() #chaining of web elements.
    veggies.append(berrie.find_element(By.XPATH, "//h4")) #chaining of web elements.
    # Add to cart button is a web element inside berrie web element
print(veggies[0].text)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# implicit wait is applied in the below step.
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoBtn")))
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"


# calculate total
for ele in driver.find_elements(By.XPATH, "//tr/td[5]/p"):
    print(ele.text)
# alternate way using css selector
for ele in driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p"):
    print(ele.text)

# print(veggies[0].text) # throws stale element reference exception here

# FAQ about waits
# why selenium wait is preferred over static sleep? selenium wait will not wait for the whole time duration given.
# for ex: if selenium wait is 5 sec and the web element is found at 3rd sec, selenium goes to next step. (2 sec saved)

# why explict wait is not preferred over implicit wait globally ?
# when web elements are expected to load within 5 sec, one particular step needs 10 sec, before that specific step we
# use explicit wait,
# if explicit wait is used globally (with 10 sec), i) all the steps will unncessary wait for whole 15 sec
# ii) if any bug with delayed appearance of web elements after 5 seconds can't be found

# why explicit wait is preferred over implict
# implict - just check the presence of an element
# explict - not only presence, visibility or clickability, text, alerts, etc.