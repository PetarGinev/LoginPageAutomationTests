import pytest
from selenium.webdriver.common.by import By
import time


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username_variable, password_variable, expected_error_message",
                             [("student1", "Password123", "Your username is invalid!"),
                              ("student", "Password1234", "Your password is invalid!")])
    def test_negative_login(self, driver, username_variable, password_variable, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrect User into Username field
        username = driver.find_element(By.ID, "username")
        username.send_keys(username_variable)

        # Type password Password123 into Password field
        password = driver.find_element(By.ID, "password")
        password.send_keys(password_variable)

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(1)

        # Verify error message is displayed
        error_message_element = driver.find_element(By.ID, "error")
        assert error_message_element.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is "Your username is invalid!"
        error_message = error_message_element.text
        assert error_message == expected_error_message, "Error message is not expected"


"""

Old versions 

    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrect User into Username field
        username = driver.find_element(By.ID, "username")
        username.send_keys("student1")

        # Type password Password123 into Password field
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(1)

        # Verify error message is displayed
        error_message_element = driver.find_element(By.ID, "error")
        assert error_message_element.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_message = error_message_element.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username User into Username field
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

        # Type incorrect password Password1234 into Password field
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password1234")

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(1)

        # Verify error message is displayed
        error_message_element = driver.find_element(By.ID, "error")
        assert error_message_element.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your password is invalid!
        error_message = error_message_element.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
"""