import logging
import time
from AndroidRunner.Device import Device

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

def scenarioNativeAliExpressJ7(device: Device, isFirstRun):
    # if isFirstRun:
    tap(device, 362, 946) # Remove pop up
    tap(device, 281, 93) # print('search')
    write_text(device, 'Shoes') # print('search write')
    tap(device, 661, 1218) # print('search btn')
    while True: # Keep repeating
        swipe(device, 288, 1024, 288, 204)
        tap(device, 31, 90) # print('search')
        tap(device, 560, 93) # clear search
        write_text(device, 'Shoes') # print('search write')
        tap(device, 661, 1218) # print('search bt

def scenarioNativeBookingJ7(device: Device, isFirstRun):
    if isFirstRun:
        tap(device, 348, 1064) # accept cookies
    tap(device, 42, 85) # Do not login
    tap(device, 371, 634) # Search bar 
    write_text(device, 'Amsterdam')
    tap(device, 346, 221) # Top result
    tap(device, 351, 1194) # Select dates
    tap(device, 369, 869) # Blue search btn
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 22, 77) # Back
        tap(device, 371, 634) # Search bar 
        write_text(device, 'Amsterdam')
        tap(device, 346, 221) # Top result
        tap(device, 351, 1194) # Select dates
        tap(device, 369, 869) # Blue search btn

def scenarioNativeDeliverooJ7(device: Device, isFirstRun):
    if isFirstRun:
        tap(device, 459, 725) # Deny location
        tap(device, 672, 93) # Search location btn
        write_text(device, 'Amsterdam')
        tap(device, 193, 194) # Top result
        tap(device, 369, 1221) # Confirm location
        tap(device, 659, 90) # Skip
        tap(device, 351, 994) # Ok
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioNative9GAGJ7(device: Device, isFirstRun):
    # while True:
    # tap(device, 596, 189)
    #     write_text(device, 'Call of Duty')
    #     tap(device, 679, 1221)
    #     tap(device, 585, 280)
    #     swipe(device, 288, 1024, 288, 204)
    #     tap(device, 416, 306)
    pass

def scenarioNativeRedditJ7(device: Device, isFirstRun):
    # tap(device, 598, 1200)
    # # while True:
    # tap(device, 148, 754)
    # tap(device, 157, 992)
    # swipe(device, 288, 204, 288, 1024)
    # swipe(device, 288, 204, 288, 1024)
    pass

def scenarioNativeWeatherJ7(device: Device, isFirstRun):
    tap(device, 365, 1160) # Next 
    tap(device, 353, 1064) # I understand
    tap(device, 344, 1074) # I understand
    tap(device, 459, 744) # Deny
    # while True:
    write_text(device, 'Amsterdam')
    tap(device, 657, 1216) # Search
    tap(device, 263, 242) # Top result
    swipe(device, 288, 204, 288, 1024) # down
    swipe(device, 288, 204, 288, 1024) # up
    tap(device, 67, 82) # search top

def scenarioNativeYoutubeJ7(device: Device, isFirstRun):
    # tap(device, 378, 893)
    # tap(device, 495, 941)
    # # while True:
    # swipe(device, 288, 204, 288, 1024)
    # swipe(device, 288, 204, 288, 1024)
    # tap(device, 357, 1234)
    # tap(device, 407, 613)
    # tap(device, 117, 186)
    pass

def scenarioNativeZaraJ7(device: Device, isFirstRun):
    # tap(device, 355, 1197)
    # tap(device, 355, 1197)
    # tap(device, 679, 194)
    # # while True:
    # tap(device, 598, 173)
    # write_text(device, 'Shoes')
    # tap(device, 83, 269)
    # swipe(device, 288, 204, 288, 1024)
    # tap(device, 148, 640)
    # tap(device, 47, 178)
    pass

def main(device, *args, **kwargs):
    # FIXME takes for ever
    print('=INTERACTION=')
    print((device))
    print((device.id))
    print((device.current_activity()))
    isFirstRun = args[1][1]

    if device.current_activity().find('com.alibaba.aliexpresshd') != -1:
        print('running aliexpress')
        scenarioNativeAliExpressJ7(device, isFirstRun)
    elif device.current_activity().find('com.booking') != -1:
        print('running booking')
        scenarioNativeBookingJ7(device, isFirstRun)
    elif device.current_activity().find('com.deliveroo.orderapp') != -1:
        print('running deliveroo')
        scenarioNativeDeliverooJ7(device, isFirstRun)
    elif device.current_activity().find('com.reddit.frontpage') != -1:
        print('running reddit')
        scenarioNativeRedditJ7(device, isFirstRun)
    elif device.current_activity().find('com.ninegag.android.app') != -1:
        print('running 9gag')
        scenarioNative9GAGJ7(device, isFirstRun)
    elif device.current_activity().find('com.weather') != -1:
        print('running weather')
        scenarioNativeWeatherJ7(device, isFirstRun)
    elif device.current_activity().find('com.google.android.youtube') != -1:
        print('running youtube')
        scenarioNativeYoutubeJ7(device, isFirstRun)
    elif device.current_activity().find('com.inditex.zara') != -1:
        print('running zara')
        scenarioNativeZaraJ7(device, isFirstRun)
    else:
        raise Exception('There is no known interaction script for this subject')