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


def scenarioWebAliExpressJ7(device: Device):
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

def scenarioWebBookingJ7(device: Device):
    tap(device, 546, 1218)
    while True:
        tap(device, 333, 760)
        write_text(device, 'Amsterdam')
        tap(device, 633, 1202)
        swipe(device, 288, 1024, 288, 204)
        swipe(device, 288, 204, 288, 1024)

def scenarioWebDeliverooJ7(device: Device):
    # while True:??
    tap(device, 333, 738)
    write_text(device, 'EC4R 3TE')
    tap(device, 351, 554)
    tap(device, 396, 1005)
    swipe(device, 288, 204, 288, 1024)
    swipe(device, 288, 204, 288, 1024)

def scenarioWebTwitchJ7(device: Device):
    while True:
        tap(device, 596, 189)
        write_text(device, 'Call of Duty')
        tap(device, 679, 1221)
        tap(device, 585, 280)
        swipe(device, 288, 1024, 288, 204)
        tap(device, 416, 306)

def scenarioWebRedditJ7(device: Device):
    tap(device, 598, 1200)
    # while True:
    tap(device, 148, 754)
    tap(device, 157, 992)
    swipe(device, 288, 204, 288, 1024)
    swipe(device, 288, 204, 288, 1024)

def scenarioWebWeatherJ7(device: Device):
    tap(device, 366, 1104)
    tap(device, 369, 194)
    write_text(device, 'Amsterdam')
    tap(device, 650, 1208)
    swipe(device, 288, 204, 288, 1024)
    swipe(device, 288, 204, 288, 1024)

def scenarioWebYoutubeJ7(device: Device):
    tap(device, 378, 893)
    tap(device, 495, 941)
    # while True:
    swipe(device, 288, 204, 288, 1024)
    swipe(device, 288, 204, 288, 1024)
    tap(device, 357, 1234)
    tap(device, 407, 613)
    tap(device, 117, 186)

def scenarioWebZaraJ7(device: Device):
    tap(device, 355, 1197)
    tap(device, 355, 1197)
    tap(device, 679, 194)
    # while True:
    tap(device, 598, 173)
    write_text(device, 'Shoes')
    tap(device, 83, 269)
    swipe(device, 288, 204, 288, 1024)
    tap(device, 148, 640)
    tap(device, 47, 178)

def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print((device))
    print((device.id))
    print((args[1])) # URL

    if args[1] in 'https://www.aliexpress.com/':
        scenarioWebAliExpressJ7(device)
    elif args[1] in 'https://www.booking.com/':
        scenarioWebBookingJ7(device)
    elif args[1] in 'https://www.reddit.com/':
        scenarioWebRedditJ7(device)
    elif args[1] in 'https://www.weather.com/':
        scenarioWebWeatherJ7(device)
    elif args[1] in 'https://www.twitch.tv/':
        scenarioWebTwitchJ7(device)
    elif args[1] in 'https://deliveroo.co.uk/':
        scenarioWebDeliverooJ7(device)
    elif args[1] in 'https://www.youtube.com/':
        scenarioWebYoutubeJ7(device)
    elif args[1] in 'https://www.zara.com/us/':
        scenarioWebZaraJ7(device)
    else:
        raise Exception('There is no known interaction script for this subject')