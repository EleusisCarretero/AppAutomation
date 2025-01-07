import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Configuración del dispositivo
options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "192.168.1.64:5555"  # Verifica con 'adb devices'
options.automationName = "UiAutomator2"
options.appPackage = "com.samsung.android.dialer"
options.appActivity = ".DialtactsActivity"
options.noReset = True
options.newCommandTimeout = 300



# Conexión con el servidor Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

driver.find_element(AppiumBy.ID,'com.android.dialer:id/one').click()
driver.find_element(AppiumBy.ID,'com.android.dialer:id/two').click()
driver.find_element(AppiumBy.ID,'com.android.dialer:id/three').click()
driver.find_element(AppiumBy.ID,'com.android.dialer:id/five').click()

driver.find_element(AppiumBy.ID,'com.android.dialer:id/dialButtonSim1').click()


time.sleep(2)
driver.quit()
