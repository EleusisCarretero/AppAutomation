import time
from appium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Configuración de opciones
options = UiAutomator2Options()
options.deviceName = 'Android'
options.platformName = 'Android'
options.browserName = 'Chrome'
# options.automationName = 'UiAutomator2'

# Inicia el driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Abre Wikipedia
driver.get("http://wikipedia.org")
# print(driver.title)

# Espera explícita para el dropdown
print(driver.contexts)  # Lista todos los contextos disponibles
driver.switch_to.context("WEBVIEW_chrome")  # Cambia al contexto WebView

# wait = WebDriverWait(driver, 10)
# dropdown = wait.until(EC.presence_of_element_located(AppiumBy.ID, "searchLanguage"))
dropdown = driver.find_element(AppiumBy.XPATH, "//select[@id='searchLanguage']")

# Selecciona el idioma
select = Select(dropdown)
select.select_by_value("hi")

# Encuentra y cuenta las opciones
options_elements = driver.find_elements(By.TAG_NAME, "option")
print(len(options_elements))

# Imprime texto y atributo "Lang" de cada opción
for option in options_elements:
    print("Text is:", option.text, "Lang is:", option.get_attribute('lang'))

# Finaliza el driver
time.sleep(2)
driver.quit()