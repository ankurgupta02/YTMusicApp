import pytest
from pages.home_page import Home_Page_Shelf
from utilities.custom_logger import LogGen
from pages.elements import Elements
from pages.locators import Home_Locators, Player_Locators
from utilities.common_helpers import Common_Helpers
from utilities.read_properties import ReadConfig


class Test_Home_Page_Signout:
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def pageObjects(self, setup):
        self.driver = setup
        self.driver.get(ReadConfig.getApplicationUrl())
        self.hp = Home_Page_Shelf(self.driver)
        self.ch = Common_Helpers(self.driver)

    def test_signindialog_with_savetoplaylist_option(self):
        self.logger.info(
            "****test_signindialog_with_savetoplaylist_option test case begin****")
        self.hp.click_button_on_randomvideo_in_shelf(Home_Locators.SHELF_ALLITEMS_XPATH,
                                                     Home_Locators.CONTEXTUAL_MENU_BUTTON)
        self.hp.click_submenuitem_on_randomvideo_in_shelf(Elements.SAVE_TO_PLAYLIST)

        self.hp.assert_text_on_signindialogbox(Elements.SAVE_THIS_FOR_LATER)
        self.logger.info(f"****{Elements.SAVE_THIS_FOR_LATER} text is present on dialog****")
        self.hp.assert_text_on_signindialogbox(Elements.MAKE_PLAYLISTS_AND_SHARE_THEM_AFTER_SIGNING_IN)
        self.logger.info(
            f"****{Elements.MAKE_PLAYLISTS_AND_SHARE_THEM_AFTER_SIGNING_IN} text is present on dialog****")

        self.hp.assert_signinbutton_on_signindialogbox()
        self.logger.info("****SignIn button is present on dialog****")

        self.logger.info(
            f"****SignIn Dialog test case is passed when {Elements.SAVE_TO_PLAYLIST} option is clicked on shelf video****\n")

    def test_signindialog_with_savetolibrary_option(self):
        self.logger.info(
            "****test_signindialog_with_savetolibrary_option test case begin****")
        self.hp.click_button_on_randomvideo_in_shelf(Home_Locators.SHELF_ALLITEMS_XPATH,
                                                     Home_Locators.CONTEXTUAL_MENU_BUTTON)
        self.hp.click_submenuitem_on_randomvideo_in_shelf(Elements.SAVE_TO_LIBRARY)

        self.hp.assert_text_on_signindialogbox(Elements.SAVE_THIS_FOR_LATER)
        self.logger.info(f"****{Elements.SAVE_THIS_FOR_LATER} text is present on dialog****")
        self.hp.assert_text_on_signindialogbox(Elements.SAVE_FAVORITES_TO_YOUR_LIRARY_AFTER_SIGNING_IN)
        self.logger.info(
            f"****{Elements.SAVE_FAVORITES_TO_YOUR_LIRARY_AFTER_SIGNING_IN} text is present on dialog****")

        self.hp.assert_signinbutton_on_signindialogbox()
        self.logger.info("****SignIn button is present on dialog****")

        self.logger.info(
            f"****SignIn Dialog test case is passed when {Elements.SAVE_TO_LIBRARY} option is clicked on shelf video****\n")

    def test_signindialog_with_like_option(self):
        self.logger.info(
            "****test_signindialog_with_like_option test case begin****")
        self.hp.click_button_on_randomvideo_in_shelf(Home_Locators.SHELF_ALLITEMS_XPATH, Home_Locators.LIKE_BUTTON)

        self.hp.assert_text_on_signindialogbox(Elements.LIKE_THIS_SONG)
        self.logger.info(f"****{Elements.LIKE_THIS_SONG} text is present on dialog****")
        self.hp.assert_text_on_signindialogbox(Elements.IMPROVE_RECOMMENDATIONS_AND_SAVE_MUSIC_AFTER_SIGNING_IN)
        self.logger.info(
            f"****{Elements.IMPROVE_RECOMMENDATIONS_AND_SAVE_MUSIC_AFTER_SIGNING_IN} text is present on dialog****")

        self.hp.assert_signinbutton_on_signindialogbox()
        self.logger.info("****SignIn button is present on dialog****")

        self.logger.info(
            f"****SignIn Dialog test case is passed when Like option is clicked on shelf video****\n")

    def test_signindialog_with_dislike_option(self):
        self.logger.info(
            "****test_signindialog_with_dislike_option test case begin****")
        self.hp.click_button_on_randomvideo_in_shelf(Home_Locators.SHELF_ALLITEMS_XPATH, Home_Locators.DISLIKE_BUTTON)

        self.hp.assert_text_on_signindialogbox(Elements.NOT_A_FAN)
        self.logger.info(f"****{Elements.NOT_A_FAN} text is present on dialog****")
        self.hp.assert_text_on_signindialogbox(Elements.IMPROVE_YOUR_RECOMMENDATIONS_AFTER_SIGNING_IN)
        self.logger.info(
            f"****{Elements.IMPROVE_YOUR_RECOMMENDATIONS_AFTER_SIGNING_IN} text is present on dialog****")

        self.hp.assert_signinbutton_on_signindialogbox()
        self.logger.info("****SignIn button is present on dialog****")

        self.logger.info(
            f"****SignIn Dialog test case is passed when Dislike option is clicked on shelf video****\n")

    def test_playall_button_quickshelf(self):
        self.logger.info("****test_playall_button_quickshelf test case begin****")

        allvideostitles_quickshelf = self.hp.allvideostitles_in_a_container(Home_Locators.SHELF_ALLVIDEOS_TITLES)
        playerpageobject = self.hp.click_playall_button_on_shelf()

        self.ch.wait_for_element_visible(Player_Locators.PLAYLIST_QUEUE, "Playlist Queue")

        playerpageobject.assert_is_playing()
        allvideostitles_playlist = self.hp.allvideostitles_in_a_container(Player_Locators.PLAYLIST_QUEUE_ALLVIDEOS_TITLES)
        self.hp.compare_twolists(allvideostitles_quickshelf, allvideostitles_playlist)
        self.logger.info(
            f"****Previous button is functional properly as Scroll goes horizontally left side after clicking the previous button until disabled****\n")

    def test_horizontalscroll_quickshelf(self):
        self.logger.info("****test_horizontalscroll_quickshelf test case begin****")
        element = self.hp.get_a_shelf(Home_Locators.SHELF_XPATH)

        # scroll position before scrolling the scroll bar
        beforescroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # scroll position after right side scrolling the scroll bar in middle(~almost)
        self.hp.horizontalscroll(Elements.MID_SCROLL, element)
        aftermidscroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # scroll position after right side scrolling the scroll bar till the end
        self.hp.horizontalscroll(Elements.MAX_SCROLL, element)
        aftermaxscroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # compare the scroll position before, mid and max scrolling right side
        self.hp.assert_horizontalscroll(beforescroll_currentposition, aftermidscroll_currentposition,
                                        aftermaxscroll_currentposition)
        self.logger.info(f"****Horizontal Scroll right side is successully done, working fine.****")

        # scroll position after left side scrolling the scroll bar in middle(~almost)
        self.hp.horizontalscroll(Elements.MID_SCROLL, element)
        aftermidscroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # scroll position after left side scrolling the scroll bar till the starting
        self.hp.horizontalscroll(Elements.MIN_SCROLL, element)
        afterminscroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # compare the scroll position starting, mid and max scrolling left side
        self.hp.assert_horizontalscroll(afterminscroll_currentposition, aftermidscroll_currentposition,
                                        aftermaxscroll_currentposition)
        self.logger.info(f"****Horizontal Scroll left side is successully done, working fine.****\n")

    def test_previous_next_buttons_quickshelf(self):
        self.logger.info("****test_previous_next_buttons_quickshelf test case begin****")
        element = self.hp.get_a_shelf(Home_Locators.SHELF_XPATH)

        # check previous and next button status before clicking the previous or next button
        self.hp.assert_previous_next_button_on_shelf(Home_Locators.PREVIOUS_BUTTON_ON_SHELF,
                                                     expected=Elements.BUTTON_IS_DISABLED)
        self.hp.assert_previous_next_button_on_shelf(Home_Locators.NEXT_BUTTON_ON_SHELF,
                                                     expected=Elements.BUTTON_IS_ENABLED)
        self.logger.info(f"****Initially, Previous button is disabled and Next button is enabled.****")

        # scroll position before clicking the previous or next button
        beforescroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # click on next button until disabled (till clickable)
        self.hp.click_previous_next_button_on_shelf(Home_Locators.NEXT_BUTTON_ON_SHELF)

        # mouseover on an item on shelf so that horizontal scroll can be seen
        self.hp.get_a_shelf(Home_Locators.SHELF_XPATH)

        # check previous and next button status after clicking the next button until disabled (till clickable)
        self.hp.assert_previous_next_button_on_shelf(Home_Locators.PREVIOUS_BUTTON_ON_SHELF,
                                                     expected=Elements.BUTTON_IS_ENABLED)
        self.hp.assert_previous_next_button_on_shelf(Home_Locators.NEXT_BUTTON_ON_SHELF,
                                                     expected=Elements.BUTTON_IS_DISABLED)
        self.logger.info(
            f"****Previous button is enabled and Next button is disabled after clicking the next button until disabled.****")

        # scroll position after clicking the next button until disabled (till clickable)
        aftermaxscroll_currentposition = self.hp.horizontalscroll_currentposition(element)

        # compare the scroll position before and max scrolling right side after clicking the next button until disabled (till clickable)
        self.hp.assert_horizontalscroll(beforescroll_currentposition, aftermaxscroll_currentposition)
        self.logger.info(
            f"****Next button is functional properly as Scroll goes horizontally right side after clicking the next button until disabled****")

        # click on previous button until disabled (until clickable)
        self.hp.click_previous_next_button_on_shelf(Home_Locators.PREVIOUS_BUTTON_ON_SHELF)

        # mouseover on an item on shelf so that horizontal scroll can be seen
        self.hp.get_a_shelf(Home_Locators.SHELF_XPATH)

        # scroll position after clicking the previous button until disabled (till clickable)
        afterminscroll_position = self.hp.horizontalscroll_currentposition(element)

        # check previous and next button status after clicking the previous button until disabled (till clickable)
        self.hp.assert_previous_next_button_on_shelf(Home_Locators.PREVIOUS_BUTTON_ON_SHELF,
                                                     expected=Elements.BUTTON_IS_DISABLED)
        self.hp.assert_previous_next_button_on_shelf(Home_Locators.NEXT_BUTTON_ON_SHELF,
                                                     expected=Elements.BUTTON_IS_ENABLED)
        self.logger.info(
            f"****Previous button is disabled and Next button is enabled after clicking the previous button until disabled.****")

        self.hp.assert_horizontalscroll(afterminscroll_position, aftermaxscroll_currentposition)
        self.logger.info(
            f"****Previous button is functional properly as Scroll goes horizontally left side after clicking the previous button until disabled****\n")
