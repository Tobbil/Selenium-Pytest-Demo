from selenium.webdriver.common.by import By


class MainPage:
    URL = "http://www.artoftranslation.pl"
    EXPECTED_PAGE_TITLE = "Art of Translation"
    EXPECTED_PHONE_NUMBER = "+48 585 500 132"
    EXPECTED_EMAIL = "biuro@artoftranslation.pl"
    EXPECTED_FACEBOOK_LINK = "https://www.facebook.com/pages/Art-of-Translation/174070282659316"

    # LOCATORS
    PHONE_NUMBER = (By.XPATH, "/html/body/header/div[1]/div/div[3]/div/p[1]")
    EMAIL_ADDRESS = (
        By.XPATH, "/html/body/header/div[1]/div/div[3]/div/p[2]/a")
    FACEBOOK_LINK = (
        By.XPATH, "/html/body/header/div[2]/div/nav/ul[2]/li[1]/a")
