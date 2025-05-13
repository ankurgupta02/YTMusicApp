import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Player_Locators


class PlayerPage:
    """
    Page object representing the video player on YouTube Music.
    Provides methods to interact with the video element and player controls.
    """

    def __init__(self, driver):
        """
        Initialize with a Selenium WebDriver instance and get the video element.
        """
        self.driver = driver
        self.player = self._get_video_element()

    def _get_video_element(self):
        """
        Retrieve the HTML5 video element from the page using JavaScript.
        :return: video element reference
        """
        return self.driver.execute_script("return document.querySelector('video');")

    def _execute_js(self, command, *args):
        """
        Execute JavaScript commands on the video element.
        :param command: JavaScript property or method to execute on the video element
        :param args: additional arguments for the JS command
        :return: result of the JS execution
        """
        return self.driver.execute_script(f'return arguments[0].{command}', self.player, *args)

    def play(self):
        """
        Play the video by clicking on the page body (to focus) and invoking play() on the video element.
        """
        self.driver.find_element(By.TAG_NAME, 'body').click()
        self._execute_js("play()")

    def pause(self):
        """
        Pause the video playback.
        """
        self._execute_js("pause()")

    def seek(self, seconds):
        """
        Seek the video to a specific time in seconds.
        :param seconds: time position to seek to
        """
        self._execute_js("currentTime = arguments[1]", seconds)

    def set_volume(self, level):
        """
        Set the video volume.
        :param level: float between 0.0 (mute) and 1.0 (max volume)
        """
        self._execute_js("volume = arguments[1]", level)

    def get_current_time(self):
        """
        Get the current playback time of the video in seconds.
        :return: current time in seconds
        """
        return self._execute_js("currentTime")

    def assert_is_playing(self):
        """
        Assert that the video is currently playing.
        Checks that the video is not paused and that the playback time is progressing.
        Raises AssertionError if conditions are not met.
        """
        assert not self._execute_js("paused"), "Video is not playing!"
        start_time = self.get_current_time()
        time.sleep(5)
        end_time = self.get_current_time()
        assert end_time > start_time, (
            "Video is playing but playback time is not progressing; "
            "player controls may be missing or video is stalled."
        )

    def assert_not_playing(self):
        """
        Assert that the video is currently paused.
        Checks that the video is paused and playback time does not advance.
        Raises AssertionError if conditions are not met.
        """
        assert self._execute_js("paused"), "Video is playing!"
        start_time = self.get_current_time()
        time.sleep(5)
        end_time = self.get_current_time()
        assert end_time == start_time, (
            "Video is paused but playback time is progressing; "
            "player controls may be missing or seek-bar is moving."
        )

    def is_buffering(self):
        """
        Check if the video is buffering.
        readyState < 3 indicates buffering or insufficient data to play.
        :return: True if buffering, False otherwise
        """
        return self._execute_js("readyState") < 3

    def assert_is_not_buffering(self):
        """
        Assert that the video is not buffering.
        Raises AssertionError if buffering is detected.
        """
        assert not self.is_buffering(), "Video is buffering!"

    def get_current_playing_video_title(self):
        """
        Get the title of the currently playing video from the player UI.
        :return: video title string
        """
        return self.driver.find_element(By.XPATH, Player_Locators.CURRENT_PLAYING_VIDEO_TITLE).text

    def assert_next_video_title(self, old_title, new_title, video_queue):
        """
        Assert that the next video is playing by comparing titles.
        :param old_title: title before clicking next
        :param new_title: title after clicking next
        :param video_queue: list of video titles in the queue
        """
        assert new_title == video_queue[1] and old_title != new_title, "Next video is not playing."

    def assert_previous_video_title(self, old_title, new_title, video_queue):
        """
        Assert that the previous video is playing by comparing titles.
        :param old_title: title before clicking previous
        :param new_title: title after clicking previous
        :param video_queue: list of video titles in the queue
        """
        assert new_title == video_queue[0] and old_title == new_title, "Previous video is not playing."

    def click_button(self, button_xpath):
        """
        Click a button on the player identified by its XPath.
        :param button_xpath: XPath locator of the button
        """
        self.driver.find_element(By.XPATH, button_xpath).click()

    def wait_for_ads_to_finish(self, timeout=6):
        """
        Wait for any ads to finish playing before the main video starts.
        Handles both skippable and non-skippable ads.
        Attempts to click the skip button if available.
        """
        while True:
            is_ad_playing = self.driver.execute_script(
                "return document.querySelector('.ytp-ad-player-overlay') !== null"
            )
            if not is_ad_playing:
                break
            try:
                skip_button = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, Player_Locators.SKIP_BUTTON))
                )
                skip_button.click()
            except TimeoutException:
                # Wait until the skip button disappears or ad ends
                time.sleep(timeout*2)

    def wait_until_video_ready(self, timeout=10):
        """
        Wait until the video element is ready to play.
        readyState >= 2 means the video has enough data to play the current frame.
        Raises Exception if video is not ready within timeout.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.querySelector('video')?.readyState >= 2")
            )
        except TimeoutException:
            raise Exception("Video did not become ready within the given timeout.")



'''
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Player_Locators

class PlayerPage:
    def __init__(self, driver):
        self.driver = driver
        self.player = self.get_video_element()

    def get_video_element(self):
        """Returns the video element on YouTube Music."""
        video = self.driver.execute_script("return document.querySelector('video');")
        return video

    def execute_js(self, command, *args):
        """Executes JavaScript on the video element."""
        return self.driver.execute_script(f'return arguments[0].{command}', self.player, *args)

    def play(self):
        """Plays the video."""
        self.driver.find_element(By.TAG_NAME, 'body').click()
        self.execute_js("play()")

    def pause(self):
        """Pauses the video."""
        self.execute_js("pause()")

    def seek(self, seconds):
        """Seeks the video to a specific time in seconds."""
        self.execute_js("currentTime = arguments[1]", seconds)

    def set_volume(self, level):
        """Sets the video volume (0.0 to 1.0)."""
        self.execute_js("volume = arguments[1]", level)

    def get_currenttime(self):
        """Changes playback speed."""
        return self.execute_js("currentTime")

    def assert_is_playing(self):
        """Returns True if the video is playing, otherwise False."""
        assert not self.execute_js("paused"), "Video is not playing!"
        current_time_1 = self.get_currenttime()
        print(current_time_1)
        time.sleep(5)
        current_time_2 = self.get_currenttime()
        assert current_time_2 > current_time_1, "Although, video is playing but either player controls are missing or video is NOT progressing!"

    def assert_not_playing(self):
        """Returns True if the video is playing, otherwise False."""
        assert self.execute_js("paused"), "Video is playing!"
        current_time_1 = self.get_currenttime()
        time.sleep(5)  # Wait for 2 seconds
        current_time_2 = self.get_currenttime()
        assert current_time_2 == current_time_1, "Although, video is paused but either player controls are missing or seek-bar is progessing."

    def get_currentplaying_videotitle(self):
        videotile = self.driver.find_element(By.XPATH, Player_Locators.CURRENT_PLAYING_VIDEO_TITLE).text
        return videotile

    def assert_next_video_title(self, oldvideotitle, newvideotitle, videoqueue):
        assert newvideotitle == videoqueue[1] and oldvideotitle != newvideotitle, "Next video is not playing."

    def assert_previous_video_title(self, oldvideotitle, newvideotitle, videoqueue):
        assert newvideotitle == videoqueue[0] and oldvideotitle == newvideotitle, "Previous video is not playing."

    def click_button(self, button):
        self.driver.find_element(By.XPATH, button).click()

    def wait_for_ads_to_finish(self, timeout=10):
        # Handles multiple skippable and non-skippable ads before main video starts.
        while True:
            is_ad_playing = self.driver.execute_script("return document.querySelector('.ytp-ad-player-overlay');")

            if not is_ad_playing:
                break
            # Attempt to skip if skip button is visible
            try:
                skip_btn = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(
                    (By.XPATH, Player_Locators.SKIP_BUTTON)))
                skip_btn.click()
            except:
                WebDriverWait(self.driver, timeout * 3).until_not(
                    EC.presence_of_element_located((By.XPATH, Player_Locators.SKIP_BUTTON))
                    # ((By.CSS_SELECTOR, ".ytp-ad-player-overlay"))
                )
'''
'''
    def wait_until_video_ready(self, timeout=10):
        """Waits until the video is fully ready to play."""
        """
            What readyState >= 2 Means:
            0: No info yet. || 1: Metadata loaded.2: Current data available (can play current frame).
            3: Can play, buffering may occur. || 4: Fully buffered, can play without stopping.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.querySelector('video')?.readyState >= 2")
            )
        except TimeoutException:
            raise Exception("Video did not become ready within the given timeout.")
'''