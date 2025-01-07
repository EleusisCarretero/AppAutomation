from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
options = UiAutomator2Options()
options.platformName="Android"
options.deviceName = "192.168.1.64:5555"
options.automationName = "UiAutomator2"
options.appPackage = "com.sec.android.app.popupcalculator"
options.appActivity = "com.sec.android.app.popupcalculator.Calculator"

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
# Launch 'manually' the calculator app
driver.execute_script("mobile: shell", {
    "command": "am start",
    "args": ["-n", "com.sec.android.app.popupcalculator/.Calculator"]
    })

time.sleep(3)
driver.quit()
