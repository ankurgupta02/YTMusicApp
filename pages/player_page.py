import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def set_playback_speed(self, speed):
        """Changes playback speed."""
        self.execute_js("playbackRate = arguments[1]", speed)

    def get_currenttime(self):
        """Changes playback speed."""
        return self.execute_js("currentTime")

    def assert_is_playing(self):
        """Returns True if the video is playing, otherwise False."""
        assert not self.execute_js("paused"), "Video is not playing!"
        current_time_1 = self.get_currenttime()
        time.sleep(5)
        current_time_2 = self.get_currenttime()
        assert current_time_2 > current_time_1, "Although, video is playing but either player controls are missing or video is NOT progressing!"

    def assert_not_playing(self):
        """Returns True if the video is playing, otherwise False."""
        assert self.execute_js("paused"), "Video is not playing!"
        current_time_1 = self.get_currenttime()
        time.sleep(5)  # Wait for 2 seconds
        current_time_2 = self.get_currenttime()
        assert current_time_2 == current_time_1, "Although, video is paused but either player controls are missing or seek-bar is progessing."


    def is_buffering(self):
        """Checks if the video is buffering."""
        return self.execute_js("readyState") < 3


    def assert_is_not_buffering(self):
        """Asserts that the video is not buffering."""
        assert not self.is_buffering(), "Video is buffering!"

    def assert_currentplaying_videotitle(self):
        videotile = self.driver.find_element(By.XPATH,
                                             "//yt-formatted-string[@class='title style-scope ytmusic-player-bar']").text
        return videotile

    def wait_for_currentplayingvideotitle_to_load(self):
        try:
            # Waits for a specific element to be visible on the page, indicating the page has loaded.
            element_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//yt-formatted-string[@class='title style-scope ytmusic-player-bar']"))
                                                                      # Change to your preferred locator
                                                                      )
        except TimeoutException:
            assert True, "Element not found"

    def play_next_song(self):
        next_button = self.driver.find_element("xpath", "//tp-yt-paper-icon-button[@title='Next song']")
        next_button.click()
        print("Skipped to the next song.")
        time.sleep(2)

    def toggle_shuffle(self):
        shuffle_button = self.driver.find_element("xpath", "//tp-yt-paper-icon-button[@title='Shuffle']")
        shuffle_button.click()
        print("Toggled shuffle mode.")
        time.sleep(2)

    def toggle_loop(self):
        loop_button = self.driver.find_element("xpath", "//tp-yt-paper-icon-button[@title='Repeat']")
        loop_button.click()
        print("Toggled loop mode.")
        time.sleep(2)

    def skip_ads(self):
        """Detects and skips ads if present."""
        while True:
            try:
                ad_skip_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Skip Ad')]")
                ad_skip_button.click()
                print("⏭ Skipped an ad!")
                time.sleep(2)
            except:
                break  # No ads detected

    def wait_until_video_ready(self, timeout=10):
        """Waits until the video is fully ready to play."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            ready_state = self.driver.execute_script("return document.querySelector('video').readyState")
            if ready_state >= 2:
                return True
            time.sleep(0.5)
        raise Exception("Video did not become ready in time.")
    def wait_for_ads_to_finish(self, timeout=20):
        """
        Handles multiple skippable and non-skippable ads before main video starts.
        """

        while True:
            is_ad_playing = self.driver.execute_script(
                "return document.querySelector('.ytp-ad-player-overlay');"
            )

            if not is_ad_playing:
                print("No more ads.")
                break

            # Attempt to skip if skip button is visible
            try:
                ad_skip_button= WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button-modern')]")))
                ad_skip_button.click()
                print("⏭ Skipped an ad!")
            except:
                print("Clicked Skip Ad not availble.")
                pass


    def wait_for_ads_to_finish_old(self, timeout=20):
        """
        Handles multiple skippable and non-skippable ads before main video starts.
        """
        end_time = time.time() + timeout

        while time.time() < end_time:
            is_ad_playing = self.driver.execute_script(
                "return document.querySelector('.ytp-ad-player-overlay');"
            )

            if not is_ad_playing:
                print("No more ads.")
                return True
            time.sleep(5)
            # Attempt to skip if skip button is visible
            try:
                ad_skip_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button-modern ytp-button')]")
                ad_skip_button.click()
                print("⏭ Skipped an ad!")
                time.sleep(2)
            except:
                print("Clicked Skip Ad not availble.")
                # No skip button yet

            time.sleep(2)  # Wait and re-check
            # Loop continues until ad ends or another one starts

        raise TimeoutError("Ad(s) did not finish within the timeout.")









'''
What readyState >= 2 Means:
0: No info yet.
1: Metadata loaded.2: Current data available (can play current frame).
3: Can play, buffering may occur.
4: Fully buffered, can play without stopping.
'''
