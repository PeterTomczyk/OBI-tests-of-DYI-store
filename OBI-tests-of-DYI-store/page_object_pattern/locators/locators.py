from selenium.webdriver.common.by import By


class LoginDataPage:

    cookies_button = (By.XPATH, "//button[contains(.,'OK')]")
    my_account_button = (By.XPATH, "//*[text()='Moje konto']")
    username = (By.NAME, "j_username")
    login_password = (By.NAME, "j_password")
    log_in_button = (By.XPATH, "//button[contains(.,'Zaloguj się')]")
    log_out_msg = (By.LINK_TEXT, "Wyloguj")
    log_in_msg = (By.CSS_SELECTOR, "h5.tw-font-obi-bold.tw-text-3xl")


class AccountRegLocators:

    first_reg_button = (By.LINK_TEXT, "Zarejestruj się")
    natural_person = (By.XPATH, "//*[text()='Osoba prywatna']")
    gender = (By.CSS_SELECTOR, "span.fake-radio")
    name = (By.NAME, "userData.addressData.firstname")
    last_name = (By.NAME, "userData.addressData.lastname")
    street_name = (By.NAME, "userData.addressData.streetname")
    street_number = (By.NAME, "userData.addressData.streetnumber")
    postal_code = (By.NAME, "userData.addressData.postalcode")
    town = (By.NAME, "userData.addressData.town")
    email_address = (By.NAME, "userData.addressData.email")
    reg_in_password = (By.NAME, "userData.password")
    repeat_password = (By.NAME, "userData.passwordRepeat")
    phone = (By.NAME, "userData.addressData.phone1")
    consent_for_newsletter = (By.CSS_SELECTOR, "span.fake-checkbox")
    consent_to_the_regulations = (By.CSS_SELECTOR, "span.fake-checkbox")
    reg_in_button_finish = (By.XPATH, "//button[text()='Zarejestruj się!']")
    correct_msg = (By.XPATH, "//div[h3/text()='Witaj nowy użytkowniku OBI.pl!']")
    error_msg = (By.CSS_SELECTOR, "p.p.span8.width-limited.error-text")


