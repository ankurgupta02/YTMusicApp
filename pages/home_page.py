from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.player_page import PlayerPage
from pages.locators import Home_Locators
from pages.elements import Elements
from utilities.common_helpers import Common_Helpers


class Home_Page_Shelf(Common_Helpers):

    def __init__(self, driver):
        super().__init__(driver)
#        self.driver = driver
#        self.common = Common_Helpers(driver)

    def get_a_shelf(self, shelf_xpath):
        shelf = self.driver.find_element(By.XPATH, shelf_xpath)
        self.move_and_click_to_element(shelf)
        return shelf

    def get_allvideositems_in_a_shelf(self, shelf_allitems_xpath):
        allvideoitems = self.driver.find_elements(By.XPATH, shelf_allitems_xpath)
        return allvideoitems

    def click_button_on_randomvideo_in_shelf(self, shelf_allitems_xpath, element):
        allvideoitems = self.get_allvideositems_in_a_shelf(shelf_allitems_xpath)
        any_randomvideo = self.get_a_random_video(allvideoitems)

        randomvideo_xpath = f"{shelf_allitems_xpath}[{any_randomvideo}]"
        randomvideo = self.driver.find_element(By.XPATH, randomvideo_xpath)
        randomvideo_element = self.driver.find_element(By.XPATH, randomvideo_xpath + element)

        self.move_and_click_to_element(randomvideo)
        self.move_and_click_to_element(randomvideo_element)

    def click_submenuitem_on_randomvideo_in_shelf(self, submenuitem):
        self.driver.find_element(By.XPATH, Home_Locators.SHELF_SUBMENUITEM_XPATH.format(item=submenuitem)).click()

    def assert_text_on_signindialogbox(self, dialogtext):
        dialog_text = self.driver.find_element(By.XPATH,
                                               Home_Locators.SHELF_SUBMENUITEM_XPATH.format(item=dialogtext)).is_displayed()
        assert dialog_text, "Either dialog text is missing or mismatched."

    def assert_signinbutton_on_signindialogbox(self):
        signinbutton = self.driver.find_element(By.XPATH, Home_Locators.DIALOGBOX_SIGNIN_BUTTON_XPATH).is_displayed()
        assert signinbutton, "Signin button is missing on Dialog."

    def click_previous_next_button_on_shelf(self, button):
        button = self.driver.find_element(By.XPATH, button)
        while True:
            button.click()
            if button.get_attribute("disabled") == Elements.BUTTON_IS_DISABLED:
                break

    def click_playall_button_on_shelf(self):
        self.driver.find_element(By.XPATH, Home_Locators.PLAYALL_BUTTON).click()
        playerpageobject = PlayerPage(self.driver)
        return playerpageobject

    def assert_previous_next_button_on_shelf(self, button, expected):
        button = self.driver.find_element(By.XPATH, button)
        is_disabled = button.get_attribute("disabled")
        assert is_disabled == expected, "Either Horizontal scroll is not done or Previous/Next button is not functional properly."

    def assert_horizontalscroll(self, firstscroll, secondscroll, thirdscroll=None):
        if thirdscroll == None:
            assert ([secondscroll > firstscroll]), "Shelf was NOT horizontally scrolled!"
        else:
            assert all([secondscroll > firstscroll, thirdscroll > secondscroll]), "Shelf was NOT horizontally scrolled!"

    def horizontalscroll(self, direction, element):
        if direction == Elements.MID_SCROLL or direction == Elements.MAX_SCROLL:
            return self.driver.execute_script(f"arguments[0].scrollLeft = arguments[0].{direction};", element)
        elif direction == Elements.MIN_SCROLL:
            return self.driver.execute_script(f"arguments[0].scrollLeft = 0;", element)

    def horizontalscroll_currentposition(self, element):
        return self.driver.execute_script("return arguments[0].scrollLeft;", element)

    def allvideostitles_in_a_container(self, container):
        allvideos = self.driver.find_elements(By.XPATH, container)
        allvideostitles = [title.text.strip() for title in allvideos]
        return allvideostitles

    def compare_twolists(self, list1, list2):
        assert list1 == list2, f"Both lists are not same, mismatch Found!"







    '''LET"S GO
    #element = driver.find_element(By.XPATH, "//yt-formatted-string[@class='primary-text style-scope ytmusic-tastebuilder-shelf-renderer']")
    #element = driver.find_element(By.XPATH, "//button[@aria-label='Let's go']//span[@role='text']")
    element = driver.find_element(By.XPATH, "//button[@aria-label=\"Let's go\"]")

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(5)
    element.click()
    time.sleep(5)
    havea = driver.find_element(By.XPATH, "//yt-formatted-string[@class='title style-scope ytmusic-modal-with-title-and-button-renderer']").is_displayed()
    if havea == True:
        print("yes available")
    else:
        print("No available")
    time.sleep(5)
    tellus = driver.find_element(By.XPATH, "//yt-formatted-string[@class='body style-scope ytmusic-modal-with-title-and-button-renderer']").is_displayed()
    if tellus == True:
        print("yes available")
    else:
        print("No available")
    time.sleep(5)
    imga = driver.find_element(By.XPATH, "//yt-img-shadow[@class='style-scope ytmusic-tastebuilder-shelf-renderer no-transition']//img[@id='img']").is_displayed()
    if imga == True:
        print("yes available")
    else:
        print("No available")
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='contentWrapper']/ytmusic-modal-with-title-and-button-renderer/div/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]").click()
    '''
