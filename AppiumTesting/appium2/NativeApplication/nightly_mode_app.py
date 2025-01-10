import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import PointerInput
from selenium.webdriver.common.actions import interaction


options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "192.168.1.64:5555"
options.deviceName = "Android"
options.automationName = "UiAutomator2"
options.appPackage = "com.eyefilter.nightmode.bluelightfilter"
options.appActivity = "com.eyefilter.nightmode.bluelightfilter/com.eyefilter.nightmode.bluelightfilter.ui.MainActivity"
options.noReset = True


driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
# Launch 'manually' the calculator app
driver.execute_script("mobile: shell", {
        "command": "monkey",
        "args": ["-p", "com.eyefilter.nightmode.bluelightfilter", "-c", "android.intent.category.LAUNCHER", "1"]
})

# 1. Click on the candel
driver.find_element(AppiumBy.XPATH, "//android.widget.RelativeLayout[@resource-id='com.eyefilter.nightmode.bluelightfilter:id/ly_color_1']").click()
time.sleep(2)
# 2. Click on bulb
driver.find_element(AppiumBy.XPATH, "//android.widget.RelativeLayout[@resource-id='com.eyefilter.nightmode.bluelightfilter:id/ly_color_4']").click()
time.sleep(2)
# 3. click on sun
driver.find_element(AppiumBy.XPATH, "//android.widget.RelativeLayout[@resource-id='com.eyefilter.nightmode.bluelightfilter:id/ly_color_6']").click()
time.sleep(2)
# 4. Click on the switch
driver.find_element(AppiumBy.XPATH, "//android.widget.Switch[@resource-id='com.eyefilter.nightmode.bluelightfilter:id/filter_switch']").click()
time.sleep(2)
# 4. Click on the switch
driver.find_element(AppiumBy.XPATH, "//android.widget.Switch[@resource-id='com.eyefilter.nightmode.bluelightfilter:id/filter_switch']").click()
time.sleep(2)
target_position = 0.5
action = ActionChains(driver)
window_size = driver.get_window_size()
x, y = window_size['width'] / 6, window_size['height'] / 2
distance = start_x + (size['width'] * target_position)
action.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
action.w3c_actions.pointer_action.move_to_location(x + distance, y)
action.w3c_actions.pointer_action.click_and_hold()
# action.w3c_actions.pointer_action.move_to_location(x, y - distance)
action.w3c_actions.pointer_action.release()
action.w3c_actions.perform()



# 5. Move the seekbar
# seekbar = driver.find_element(AppiumBy.ID, "com.eyefilter.nightmode.bluelightfilterid/seekbar")
# size = seekbar.size  # Get size
# location = seekbar.location  # Get Location

# start_x = location['x']  # initial coordinates on X
# end_x = start_x + size['width']  # Final coo in X
# y = location['y'] + (size['height'] // 2) # Coo in Y

# # Calcular posición deseada (50%)
# target_position = 0.5  # Porcentaje deseado (por ejemplo, 50%)
# target_x = start_x + (size['width'] * target_position)

# # Deslizar el SeekBar
# touch_action = TouchAction(driver)
# touch_action.press(x=start_x, y=y).move_to(x=target_x, y=y).release().perform()
driver.quit()

