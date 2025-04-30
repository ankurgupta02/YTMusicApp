from selenium.webdriver.common.by import By
from pages.locators import Login_Locator
from utilities.common_helpers import Common_Helpers

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.common = Common_Helpers()

    def clickSignin(self):
        self.driver.find_element(By.XPATH, Login_Locator.SIGN_IN_BUTTON).click()

    def setEmail(self, username):
        self.common.wait_for_element_visible(self.driver, (By.XPATH, Login_Locator.EMAIL_ID)).send_keys(username)

    def setPassword(self, password):
        self.common.wait_for_element_visible(self.driver, (By.XPATH, Login_Locator.PASSWORD)).send_keys(password)

    def clickNextButton(self):
        self.driver.find_element(By.XPATH, Login_Locator.NEXT_BUTTON).click()

    def assertSignIn(self):
        assertSignInPage = self.driver.find_element(By.XPATH, Login_Locator.SIGN_IN_BUTTON).is_displayed()
        assert assertSignInPage==True, "Sign In button is not available"

    def assertPageTitle(self, expected_title):
        assertPageTitle = self.driver.title
        assert assertPageTitle==expected_title, "Page Title is mismatched."

    def clickAvatar(self):
        self.driver.find_element(By.XPATH, Login_Locator.AVATAR_BUTTON).click()

    def clickSignOut(self):
        self.driver.find_element(By.XPATH, Login_Locator.SIGN_OUT_BUTTON).click()

    def checkLeftPanelGuideText(self):
        return self.driver.find_element(By.XPATH, Login_Locator.SIGN_IN_TEXT_LEFT_GUIDE).is_displayed()

    def clickGuideIcon(self):
        self.driver.find_element(By.XPATH, Login_Locator.LEFT_GUIDE_BUTTON).click()

    def clickSignin_LeftGuideExpanded(self):
        self.driver.find_element(By.XPATH, Login_Locator.SIGN_IN_BUTTON_WHEN_LEFTGUIDE_EXPANDED).click()

    def clickSignin_LeftGuideCollapsed(self):
        self.driver.find_element(By.XPATH, Login_Locator.SIGN_IN_BUTTON_WHEN_LEFTGUIDE_COLLAPSED).click()