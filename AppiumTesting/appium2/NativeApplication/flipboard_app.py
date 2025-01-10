import random
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


if __name__ == "__main__":
    desired_caps = dict(
        platformName="Android",
        deviceName = "192.168.1.64:5555",
        automationName = "UiAutomator2",
        appPackage = "flipboard.app",
        appActivity = "flipboard.activities.LaunchActivityAlias"
    )
    options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    # Get started
    driver.find_element(AppiumBy.ID, "flipboard.app:id/first_launch_get_started_button").click()
    # Chose options
    driver.find_elements(AppiumBy.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag")[0].click()
    driver.find_elements(AppiumBy.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag")[1].click()
    driver.find_elements(AppiumBy.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag")[2].click()
    # continue
    driver.find_element(AppiumBy.ID, "flipboard.app:id/topic_picker_continue_button").click()
    # skip
    driver.find_element(AppiumBy.ID, "flipboard.app:id/account_login_buttons_skip").click()
    #swipe 
    duration = 1000
    _times = 4
    for x, y, step_y in [(930, 1000, -400), (930, 1000, 4000)]:
        for _ in range(_times):
            driver.swipe(x,y,x,y + step_y, duration=duration)
            time.sleep(1)
    time.sleep(3)
    for x, y, step_x in [(930, 1000, -800), (120, 1000, 800)]:
        for _ in range(2):
            driver.swipe(x,y,x+step_x,y, duration=duration)
            time.sleep(1)

    driver.quit()
