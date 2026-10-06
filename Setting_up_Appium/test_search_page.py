from socket import timeout
import time
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from collections_page import CollectionsPage
from appium.webdriver.common.appiumby import AppiumBy
from view_helpers import wait_for_element, tap_percent

def test_search_web(driver, WebDriver):
    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, 'Search'))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search').click()

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, 'Search field'))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'open flowers.com').click()

    def is_present(driver, locator, timeout=10):
        try: 
            wait_for_element(driver, locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    #coupon pop up on website. 
    wait_for_element(driver, (AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Enter email to use code at checkout, form']/XCUIElementTypeOther[1]/XCUIElementTypeOther" ), timeout=10)

    #waits to see if a notif about cookies shows
    if is_present(driver, (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='We use Cookies']")):
            driver.find_element(AppiumBy.XPATH, "//*[contains(@name, 'Close icon')]")

    #waits to see if a pop up for coupon shows up on webview
    if is_present(driver, (AppiumBy.XPATH, "//*[contains(@name, 'Unlock')]")):
        driver.find_element(AppiumBy.XPATH, "//*[contains(@name, 'Not Interested')]")

    wait_for_element(driver, (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Link Actions'])[2]"), timeout=10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Copy Link").click()

    # clicks the Close button on webview
    tap_percent(driver, 0.11, 0.12)
    wait_for_element(driver, (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[@Name='Search])[2]"), timeout=10)