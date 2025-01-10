import random
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


if __name__ == "__main__":
    desired_caps = dict(
        platformName="Android",
        deviceName = "Android",
        automationName = "UiAutomator2",
        appPackage = "com.samsung.android.dialer",
        appActivity = "com.samsung.android.dialer.DialtactsActivity"
    )
    options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    # click on contacts button
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Contacts, Selected"]').click()
    # Scroll untill it founds an object with name "Betzabe"
    obj = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Betzabe").instance(0))')
    # Click on contact found
    obj.click()
    # Scroll up and down
    duration = 1000
    for x, y, step_y in [(514, 600, -400), (514, 500, 300)]:
        for _ in range(5):
            driver.swipe(x,y,x,y + step_y, duration=duration)


    


    time.sleep(3)
    driver.quit()
