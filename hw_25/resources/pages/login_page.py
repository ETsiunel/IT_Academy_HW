"""Login page"""


from selenium.webdriver.common.by import By
from hw_25.resources.pages.base_page import BasePage
from hw_25.resources.locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def go_to_signup(self):
        self.driver.find_element(By.CSS_SELECTOR, LoginLocators.signup_button).click()

    def login(self, email, password):
        email_input = self.driver.find_element(By.CSS_SELECTOR, LoginLocators.email_input_login)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.CSS_SELECTOR, LoginLocators.password_input_login)
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(By.CSS_SELECTOR, LoginLocators.submit_button_login).click()

    def is_logged_in(self):
        return "Logout" in self.driver.page_source
