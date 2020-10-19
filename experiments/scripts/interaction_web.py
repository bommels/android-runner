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


def scenarioWebAliExpressJ7(device: Device, isFirstRun):
    # if isFirstRun:
    tap(device, 369, 912) # print('remove pop up')
    tap(device, 243, 410) # print('search')
    write_text(device, 'Shoes') # print('search write')
    tap(device, 661, 1218) # print('search btn')
    swipe(device, 288, 1024, 288, 204)
    while True: # Keep repeating
        tap(device, 256, 104) # print('search')
        tap(device, 596, 192) # clear search
        write_text(device, 'Shoes') # print('search write')
        tap(device, 661, 1218) # print('search btn')
        swipe(device, 288, 1024, 288, 204)

def scenarioWebTripAdvisorJ7(device: Device, isFirstRun):
    tap(device, 672, 533) # First search
    
    tap(device, 342, 589) # Click Shopping
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 663, 330) # Get search bar
        tap(device, 346, 594) # Click Shopping

def scenarioWebDeliverooJ7(device: Device, isFirstRun):
    tap(device, 333, 738) # Tap zip code search
    write_text(device, 'EC4R 3TE')
    tap(device, 351, 554) # search
    # if isFirstRun:
    tap(device, 355, 1012) # ok promo
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWebTwitchJ7(device: Device, isFirstRun):
    while True:
        tap(device, 596, 189) # Search bar
        write_text(device, 'Call of Duty')
        tap(device, 679, 1221) # Search
        tap(device, 585, 280) # Tap live streams
        swipe(device, 288, 1024, 288, 204)
        tap(device, 416, 306) # Tap some stream

def scenarioWeb9GAGJ7(device: Device, isFirstRun):
    time.sleep(1) # wait 
    tap(device, 612, 1216) # Continue to web app
    time.sleep(5) # wait for cookies
    tap(device, 362, 1045) # Accept cookies
    #tap(device, 670, 1224) # Remove bottom bar
    while True:
        tap(device, 339, 264) # Press Trending
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 128, 264) # Press Hot
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWebRedditJ7(device: Device, isFirstRun):
    # tap(device, 40, 1232) # Click away different app pop up (try)
    time.sleep(2) # Wait a little longer for the pop up
    tap(device, 598, 1200) # Continue web version
    # if isFirstRun:
    tap(device, 434, 768) # block notifications
    tap(device, 690, 256) # cookies
    # else:
        # tap(device, 40, 1232) # Click away different app pop up
    # tap(device, 625, 912) # Click first meme --> can be a link to some different website
    while True:
        tap(device, 117, 621) # Press hot
        tap(device, 157, 866) # Change top
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 121, 621) # Press top
        tap(device, 119, 781) # Change hot
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWebWeatherJ7(device: Device, isFirstRun):
    # if isFirstRun:
    tap(device, 366, 1104) # Agree
    tap(device, 369, 194) # search bar
    while True:
        write_text(device, 'Amsterdam')
        tap(device, 650, 1208) # Search btn
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 562, 186) # search bar

def scenarioWebYoutubeJ7(device: Device, isFirstRun):
    # if isFirstRun:
    tap(device, 378, 893) # Do not sign in
    tap(device, 495, 941) # agree 
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 357, 1234) # Trending
        tap(device, 407, 613) # First video
        tap(device, 117, 186) # Youtube home page

def scenarioWebZaraJ7(device: Device, isFirstRun):
    # if isFirstRun:
    tap(device, 679, 194) # Cookies
    tap(device, 355, 1097) # Stay on Us
    tap(device, 598, 173) # Search bar
    tap(device, 353, 181) # Focus search bar
    while True:
        write_text(device, 'Shoes')
        tap(device, 83, 269) # Top result
        swipe(device, 288, 1204, 288, 204) 
        tap(device, 148, 640) # Click on shoe
        tap(device, 47, 178) # Back arrow
        tap(device, 668, 192) # Clear search bar input 

def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print((device))
    print((device.id))
    print((args))
    URL = args[1][0]
    isFirstRun = args[1][1]

    if URL in 'https://www.aliexpress.com/':
        scenarioWebAliExpressJ7(device, isFirstRun)
    elif URL in 'https://www.tripadvisor.com/':
        scenarioWebTripAdvisorJ7(device, isFirstRun)
    elif URL in 'https://www.reddit.com/':
        scenarioWebRedditJ7(device, isFirstRun)
    elif URL in 'https://www.weather.com/':
        scenarioWebWeatherJ7(device, isFirstRun)
    elif URL in 'https://9gag.com/':
        scenarioWeb9GAGJ7(device, isFirstRun)
    elif URL in 'https://deliveroo.co.uk/':
        scenarioWebDeliverooJ7(device, isFirstRun)
    elif URL in 'https://www.youtube.com/':
        scenarioWebYoutubeJ7(device, isFirstRun)
    elif URL in 'https://www.zara.com/us/':
        scenarioWebZaraJ7(device, isFirstRun)
    else:
        raise Exception('There is no known interaction script for this subject')