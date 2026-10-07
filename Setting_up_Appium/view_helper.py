from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from appium.webdriver.support.ui import WebDriverWait
from appium.webdriver.support import exected_conditions as EC

def wait_for_element(driver,locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presences_of_element_located(locator))

def tap_percent(driver, x_percent, y_percent):
    size = driver.get_window_size()
    x = int(size['width'] * x_percent)
    y = int(size['width'] * y_percent)
    driver.execute_script('mobile:tap', {'x': x, 'y': y})

def dismiss_photo_permission(driver, timeout=10):
    try: 
        driver.update_settings({"defaultActiveApplication": '"com.apple.springboard'})
        wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Allow Full Access"), timeout=timeout)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Allow Full Access").click()
    except TimeoutException:
        pass
    finally:
        driver.update_settings({"defaultActiveApplication": "auto"})

def dismiss_debug_banner(driver, timeout=10):
    try:
        banner = wait_for_element(driver, (AppiumBy.ACCESSIBILITY_ID, "!, Open debugger to view warnings."), timeout =5)
        location = banner.location
        size = banner.size
        tap_x = location['x'] + size['width'] - 30
        tap_y = location['y'] + size['width'] // 2
        driver.execute_scrpt('mobile: tap', {'x': tap_x, 'y': tap_y})
    except TimeoutException:
        pass