import pytest
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from pages.elements import Elements


class Test_Login_Page:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def initialize_pageObject(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)

    def testHomePageTitle(self):
        self.logger.info("*******************Test_001_Login************************")
        self.logger.info("*******************Verify Home Page Title****************")
        self.lp.assertPageTitle(Elements.EXPECTED_TITLE)
        self.logger.info("*******************Page Title Test is Passed.****************")

    def testSignIn(self):
        self.logger.info("*******************Verify Sign In****************")
        self.lp.clickSignin()
        self.lp.setEmail(self.username)
        self.lp.clickNextButton()
        self.lp.setPassword(self.password)
        self.lp.clickNextButton()
        self.lp.clickAvatar()
        self.lp.clickSignOut()
        self.lp.assertSignIn()
        self.logger.info("*******************Sign In Test is Passed****************")

    def testSignIn_LeftPanelGuideExpanded(self):
        self.logger.info("*******************Verify Sign In when Left Panel Guide Expanded****************")
        istextvisible = self.lp.checkLeftPanelGuideText()
        if not istextvisible:
            self.lp.clickGuideIcon()
        self.lp.clickSignin_LeftGuideExpanded()
        self.lp.setEmail(self.username)
        self.lp.clickNextButton()
        self.lp.setPassword(self.password)
        self.lp.clickNextButton()
        self.lp.clickAvatar()
        self.lp.clickSignOut()
        self.lp.assertSignIn()
        self.logger.info("*******************Sign In Test is Passed when Left Panel Guide Expanded****************")

    def testSignIn_LeftPanelGuideCollapsed(self):
        self.logger.info("*******************Verify Sign In when Left Panel Guide Collapsed****************")
        istextvisible = self.lp.checkLeftPanelGuideText()
        if istextvisible:
            self.lp.clickGuideIcon()
        self.lp.clickSignin_LeftGuideCollapsed()
        self.lp.setEmail(self.username)
        self.lp.clickNextButton()
        self.lp.setPassword(self.password)
        self.lp.clickNextButton()
        self.lp.clickAvatar()
        self.lp.clickSignOut()
        self.lp.assertSignIn()
        self.logger.info(
            "*******************Sign In Test is Passed when Left Panel Guide Collapsed****************")
