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
    if isFirstRun:
        tap(device, 1255, 2086) # accept cookies
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
        tap(device, 760, 1859) # Deny location
        tap(device, 1377, 253) # Search location btn
        write_text(device, 'Amsterdam')
        tap(device, 409, 474) # Top result
        tap(device, 774, 2821) # Confirm location
        tap(device, 1350, 247) # Skip
        tap(device, 711, 2125) # Ok
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)

def scenarioNative9GAG7pro(device: Device, isFirstRun):
    time.sleep(2) # wait for cookies
    if isFirstRun:
        tap(device, 769, 2170) # Consent
    while True:
        tap(device, 531, 383) # Press Trending
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 189, 383) # Press Hot
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
        tap(device, 756, 2678) # Next 
        tap(device, 706, 2678) # I understand
        tap(device, 733, 2522) # I understand
        tap(device, 729, 1969) # Deny
    while True:
        write_text(device, 'Amsterdam')
        tap(device, 1318, 2808) # Search
        tap(device, 670, 572) # Top result
        swipe(device, 576, 2339, 576, 467) # down
        swipe(device, 576, 467, 576, 2339) # up
        tap(device, 144, 221) # search top

def scenarioNativeYoutube7pro(device: Device, isFirstRun):
    # if isFirstRun:
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 418, 2801) # Explore
        tap(device, 346, 390) # Trending
        tap(device, 774, 877) # First video
        swipe(device, 576, 467, 576, 2339)
        tap(device, 1363, 2665) # Cancel video
        tap(device, 225, 221) # Return to youtube home page

def scenarioNativeZara7pro(device: Device, isFirstRun):
    if isFirstRun:
        tap(device, 432, 1118) # Other region
        tap(device, 373, 611) # Search region
        write_text(device, 'United States')
        tap(device, 382, 884) # Top result
        tap(device, 778, 1189) # Continue
        tap(device, 490, 2821) # Don't allow notification
        tap(device, 711, 1859) # Deny
    while True:
        tap(device, 117, 2853) # Search
        tap(device, 369, 234) # Search bar focus
        write_text(device, 'Shoes')
        tap(device, 1300, 2801) # Keyboard search
        swipe(device, 576, 2339, 576, 467)
        tap(device, 391, 1924) # Click on shoe
        tap(device, 121, 247) # Back cross
        tap(device, 90, 227) # Clear search bar input 

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
    elif device.current_activity().find('com.weather.Weather') != -1:
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