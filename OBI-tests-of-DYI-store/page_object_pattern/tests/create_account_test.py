import random

import allure
import pytest
from page_object_pattern.pages.account_registration_page import AccountRegistrationPage


@pytest.mark.usefixtures("setup")
class TestOfCreatingAccount:

    @allure.title("Test create account passed")
    @allure.description("This is test of correct account creation")
    def test_create_account_passed(self):
        email = str(random.randint(0, 1000)) + "pythondeveloper@o2.pl"
        account_registration_page = AccountRegistrationPage(self.driver)
        account_registration_page.open_page()
        account_registration_page.set_personal_data("Piotr", "Tomczyk")
        account_registration_page.set_address_part_1("Kwiatowa", "9")
        account_registration_page.set_address_part_2("00-001", "Warszawa")
        account_registration_page.set_email(email)
        account_registration_page.set_password("Pythontester1*", "Pythontester1*")
        account_registration_page.set_phone("+48 223 456 789")
        account_registration_page.newsletter_subscription()
        account_registration_page.consent_to_the_conditions()
        account_registration_page.save_data()

        assert "Witaj nowy użytkowniku OBI.pl!" in account_registration_page.correct_msg_created()

    @allure.title("Test create account failed")
    @allure.description("This is test of incorrect account creation")
    def test_create_account_failed(self):
        account_registration_page = AccountRegistrationPage(self.driver)
        account_registration_page.open_page()
        account_registration_page.set_personal_data("Piotr", "Tomczyk")
        account_registration_page.set_address_part_1("Kwiatowa", "9")
        account_registration_page.set_address_part_2("00-001", "Warszawa")
        account_registration_page.set_email("ppython.ttester@gmail.com")
        account_registration_page.set_password("Pythontester1*", "Pythontester1*")
        account_registration_page.set_phone("+48 223 456 789")
        account_registration_page.newsletter_subscription()
        account_registration_page.consent_to_the_conditions()
        account_registration_page.save_data()
        assert "Pod tym adresem mailowym zostało już zarejestrowane konto Klienta na OBI.pl." in account_registration_page.error_msg_created()





