from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de capacidades
options = UiAutomator2Options()
options.deviceName = 'Android'
options.platformName = 'Android'
options.browserName = 'Chrome'
options.automationName = 'UiAutomator2'

# Inicializar el driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

try:
    # Abrir la página de Google
    driver.get("http://google.com")
    
    # Esperar a que el campo de búsqueda esté presente
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@class='android.widget.EditText']"))
    )
    
    # Interactuar con el campo de búsqueda
    search_box.send_keys("Hello Appium")
    
    # Imprimir el título de la página
    # page_title = driver.execute_script("return document.title;")
    # print(f"Page title: {page_title}")
finally:
    # Esperar un momento y cerrar el navegador
    time.sleep(5)
    driver.quit()
