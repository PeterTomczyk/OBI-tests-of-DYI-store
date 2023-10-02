import logging
import allure
from allure_commons.types import AttachmentType
from page_object_pattern.locators import locators


class AccountRegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cookies_button = locators.LoginDataPage.cookies_button
        self.my_account_button = locators.LoginDataPage.my_account_button
        self.first_reg_button = locators.AccountRegLocators.first_reg_button
        self.natural_person = locators.AccountRegLocators.natural_person
        self.gender = locators.AccountRegLocators.gender
        self.name = locators.AccountRegLocators.name
        self.last_name = locators.AccountRegLocators.last_name
        self.street_name = locators.AccountRegLocators.street_name
        self.street_number = locators.AccountRegLocators.street_number
        self.postal_code = locators.AccountRegLocators.postal_code
        self.town = locators.AccountRegLocators.town
        self.email_address = locators.AccountRegLocators.email_address
        self.reg_in_password = locators.AccountRegLocators.reg_in_password
        self.repeat_password = locators.AccountRegLocators.repeat_password
        self.phone = locators.AccountRegLocators.phone
        self.consent_for_newsletter = locators.AccountRegLocators.consent_for_newsletter
        self.consent_to_the_regulations = locators.AccountRegLocators.consent_to_the_regulations
        self.reg_in_button_finish = locators.AccountRegLocators.reg_in_button_finish
        self.correct_msg = locators.AccountRegLocators.correct_msg
        self.error_msg = locators.AccountRegLocators.error_msg

    @allure.step("Opening page")
    def open_page(self):
        self.logger.info("Opening page")
        self.driver.get("https://www.obi.pl/")
        self.driver.find_element(*self.cookies_button).click()
        self.driver.find_element(*self.my_account_button).click()
        self.driver.find_element(*self.first_reg_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Opening page", attachment_type=AttachmentType.PNG)

    @allure.step("Setting name: '{1}' and last name: '{2}'")
    def set_personal_data(self, name, last_name):
        self.logger.info("Setting name {name} and last_name {last_name}".format(name=name, last_name=last_name))
        self.driver.find_element(*self.natural_person).click()
        self.driver.find_elements(*self.gender)[1].click()
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting personal data", attachment_type=AttachmentType.PNG)

    @allure.step("Setting street name: '{1}' and street number: '{2}'")
    def set_address_part_1(self, street_name, street_number):
        self.logger.info("Setting street_name {street}, street_number {number}".format(street=street_name, number=street_number))
        self.driver.find_element(*self.street_name).send_keys(street_name)
        self.driver.find_element(*self.street_number).send_keys(street_number)
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting address -> part_1", attachment_type=AttachmentType.PNG)

    @allure.step("Setting postal code: '{1}' and town: '{2}'")
    def set_address_part_2(self, postal_code, town):
        self.logger.info("Setting postal_code {code}, town {town}".format(code=postal_code, town=town))
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.town).send_keys(town)
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting address -> part_2", attachment_type=AttachmentType.PNG)

    @allure.step("Setting email: '{1}'")
    def set_email(self, email):
        self.logger.info("Setting email {}".format(email))
        self.driver.find_element(*self.email_address).send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting email", attachment_type=AttachmentType.PNG)

    @allure.step("Setting password: '{1}' and repeat password: '{2}'")
    def set_password(self, password, repeat_password):
        self.logger.info("Setting password {password}, repeat_password {repeat}".format(password=password, repeat=repeat_password))
        self.driver.find_element(*self.reg_in_password).send_keys(password)
        self.driver.find_element(*self.repeat_password).send_keys(repeat_password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting email", attachment_type=AttachmentType.PNG)

    @allure.step("Setting phone number: '{1}'")
    def set_phone(self, phone):
        self.logger.info("Setting phone {}".format(phone))
        self.driver.find_element(*self.phone).click()
        self.driver.find_element(*self.phone).send_keys(phone)
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting phone number", attachment_type=AttachmentType.PNG)

    @allure.step("Setting newsletter subscription")
    def newsletter_subscription(self):
        self.logger.info("Consent to the newsletter")
        self.driver.find_elements(*self.consent_for_newsletter)[0].click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting newsletter subscription", attachment_type=AttachmentType.PNG)

    @allure.step("Setting consent to the conditions")
    def consent_to_the_conditions(self):
        self.logger.info("Consent to the conditions")
        self.driver.find_elements(*self.consent_to_the_regulations)[1].click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Setting consent to the conditions",attachment_type=AttachmentType.PNG)

    @allure.step("Saving data")
    def save_data(self):
        self.logger.info("Saving data")
        self.driver.find_element(*self.reg_in_button_finish).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Saving data", attachment_type=AttachmentType.PNG)

    @allure.step("Correct message creating")
    def correct_msg_created(self):
        self.logger.info("Correct message creating")
        allure.attach(self.driver.get_screenshot_as_png(), name="Correct message creating", attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.correct_msg).text

    @allure.step("Error message creating")
    def error_msg_created(self):
        self.logger.info("Error message creating")
        allure.attach(self.driver.get_screenshot_as_png(), name="Error message creating", attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.error_msg).text


