import allure
import logging
from allure_commons.types import AttachmentType
from page_object_pattern.locators import locators


class LoginDataPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cookies_button = locators.LoginDataPage.cookies_button
        self.my_account_button = locators.LoginDataPage.my_account_button
        self.username = locators.LoginDataPage.username
        self.login_password = locators.LoginDataPage.login_password
        self.log_in_button = locators.LoginDataPage.log_in_button
        self.log_out_msg = locators.LoginDataPage.log_out_msg
        self.log_in_msg = locators.LoginDataPage.log_in_msg

    @allure.step("Opening page")
    def open_page(self):
        self.logger.info("Opening page")
        self.driver.get("https://www.obi.pl/")
        self.driver.find_element(*self.cookies_button).click()
        self.driver.find_element(*self.my_account_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Opening page", attachment_type=AttachmentType.PNG)

    @allure.step("Setting username: '{1}' and password: '{2}'")
    def log_in(self, username, password):
        self.logger.info("Entering username {username}, password {password}".format(username=username, password=password))
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.log_in_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Log in page", attachment_type=AttachmentType.PNG)

    @allure.step("Displaying log out link")
    def is_logout_link_displayed(self):
        self.logger.info("Logout link displaying")
        allure.attach(self.driver.get_screenshot_as_png(), name="Displaying logout link", attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.log_out_msg).is_displayed()

    @allure.step("Displaying log in message")
    def log_in_message(self):
        self.logger.info("Login message displaying")
        allure.attach(self.driver.get_screenshot_as_png(), name="Displaying log in message", attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.log_in_msg).text




