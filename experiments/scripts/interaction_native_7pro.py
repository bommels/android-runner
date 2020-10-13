import logging
import time
from AndroidRunner.Device import Device
from AndroidRunner.Experiment import Experiment

logger = logging.getLogger(__name__)

def tap(device: Device, x: int, y: int, sleep = 4):
    device.shell("input tap %s %s" % (x, y)) # somehow stops after this...
    time.sleep(sleep)

def write_text(device: Device, text: str, sleep = 1):
    device.shell('input text \'%s\'' % text)
    time.sleep(sleep)

def swipe(device: Device, x1: int, y1: int, x2: int, y2: int, sleep = 4, duration = 1000):
    device.shell('input swipe %s %s %s %s %s' % (x1, y1, x2, y2, duration))
    time.sleep(sleep)

def scenarioNativeAliExpress7pro(device: Device, isFirstRun):
    # if isFirstRun:
    tap(device, 362, 946) # Remove pop up
    tap(device, 281, 93) # print('search')
    write_text(device, 'Shoes') # print('search write')
    tap(device, 661, 1218) # print('search btn')
    while True: # Keep repeating
        swipe(device, 576, 2339, 576, 467)
        tap(device, 31, 90) # print('search')
        tap(device, 560, 93) # clear search
        write_text(device, 'Shoes') # print('search write')
        tap(device, 661, 1218) # print('search bt

def scenarioNativeBooking7pro(device: Device, isFirstRun): # FIXME not taking the first run accept cookies?
    print(isFirstRun)
    if isFirstRun:
        tap(device, 1071, 2756) # accept cookies
    tap(device, 99, 221) # Do not login
    tap(device, 769, 1352) # Search bar 
    write_text(device, 'Amsterdam')
    tap(device, 711, 403) # Top result
    tap(device, 724, 2762) # Select dates
    tap(device, 702, 1917) # Blue search btn
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 81, 169) # Back
        tap(device, 769, 1352) # Search bar 
        write_text(device, 'Amsterdam')
        tap(device, 711, 403) # Top result
        tap(device, 724, 2762) # Select dates
        tap(device, 702, 1917) # Blue search btn

def scenarioNativeDeliveroo7pro(device: Device, isFirstRun):
    if isFirstRun:
        tap(device, 459, 725) # Deny location
        tap(device, 672, 93) # Search location btn
        write_text(device, 'Amsterdam')
        tap(device, 193, 194) # Top result
        tap(device, 369, 1221) # Confirm location
        tap(device, 659, 90) # Skip
        tap(device, 351, 994) # Ok
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)

def scenarioNative9GAG7pro(device: Device, isFirstRun):
    time.sleep(2) # wait for cookies
    if isFirstRun:
        tap(device, 375, 970) # Consent
    while True:
        tap(device, 265, 173) # Press Trending
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 85, 181) # Press Hot
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)

def scenarioNativeReddit7pro(device: Device, isFirstRun):
    if isFirstRun:
        tap(device, 702, 2860) # continue without account
    while True:
        tap(device, 270, 591) # Press hot
        tap(device, 243, 2470) # Change top
        tap(device, 274, 2788) # All time
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 346, 591) # Press top
        tap(device, 265, 2119) # Change hot
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)

def scenarioNativeWeather7pro(device: Device, isFirstRun):  # FIXME first run also?
    if isFirstRun:
        tap(device, 365, 1160) # Next 
        tap(device, 353, 1064) # I understand
        tap(device, 344, 1074) # I understand
        tap(device, 459, 744) # Deny
    while True:
        write_text(device, 'Amsterdam')
        tap(device, 657, 1216) # Search
        tap(device, 263, 242) # Top result
        swipe(device, 576, 2339, 576, 467) # down
        swipe(device, 576, 467, 576, 2339) # up
        tap(device, 67, 82) # search top

def scenarioNativeYoutube7pro(device: Device, isFirstRun):
    # if isFirstRun:
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 213, 1240) # Explore
        tap(device, 200, 173) # Trending
        tap(device, 288, 448) # First video
        swipe(device, 346, 250, 364, 1124)
        tap(device, 672, 1144) # Cancel video
        tap(device, 42, 85) # Return to youtube home page

def scenarioNativeZara7pro(device: Device, isFirstRun):
    if isFirstRun:
        tap(device, 285, 528) # Other region
        tap(device, 204, 280) # Search region
        write_text(device, 'United States')
        tap(device, 285, 445) # Top result
        tap(device, 407, 586) # Continue
        tap(device, 227, 1210) # Don't allow notification
        # tap(device, 450, 744) # Deny
    while True:
        tap(device, 56, 1234) # Search
        tap(device, 173, 85) # Search bar focus
        write_text(device, 'Shoes')
        tap(device, 650, 1208) # Keyboard search
        swipe(device, 288, 1204, 288, 204) 
        tap(device, 162, 389) # Click on shoe
        tap(device, 56, 106) # Back cross
        tap(device, 49, 93) # Clear search bar input 

def main(device, *args, **kwargs):
    # FIXME takes for ever to get here
    print('=INTERACTION=')
    print((device))
    print((device.id))
    print((device.current_activity()))
    isFirstRun = args[1][1] # If apps are not reinstalled every time.

    if device.current_activity().find('com.alibaba.aliexpresshd') != -1:
        print('running aliexpress')
        scenarioNativeAliExpress7pro(device, isFirstRun)
    elif device.current_activity().find('com.booking') != -1:
        print('running booking')
        scenarioNativeBooking7pro(device, isFirstRun)
    elif device.current_activity().find('com.deliveroo.orderapp') != -1:
        print('running deliveroo')
        scenarioNativeDeliveroo7pro(device, isFirstRun)
    elif device.current_activity().find('com.reddit.frontpage') != -1:
        print('running reddit')
        scenarioNativeReddit7pro(device, isFirstRun)
    elif device.current_activity().find('com.ninegag.android.app') != -1:
        print('running 9gag')
        scenarioNative9GAG7pro(device, isFirstRun)
    elif device.current_activity().find('com.weather') != -1:
        print('running weather')
        scenarioNativeWeather7pro(device, isFirstRun)
    elif device.current_activity().find('com.google.android.youtube') != -1:
        print('running youtube')
        scenarioNativeYoutube7pro(device, isFirstRun)
    elif device.current_activity().find('com.inditex.zara') != -1:
        print('running zara')
        scenarioNativeZara7pro(device, isFirstRun)
    else:
        raise Exception('There is no known interaction script for this subject')