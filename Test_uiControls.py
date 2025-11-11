from selenium import webdriver
import time, allure, pytest

from selenium.webdriver.common.by import By

# NOTES: find_elements, get_attribute(), alert, display text, radio button, checkbox

@pytest.fixture()
def test_setup():
    with allure.step("Opening the browser"):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.save_screenshot("screenshot.png")
        with open("screenshot.png", "rb") as f:
            allure.attach(f.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.description("testing alert box")
@allure.severity(allure.severity_level.CRITICAL)
def test_uiControls(test_setup, test_teardown):
    with allure.step("UI Controls - checkbox selection"):
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == "option2":
                checkbox.click()
                assert checkbox.is_selected(), "checkbox was not selected"
                break

        radio_button = driver.find_elements(By.XPATH, "//input[@type='radio']")[2]
        radio_button.click()
        assert radio_button.is_selected(), "radio button was not selected"

    with allure.step("UI Controls - display text"):
        assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
        driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
        assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()

    with allure.step("alerts"):
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Subbu")
        driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
        alert = driver.switch_to.alert
        alert.accept() # to click OK
        # alert.dismiss() - to click cancel

@pytest.fixture()
def test_teardown(request):
    def teardown():
        with allure.step("closing the browser"):
            browser_log = "INFO: Browser closed successfully"
            allure.attach(
                browser_log,
                name="Browser Log",
                attachment_type=allure.attachment_type.TEXT
            )
            driver.quit()
    request.addfinalizer(teardown)

# (.venv) PS C:\python-selenium> pytest -s -v Test_uiControls.py::test_uiControls --alluredir=reports
