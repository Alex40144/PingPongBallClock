import requests
import json
import time
import chars
from neopixeltest import Color
from neopixeltest import *

# LED strip configuration:
LED_COUNT      = 297      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

strip.begin()

while True:
    data = requests.get("http://127.0.0.1:5000/settings.json")
    data = json.loads(data.text)
    print(data)
    for item in data:
        #remove # from hex value
        colour = data[item].lstrip('#')
        #convert the hex value to rgb values
        colour = tuple(int(colour[i:i+2], 16) for i in (0, 2, 4))
        #set the pixel colour
        strip.setPixelColor(int(item)-1, Color(colour[0], colour[1], colour[2]))
    strip.show()
    time.sleep(1)

