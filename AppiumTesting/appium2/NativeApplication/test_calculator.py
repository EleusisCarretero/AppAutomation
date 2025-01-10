import random
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class CalculatorManagerError(Exception):
    pass

class CalculatorManager:

    base_xpath = "//android.widget.Button[@content-desc='{button}']"
    def __init__(self, calculator_driver):
        self.calculator_driver = calculator_driver
    
    def _click_on_button(self, button):
        e = None
        try:
            button_obj = self.calculator_driver.find_element(AppiumBy.XPATH, self.base_xpath.format(button=button))
        except Exception as e:
            print("Unable to found the element")
        if e is None:
            button_obj.click()
    
    def click_on_number(self, number):

        if number not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            raise CalculatorManagerError("parameter 'number' should be a value between [0-9]")
        self._click_on_button(number)
    
    def _click_on_operation(self, operation):
        if operation not in ["Clear", "Brackets", "Percentage", "Division", "Multiplication", "Minus", "Plus", "Calculation"]:
            raise CalculatorManagerError("parameter 'operation' should be valid operation")
        self._click_on_button(operation)

    def perform_sum(self):
        self._click_on_operation("Plus")
    
    def perform_calculation(self):
        self._click_on_operation("Calculation")



if __name__ == "__main__":
    # options = UiAutomator2Options()
    # options.platformName="Android"
    # options.deviceName = "Android"
    # options.automationName = "UiAutomator2"
    # options.appPackage = "com.sec.android.app.popupcalculator"
    # options.appActivity = "com.sec.android.app.popupcalculator.Calculator"

    
    desired_caps = dict(
        platformName="Android",
        deviceName = "Android",
        automationName = "UiAutomator2",
        appPackage = "com.sec.android.app.popupcalculator",
        appActivity = "com.sec.android.app.popupcalculator.Calculator"
    )
    options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    # Launch 'manually' the calculator app
    driver.execute_script("mobile: shell", {
        "command": "am start",
        "args": ["-n", "com.sec.android.app.popupcalculator/.Calculator"]
        })

    local_calc = CalculatorManager(calculator_driver=driver)
    local_calc.click_on_number(9)
    local_calc.perform_sum()
    local_calc.click_on_number(9)
    local_calc.perform_calculation()


    time.sleep(3)
    driver.quit()
