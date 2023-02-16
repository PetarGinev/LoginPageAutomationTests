import time
import pytest
from selenium.webdriver.common.by import By

class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Go to web page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

        # Type password Password123 into Password field
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(1)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        current_url = driver.current_url
        assert current_url == 'https://practicetestautomation.com/logged-in-successfully/'

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new pag
        log_out_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_locator.is_displayed()
        time.sleep(1)
