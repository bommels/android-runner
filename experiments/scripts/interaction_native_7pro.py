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
    time.sleep(4) # wait pop up to dissabear
    #tap(device, 362, 946) # Remove pop up
    tap(device, 382, 240) # print('search')
    write_text(device, 'Desk') # print('search write')
    tap(device, 1314, 2808) # print('search btn')
    while True: # Keep repeating
        swipe(device, 576, 2339, 576, 467)
        tap(device, 279, 227) # print('search')
        tap(device, 1125, 227) # clear search
        write_text(device, 'Desk') # print('search write')
        tap(device, 1314, 2808) # print('search btn')

def scenarioNativeTripAdvisor7pro(device: Device, isFirstRun): # FIXME not taking the first run accept cookies?
    # if isFirstRun:
    tap(device, 387, 970) # set preferences
    tap(device, 558, 925) # Privacy Notice
    tap(device, 1345, 234) # do not login 
    # tap(device, 702, 1417) # location not now
    tap(device, 711, 487) # where to
    write_text(device, 'Amsterdam')
    tap(device, 391, 598) # click first
    tap(device, 256, 1020) # Hotels
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 1341, 227) # search
        write_text(device, 'Hotels')
        tap(device, 369, 598) # click first result

def scenarioNativeDeliveroo7pro(device: Device, isFirstRun):
    #if isFirstRun:
    # tap(device, 715, 1859) # Deny location
    tap(device, 877, 1729) # no thanks location service
    tap(device, 1359, 221) # Search location btn
    write_text(device, 'Amsterdam')
    tap(device, 486, 468) # Top result
    tap(device, 751, 2782) # Confirm location
    tap(device, 1341, 227) # Skip
    tap(device, 738, 2119) # Ok
    while True:
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)

def scenarioNative9GAG7pro(device: Device, isFirstRun):
    #time.sleep(2) # wait for cookies
    #if isFirstRun:
    tap(device, 769, 2170) # Consent
    while True:
        tap(device, 531, 383) # Press Trending
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)
        tap(device, 189, 383) # Press Hot
        swipe(device, 576, 2339, 576, 467)
        swipe(device, 576, 467, 576, 2339)

def scenarioNativeReddit7pro(device: Device, isFirstRun):
    #if isFirstRun:
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
    #if isFirstRun:
    tap(device, 738, 2691) # Next 
    tap(device, 720, 2496) # I understand
    tap(device, 738, 2509) # I understand
    tap(device, 877, 1729) # no thanks location service
        # tap(device, 738, 1943) # Deny
    while True:
        write_text(device, 'Amsterdam')
        tap(device, 1305, 2821) # Search
        tap(device, 513, 604) # Top result
        swipe(device, 576, 2339, 576, 467) # down
        swipe(device, 576, 467, 576, 2339) # up
        tap(device, 391, 227) # search top

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
    #if isFirstRun:
    tap(device, 540, 1131) # Other region
    tap(device, 225, 591) # Search region
    write_text(device, 'United States')
    tap(device, 391, 877) # Top result
    tap(device, 751, 1209) # Continue
    tap(device, 391, 2814) # Don't allow notification
        # tap(device, 747, 1865) # Deny
    tap(device, 130, 2853) # Search
    while True:
        tap(device, 292, 240) # Search bar focus
        write_text(device, 'Shoes')
        tap(device, 1323, 2814) # Keyboard search
        
        swipe(device, 576, 2339, 576, 467)
        tap(device, 337, 923) # Click on shoe
        tap(device, 126, 247) # Back cross
        tap(device, 1305, 221) # Clear search bar input 

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