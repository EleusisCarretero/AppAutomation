from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# desired_caps = dict(
#     deviceName='Android',
#     platformName='Android',
#     appPackage='com.android.dialer',
#     appActivity='.BBKTwelveKeyDialer'
# )

# capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
# driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)


options = UiAutomator2Options()
options.deviceName = 'Android'
options.appActivity = 'Android'
options.appPackage = 'com.android.dialer'  # Paquete de la app de llamadas
options.appActivity = 'com.android.dialer.DialtactsActivity'  # Actividad principal

# Inicializar el driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)



driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/six').click()


time.sleep(3)
driver.quit()