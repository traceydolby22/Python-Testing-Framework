# Python-Testing-Framework
UI testing framework I've built for a previous company 

I had done this with expo go appium and xcode using visual studio text editor. 

requirements: 
Node.js version ^14.17.0 || ^16.13.0 || >= 18.0.0
NPM version >= 8 

Install appium globally: 
npm i --location=global appium

Verify it runs place in terminal: 
appium  

Install appium Doctor: 
npm install --location=global @appium/doctor

XCode set up that will print your Xcodes /contents/developer path:
xcode select -p

install iOS-specific dependencies via Homebrew if you want to use real devices: 
brew install carthage libimobiledevice usbmuxd ios-deploy

Install XCUITest driver: 
appium driver install xcuitest

Run doctor and check for iOS: 
appium driver doctor xcuitest

Install Python side: 
pip3 install Appium-Python-Client pytest

May need to brew install Python: 
brew install python

Followed by:
python3 -m venv venv
source venv/bin/activate
python3 -m pip install Appium-Python-Client pytest

To run with expo go I needed 3 terminal windows: 
1. appium
2. npx expo start -c or npx expo start ios
3. python3 -m pytest
this allowed the simulator to run and the test code in Visual studio to run. 
