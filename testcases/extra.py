import time
import undetected_chromedriver as webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

ops = Options()
ops.add_argument("--guest")
ops.add_argument("--disable-sync")
#ops.add_argument("--autoplay-policy=no-user-gesture-required")
driver = webdriver.Chrome(options=ops)
driver.maximize_window()

driver.get("https://music.youtube.com/watch?v=mmkaDi06C2w")
print(time.time())
print(driver.execute_script("return document.querySelector('video').readyState"))


#driver.execute_script("document.querySelector('video').pause();")
time.sleep(5)
driver.find_element(By.TAG_NAME, 'body').click()
driver.execute_script("document.querySelector('video').play();")
time.sleep(5)
#time.sleep(7)
#driver.execute_script("document.querySelector('video').currentTime;")




'''
#scoll the bar
element=driver.find_element(By.XPATH, "//ytmusic-carousel-shelf-renderer[1]//div[1]//ytmusic-carousel[1] //*[@id='items']")
act.move_to_element(element)
time.sleep(5)

# Get the initial scroll position
initial_scroll = driver.execute_script("return arguments[0].scrollLeft;", element)
print(initial_scroll)
# Scroll the element
#driver.execute_script("arguments[0].scrollLeft += 300;", element)
driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth /4;", element)

time.sleep(5)
# Get the new scroll position
new_scroll = driver.execute_script("return arguments[0].scrollLeft;", element)
print(new_scroll)
# Assert that the scroll position has changed
assert new_scroll > initial_scroll, "The shelf did NOT scroll!"
print("The shelf has been scrolled horizontally!")

time.sleep(5)
'''


'''
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
