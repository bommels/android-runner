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


def scenarioWebAliExpress7pro(device: Device, isFirstRun):
    time.sleep(3) # wait for cookies
    tap(device, 733, 1742) # print('remove pop up')
    tap(device, 990, 864) # print('search')
    write_text(device, 'Shoes') # print('search write')
    tap(device, 1341, 2788) # print('search btn')
    swipe(device, 288, 1024, 288, 204)
    while True: # Keep repeating
        tap(device, 751, 234) # print('search')
        tap(device, 1197, 422) # clear search
        write_text(device, 'Shoes') # print('search write')
        tap(device, 1332, 2795) # print('search btn')
        swipe(device, 288, 1024, 288, 204)

def scenarioWebBooking7pro(device: Device, isFirstRun):
    time.sleep(3) # wait for cookies
    tap(device, 1102, 2782) # accept cookies
    tap(device, 697, 1592) # First search
    write_text(device, 'Amsterdam')
    tap(device, 1336, 2821) # keyboard search btn 
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 940, 1137) # Get search bar
        tap(device, 675, 617) # Search
        tap(device, 1309, 604) # Clear search
        write_text(device, 'Amsterdam')
        tap(device, 436, 838) # Top result
        tap(device, 796, 1631) # Blue search

def scenarioWebDeliveroo7pro(device: Device, isFirstRun):
    time.sleep(3) # Wait a little longer for the pop up
    tap(device, 801, 2801) # accept cookies
    tap(device, 940, 1553) # Tap zip code search
    write_text(device, 'EC4R 3TE')
    tap(device, 895, 1742) # search
    # if isFirstRun:
    tap(device, 787, 2236) # ok promo
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWeb9GAG7pro(device: Device, isFirstRun):
    time.sleep(3) # wait for cookies
    tap(device, 936, 2288) # Accept cookies
    tap(device, 1219, 2808) # Continue to web app
    #tap(device, 670, 1224) # Remove bottom bar
    while True:
        tap(device, 747, 604) # Press Trending
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 243, 565) # Press Hot
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWebReddit7pro(device: Device, isFirstRun):
    time.sleep(3) # Wait a little longer for the pop up
    tap(device, 1147, 2782) # Continue web version
    # if isFirstRun:
    #tap(device, 868, 1735) # block notifications
    tap(device, 1386, 552) # cookies
    # else:
        # tap(device, 40, 1232) # Click away different app pop up
    # tap(device, 625, 912) # Click first meme --> can be a link to some different website
    while True:
        tap(device, 216, 1300) # Press hot
        tap(device, 252, 1781) # Change top
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 162, 1287) # Press top
        tap(device, 252, 1618) # Change hot
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWebWeather7pro(device: Device, isFirstRun):
    time.sleep(3) # wait for cookies
    tap(device, 796, 2587) # Agree
    tap(device, 900, 422) # search bar
    while True:
        write_text(device, 'Amsterdam')
        tap(device, 1327, 2814) # Search btn
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 747, 403) # search bar

def scenarioWebYoutube7pro(device: Device, isFirstRun):
    time.sleep(3) # wait for cookies
    tap(device, 742, 1963) # Do not sign in
    tap(device, 1039, 2047) # agree 
    while True:
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)
        tap(device, 711, 2860) # Trending
        tap(device, 756, 1293) # First video
        tap(device, 220, 409) # Youtube home page

def scenarioWebZara7pro(device: Device, isFirstRun):
    time.sleep(3) # wait for cookies
    tap(device, 1372, 429) # Cookies
    tap(device, 639, 2522) # Stay on Us
    tap(device, 1201, 390) # Search bar
    tap(device, 265, 403) # Focus search bar
    while True:
        write_text(device, 'Shoes')
        tap(device, 153, 572) # Top result
        swipe(device, 288, 1204, 288, 204) 
        tap(device, 427, 929) # Click on shoe
        tap(device, 94, 416) # Back arrow
        tap(device, 1341, 409) # Clear search bar input 

def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print((device))
    print((device.id))
    print((args))
    URL = args[1][0]
    isFirstRun = args[1][1]

    if URL in 'https://www.aliexpress.com/':
        scenarioWebAliExpress7pro(device, isFirstRun)
    elif URL in 'https://www.booking.com/':
        scenarioWebBooking7pro(device, isFirstRun)
    elif URL in 'https://www.reddit.com/':
        scenarioWebReddit7pro(device, isFirstRun)
    elif URL in 'https://www.weather.com/':
        scenarioWebWeather7pro(device, isFirstRun)
    elif URL in 'https://www.9gag.com/':
        scenarioWeb9GAG7pro(device, isFirstRun)
    elif URL in 'https://www.deliveroo.co.uk/':
        scenarioWebDeliveroo7pro(device, isFirstRun)
    elif URL in 'https://www.youtube.com/':
        scenarioWebYoutube7pro(device, isFirstRun)
    elif URL in 'https://www.zara.com/us/':
        scenarioWebZara7pro(device, isFirstRun)
    else:
        raise Exception('There is no known interaction script for this subject')