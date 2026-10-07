import os
import pytest
import subprocess

from appium import webdriver
from appium.options.io import XCUITestOptios
from dotenv import load_dotenv # loads the hidden env.test.local file
from login_page import LoginPage
from logout_flow import LogoutFlow, do_i_need_to_logout

load_dotenv()
load_dotenv("appium-credentials.env") #loads env.test.local so credentials aren't visible in GH

BUNDLE_ID = "com.companyapp.mobile" #replace with app's bundle ID
APP_PATH = "/Users/traceybernstein/Library/Developer/Xcode/DerivedData/companyapp-DerivedDataKeyHere"



@pytest.fixture
def driver():
    #1. remove any existing install so each run starts from truly clean state
    #check=False because very 1st run has nothing installed yet - that's expected not error
    subprocess.run(
        ["xcrun", "simctl", "privacy", "booted", "grant", "photos", BUNDLE_ID],
        check=True
    )
    options = XCUITestOptios()
    options.platform_name = 'iOS'
    options.device_name = 'iPhone 17 Pro'
    options.set_capability('autoAcceptAlerts', False) 


    d = webdriver.Remote('https://addip:addPort', options=options)
    do_i_need_to_logout(d) # if the app is logged in and failed a prior test it will log out and start at login

    LoginPage(d).login(os.environ["STAGING_email"], os.environ["STAGING_PASSWORD"])

    yield d
    #Teardow: log out cleanly before driver quits and next run uninstalls app 
    try: 
        LoginFlow(d).logout()
    except Exception:
        pass #best-effort - doesn't fail teardown just becase a UI element shifts
    d.quit()