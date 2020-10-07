import logging
import time
from AndroidRunner.Device import Device

logger = logging.getLogger(__name__)

def tap(device: Device, x: int, y: int, sleep = 4):
    device.shell('input tap %s %s' % (x, y))
    # We need to wait for the display to update after the last click.
    # The time to update is vary. 
    time.sleep(sleep)

def write_text(device: Device, text: str, sleep = 1):
    device.shell('input text \'%s\'' % text)
    time.sleep(sleep)

def swipe(device: Device, x1: int, y1: int, x2: int, y2: int, sleep = 4, duration = 1000):
    device.shell('input swipe %s %s %s %s %s' % (x1, y1, x2, y2, duration))
    time.sleep(sleep)

def scenarioWebTwitchJ7(device: Device):
    while True:
        tap(device, 596, 189)
        write_text(device, 'Call of Duty')
        tap(device, 679, 1221)
        tap(device, 585, 280)
        swipe(device, 288, 1024, 288, 204)
        tap(device, 416, 306)

def scenarioWebAliExpressJ7(device: Device):
    tap(device, 369, 912) # print('remove pop up')
    while True: # Keep repeating
        tap(device, 243, 410) # print('search')
        write_text(device, 'Shoes') # print('search write')
        tap(device, 270, 525) # print('search btn')
        swipe(device, 288, 1024, 288, 204)

def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print((device))
    print((device.id))
    print((device.current_activity())) # Should return the current URL it doesn't..
    print(device.current_web_page('https://www.aliexpress.com')) # should be a regex match probably

    if device.current_web_page('https://www.aliexpress.com'):
        scenarioWebAliExpressJ7(device)
    elif device.current_web_page('https://www.booking.com/'):
        scenarioWebBookingJ7(device)
    elif device.current_web_page('https://www.reddit.com/'):
        scenarioWebRedditJ7(device)
    elif device.current_web_page('https://www.weather.com/'):
        scenarioWebWeatherJ7(device)
    elif device.current_web_page('https://www.twitch.tv/'):
        scenarioWebTwitchJ7(device)
    elif device.current_web_page('https://www.yelp.com/'):
        scenarioWebYelpJ7(device)
    elif device.current_web_page('https://www.youtube.com/'):
        scenarioWebYoutubeJ7(device)
    elif device.current_web_page('https://www.zara.com/us/'):
        scenarioWebZaraJ7(device)
    else:
        raise Exception('There is no known interaction script for this subject')

    # elif device.current_activity().find('https://www.zara.com/us/') != -1:
    #     # scenarioWebZaraJ7(device)