import pytest
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from pages.player_page import PlayerPage
from pages.home_page import Home_Page_Shelf
from pages.locators import Player_Locators


class TestPlayerPage:
    """
    Test suite for validating the video player page functionalities including play, pause,
    and navigation controls (next, previous).
    """
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_page_objects(self, setup):
        """
        Pytest fixture that runs automatically before each test.
        Initializes the WebDriver, navigates to the video URL, and creates page object instances.
        """
        self.driver = setup
        self.driver.get(ReadConfig.getVideoUrl())
        self.player_page = PlayerPage(self.driver)
        self.home_page_shelf = Home_Page_Shelf(self.driver)

    def test_play_video(self):
        """
        Verify that a video plays successfully.
        Steps:
        - Wait until the video player is ready.
        - Start video playback.
        - Wait for any ads to finish.
        - Assert that the video is playing.
        """
        self.logger.info("**** test_play_video test case begin ****")
        self.player_page.wait_until_video_ready()
        self.player_page.play()
        self.player_page.wait_for_ads_to_finish()
        self.player_page.assert_is_playing()
        self.logger.info("**** Video playback is successful. ****\n")

    def test_pause_video(self):
        """
        Verify that a video pauses successfully.
        Steps:
        - Wait until the video player is ready.
        - Start video playback.
        - Wait for any ads to finish.
        - Pause the video.
        - Assert that the video is not playing.
        """
        self.logger.info("**** test_pause_video test case begin ****")
        self.player_page.wait_until_video_ready()
        self.player_page.play()
        self.player_page.wait_for_ads_to_finish()
        self.player_page.pause()
        self.player_page.assert_not_playing()
        self.logger.info("**** Video paused is successful. ****\n")

    def test_player_play_button(self):
        """
        Verify that clicking the play button starts video playback.
        Steps:
        - Wait until the video player is ready.
        - Click the play button.
        - Wait for any ads to finish.
        - Assert that the video is playing.
        """
        self.logger.info("**** test_player_play_button test case begin ****")
        self.player_page.wait_until_video_ready()
        self.player_page.click_button(Player_Locators.PLAY_BUTTON)
        self.player_page.wait_for_ads_to_finish()
        self.player_page.assert_is_playing()
        self.logger.info("**** Video playback is successful after clicking play button. ****\n")

    def test_player_pause_button(self):
        """
        Verify that clicking the pause button pauses video playback.
        Steps:
        - Wait until the video player is ready.
        - Click the play button to start playback.
        - Wait for any ads to finish.
        - Click the pause button.
        - Assert that the video is not playing.
        """
        self.logger.info("**** test_player_pause_button test case begin ****")
        self.player_page.wait_until_video_ready()
        self.player_page.click_button(Player_Locators.PLAY_BUTTON)
        self.player_page.wait_for_ads_to_finish()
        self.player_page.click_button(Player_Locators.PAUSE_BUTTON)
        self.player_page.assert_not_playing()
        self.logger.info("**** Video paused is successful after clicking pause button. ****\n")

    def test_player_next_button(self):
        """
        Verify that clicking the next button plays the next video and the title updates accordingly.
        Steps:
        - Wait until the video player is ready.
        - Start video playback.
        - Wait for any ads to finish.
        - Capture the current playing video title.
        - Click the next button.
        - Wait until the next video is ready.
        - Capture the next playing video title.
        - Retrieve the list of all video titles in the playlist queue.
        - Assert that the next video title is different and valid.
        """
        self.logger.info("**** test_player_next_button test case begin ****")
        self.player_page.wait_until_video_ready()
        self.player_page.play()
        self.player_page.wait_for_ads_to_finish()
        current_title = self.player_page.get_current_playing_video_title()
        self.player_page.click_button(Player_Locators.NEXT_BUTTON)
        self.player_page.wait_until_video_ready()
        next_title = self.player_page.get_current_playing_video_title()
        video_queue = self.home_page_shelf.allvideostitles_in_a_container(
            Player_Locators.PLAYLIST_QUEUE_ALLVIDEOS_TITLES
        )
        self.player_page.assert_next_video_title(current_title, next_title, video_queue)
        self.logger.info("**** Next video playback is successful. ****\n")

    def test_player_previous_button(self):
        """
        Verify that clicking the previous button plays the previous video and the title updates accordingly.
        Steps:
        - Wait until the video player is ready.
        - Start video playback.
        - Wait for any ads to finish.
        - Capture the current playing video title.
        - Click the next button to move forward.
        - Wait until the video is ready.
        - Click the previous button to go back.
        - Wait until the video is ready.
        - Capture the previous playing video title.
        - Retrieve the list of all video titles in the playlist queue.
        - Assert that the previous video title is different and valid.
        """
        self.logger.info("**** test_player_previous_button test case begin ****")
        self.player_page.wait_until_video_ready()
        self.player_page.play()
        self.player_page.wait_for_ads_to_finish()
        current_title = self.player_page.get_current_playing_video_title()
        self.player_page.click_button(Player_Locators.NEXT_BUTTON)
        self.player_page.wait_until_video_ready()
        self.player_page.click_button(Player_Locators.PREVIOUS_BUTTON)
        self.player_page.wait_until_video_ready()
        previous_title = self.player_page.get_current_playing_video_title()
        video_queue = self.home_page_shelf.allvideostitles_in_a_container(
            Player_Locators.PLAYLIST_QUEUE_ALLVIDEOS_TITLES
        )
        self.player_page.assert_previous_video_title(current_title, previous_title, video_queue)
        self.logger.info("**** Previous video playback is successful. ****\n")





'''
import pytest
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from pages.player_page import PlayerPage
from pages.home_page import Home_Page_Shelf
from pages.locators import Player_Locators


class Test_Player_Page:
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def pageObjects(self, setup):
        self.driver = setup
        self.driver.get(ReadConfig.getVideoUrl())
        self.pp = PlayerPage(self.driver)
        self.hp = Home_Page_Shelf(self.driver)

    def test_play_video(self):
        self.logger.info("****test_play_video test case begin****")
        self.pp.wait_until_video_ready()
        self.pp.play()
        self.pp.wait_for_ads_to_finish()
        self.pp.assert_is_playing()
        self.logger.info("****Video playback is successful.****\n")

    def test_pause_video(self):
        self.logger.info("****test_pause_video test case begin****")
        self.pp.wait_until_video_ready()
        self.pp.play()
        self.pp.wait_for_ads_to_finish()
        self.pp.pause()
        self.pp.assert_not_playing()
        self.logger.info("****Video paused is successful.****\n")

    def test_player_play_button(self):
        self.logger.info("****test_player_play_button test case begin****")
        self.pp.wait_until_video_ready()
        self.pp.click_button(Player_Locators.PLAY_BUTTON)
        self.pp.wait_for_ads_to_finish()
        self.pp.assert_is_playing()
        self.logger.info("****Video playback is successful after clicking on play button.****\n")

    def test_player_pause_button(self):
        self.logger.info("****test_player_pause_button test case begin****")
        self.pp.wait_until_video_ready()
        self.pp.click_button(Player_Locators.PLAY_BUTTON)
        self.pp.wait_for_ads_to_finish()
        self.pp.click_button(Player_Locators.PAUSE_BUTTON)
        self.pp.assert_not_playing()
        self.logger.info("****Video paused is successful after clicking on pause button.****\n")

    def test_player_next_button(self):
        self.logger.info("****test_player_next_button test case begin****")
        self.pp.wait_until_video_ready()
        self.pp.play()
        self.pp.wait_for_ads_to_finish()
        currentplayingvideotitle = self.pp.get_currentplaying_videotitle()
        self.pp.click_button(Player_Locators.NEXT_BUTTON)
        self.pp.wait_until_video_ready()
        nextplayingvideotitle = self.pp.get_currentplaying_videotitle()
        videoqueue = self.hp.allvideostitles_in_a_container(Player_Locators.PLAYLIST_QUEUE_ALLVIDEOS_TITLES)
        self.pp.assert_next_video_title(currentplayingvideotitle, nextplayingvideotitle, videoqueue)
        self.logger.info("****Next video playback is successful.****\n")

    def test_player_previous_button(self):
        self.logger.info("****test_player_previous_button test case begin****")
        self.pp.wait_until_video_ready()
        self.pp.play()
        self.pp.wait_for_ads_to_finish()
        currentplayingvideotitle = self.pp.get_currentplaying_videotitle()
        self.pp.click_button(Player_Locators.NEXT_BUTTON)
        self.pp.wait_until_video_ready()
        self.pp.click_button(Player_Locators.PREVIOUS_BUTTON)
        self.pp.wait_until_video_ready()
        previousplayingvideotitle = self.pp.get_currentplaying_videotitle()
        videoqueue = self.hp.allvideostitles_in_a_container(Player_Locators.PLAYLIST_QUEUE_ALLVIDEOS_TITLES)
        self.pp.assert_previous_video_title(currentplayingvideotitle, previousplayingvideotitle, videoqueue)
        self.logger.info("****Previous video playback is successful.****\n")
'''