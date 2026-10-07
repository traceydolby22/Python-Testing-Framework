from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimoutException
from view_helpers import dismiss_debug_banner

class LoginPage: 
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        #checks if debug warning is present on app view
        dismiss_debug_banner(self.driver)

        #welcome view - tap sign in 
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.IOS_PREDICATE, "label == 'Sign in', AND type == 'XCUIElementTypeButton'")))

        self.driver.find_element(
            AppiumBy.IOS_PREDICATE, "label == 'Sign in' AND type == 'XCUIElementTypeButton'").click()

        WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"email-input")))

        email_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "email-input")
        email_field.click()
        email_field.send_keys(email)

        password_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password-input")
        password_field.click()
        password_field.send_keys(password)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "log-in-button").click()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"dashboard")))
        