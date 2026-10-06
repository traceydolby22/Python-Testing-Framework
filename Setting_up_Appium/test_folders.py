import time

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from collections_page import CollectionsPage
from appium.webdriver.common.appiumby import AppiumBy
from view_helpers import dismiss_phots_permissions, wait_for_element, tap_percent

def test_create_folders(driver: WebDriver):

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "home"))

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Folder"))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Folder").click()

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "folders"), timeout=10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "folders").click()

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Open create menu"))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Open create menu").click()

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Create a Folder"))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create a Folder").click()

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Create Folder"))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create Folder").click()

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Add photo"))
    driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Choose from Library']").click()

    dismiss_phots_permissions(driver)
    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Photos"), timeout=10)
    # taps an area on an iOS view where pictures are selectable. 
    tap_percent(driver, 0.17, 0.45)
    tap_percent(driver, 0.85, 0.92)

    wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "choose"))
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "choose").click()

    