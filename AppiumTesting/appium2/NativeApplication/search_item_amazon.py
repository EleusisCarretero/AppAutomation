from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()
options.platformName = "Android"
# options.deviceName = "192.168.1.64:5555"
options.deviceName = "Android"
options.automationName = "UiAutomator2"
options.appPackage = "com.amazon.mShop.android.shopping"
options.appActivity = "com.amazon.mShop.startup.StartupLocalizationSelectionActivity"
# options.noReset = True  # Conserva sesión si existe
# options.autoGrantPermissions = True
# options.fullReset = False
# options.appWaitActivity = "com.amazon.mShop.kuber.rendering.activity.KuberRenderingActivity"

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
# Launch 'manually' the calculator app
driver.execute_script("mobile: shell", {
        "command": "monkey",
        "args": ["-p", "com.amazon.mShop.android.shopping", "-c", "android.intent.category.LAUNCHER, 1"]
})

# 1. Click on 'País' /'Region
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='País/región: México']").click()
time.sleep(2)
# 2. Select 'Estados unidos'
wait_country_list = WebDriverWait(driver,5)
wait_country_list.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.RadioButton[@resource-id='pref-option-group-primary-opt-2']"))).click()
# 3. Select 'México' again
driver.find_element(AppiumBy.XPATH, "//android.widget.RadioButton[@resource-id='pref-option-group-primary-opt-0']").click()
# 4. Click on 'Idioma'
main_menu = WebDriverWait(driver,5)
wait_country_list.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='Idioma: español']"))).click()
# 5. Select 'Chino simplificado'
wait_language_list = WebDriverWait(driver,5)
wait_country_list.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.RadioButton[@resource-id='pref-option-group-secondary-opt-2']"))).click()
# 6. Select 'Español' again
driver.find_element(AppiumBy.XPATH, "//android.widget.RadioButton[@resource-id='pref-option-group-primary-opt-0']").click()
# 7. Click on Finalizar
wait_country_list.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='Finalizado']"))).click()

