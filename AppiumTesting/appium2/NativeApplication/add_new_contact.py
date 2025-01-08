import random
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platformName="Android"
options.deviceName = "192.168.1.64:5555"
options.automationName = "UiAutomator2"
options.appPackage = "com.samsung.android.dialer"
options.appActivity = ".DialtactsActivity"

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
# Launch 'manually' the calculator app
driver.execute_script("mobile: shell", {
        "command": "am start",
        "args": ["-n", "com.samsung.android.dialer/.DialtactsActivity"]
})

# Click on 'contacts' button
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Contacts, Selected"]').click()
time.sleep(2)

#Create contact button
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Create contact"]').click()
time.sleep(2)

#Write contact
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.samsung.android.app.contacts:id/nameEdit"]').send_keys("DummyTest:Juan Guarnizo")
time.sleep(2)
# Click on number
driver.find_element(AppiumBy.XPATH,'(//android.widget.RelativeLayout[@resource-id="com.samsung.android.app.contacts:id/titleLayout"])[1]').click()
time.sleep(2)

# Write number
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@text="Phone"]').send_keys("15151515")
time.sleep(2)

#Save contact
driver.find_element(AppiumBy.ID,'com.samsung.android.app.contacts:id/menu_done').click()
time.sleep(2)


driver.quit()
