from page_object_pattern.pages.login_data_page import LoginDataPage
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Test login passed")
    @allure.description("This is a successful login in test")
    def test_log_in_passed(self):
        login_data_page = LoginDataPage(self.driver)
        login_data_page.open_page()
        login_data_page.log_in("ppython.ttester@gmail.com", "Pythontester1*")

        assert login_data_page.is_logout_link_displayed()

    @allure.title("Test login failed")
    @allure.description("This is a failed login in test")
    def test_log_in_failed(self):
        login_data_page = LoginDataPage(self.driver)
        login_data_page.open_page()
        login_data_page.log_in("ppython.ttester@gmail.com", "Pythontester1**")

        assert "Zaloguj się do Twojego Konta" in login_data_page.log_in_message()
