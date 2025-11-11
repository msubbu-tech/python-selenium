#
from selenium import webdriver
# import time
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# # NOTES: frames are embedded to local html which is the scope of driver object, driver object
# # doesn't have access to frames by default.
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/iframe")
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# driver.switch_to.frame()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")

# Switch to the "iframeResult" frame By ID or Name
driver.switch_to.frame("iframeResult")

# Now we are inside the iframeResult, which itself contains another iframe!
inner_iframe = driver.find_element(By.XPATH, "//iframe")
driver.switch_to.frame(inner_iframe)

# Interact with element inside inner iframe
heading = driver.find_element(By.TAG_NAME, "h1")
print("Text inside iframe:", heading.text)

# Go back to main page
driver.switch_to.default_content()

print("Returned to main page.")
driver.quit()