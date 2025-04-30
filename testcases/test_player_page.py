import time
import pytest
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from pages.player_page import PlayerPage

class Test_Player_Page:

    @pytest.fixture(autouse=True)
    def pageObjects(self, setup):
        self.driver = setup
        self.driver.get(ReadConfig.getVideoUrl())
        self.pp = PlayerPage(self.driver)
        self.logger = LogGen.loggen()

    def test_play_video(self, setup):
        self.driver = setup
        self.logger.info("****test_play_video test case begin****")
        self.wait_until_video_ready()
        self.pp.play()
        self.pp.wait_for_ads_to_finish()
        self.pp.assert_is_playing()
        self.logger.info("****Video playback is successful.****")

    def test_pause_video(self, setup):
        self.driver = setup
        self.logger.info("****test_pause_video test case begin****")
        self.wait_until_video_ready()
        self.pp.play()
        self.pp.wait_for_ads_to_finish()
        self.pp.pause()
        self.pp.assert_not_playing()
        self.logger.info("****Video paused is successful.****")


