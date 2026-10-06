from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

options = XCUITestOptions()
options.platform_name = 'iOS'
options.device_name = 'iPhone 17 Pro'
options.app = '/Users/traceybernstein/Library/Developer/Xcode/DerivedData/companyRepo-Datakey/Build/Products/Debug-iphonesimulator/companynamerepo.app'


options.set_capabilities('autoAcceptAlerts', True)

driver = webdriver.Remote('https://addserver:addport', options=options)