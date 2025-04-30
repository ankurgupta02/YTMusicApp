from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class Common_Helpers:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locator, element="Element", timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            assert False, f"Either {element} didn't load on page or missing."

    def get_a_random_video(self, items):
        return random.randint(1, len(items))

    def move_and_click_to_element(self, element):
        act = ActionChains(self.driver)
        act.move_to_element(element).click().perform()