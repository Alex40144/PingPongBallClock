from datetime import datetime
import random
import time
import chars
from neopixeltest import *

#############################
clock = False
#############################


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


D = chars.display()

dots = [D[4][14], D[6][14]]

numberColour = Color(255,0,0)

def Wipe():
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))


def FirstDigit(first_digit):

	if first_digit == 0:
		first_digit_pixels = chars.zero(2, 3)
	elif first_digit == 1:
		first_digit_pixels = chars.one(2, 3)
	elif first_digit == 2:
		first_digit_pixels = chars.two(2, 3)
	elif first_digit == 3:
		first_digit_pixels = chars.three(2, 3)
	elif first_digit == 4:
		first_digit_pixels = chars.four(2, 3)
	elif first_digit == 5:
		first_digit_pixels = chars.five(2, 3)
	elif first_digit == 6:
		first_digit_pixels = chars.six(2, 3)
	elif first_digit == 7:
		first_digit_pixels = chars.seven(2, 3)
	elif first_digit == 8:
		first_digit_pixels = chars.eight(2, 3)
	elif first_digit == 9:
		first_digit_pixels = chars.nine(2, 3)


	for i in range(len(first_digit_pixels)):
		strip.setPixelColor(first_digit_pixels[i], numberColour)

def SecondDigit(second_digit):

	if second_digit == 0:
		second_digit_pixels = chars.zero(2, 8)
	elif second_digit == 1:
		second_digit_pixels = chars.one(2, 8)
	elif second_digit == 2:
		second_digit_pixels = chars.two(2, 8)
	elif second_digit == 3:
		second_digit_pixels = chars.three(2, 8)
	elif second_digit == 4:
		second_digit_pixels = chars.four(2, 8)
	elif second_digit == 5:
		second_digit_pixels = chars.five(2, 8)
	elif second_digit == 6:
		second_digit_pixels = chars.six(2, 8)
	elif second_digit == 7:
		second_digit_pixels = chars.seven(2, 8)
	elif second_digit == 8:
		second_digit_pixels = chars.eight(2, 8)
	elif second_digit == 9:
		second_digit_pixels = chars.nine(2, 8)


	for i in range(len(second_digit_pixels)):
		strip.setPixelColor(second_digit_pixels[i], numberColour)

def ThirdDigit(third_digit):

	if third_digit == 0:
		third_digit_pixels = chars.zero(2, 17)
	elif third_digit == 1:
		third_digit_pixels = chars.one(2, 17)
	elif third_digit == 2:
		third_digit_pixels = chars.two(2, 17)
	elif third_digit == 3:
		third_digit_pixels = chars.three(2, 17)
	elif third_digit == 4:
		third_digit_pixels = chars.four(2, 17)
	elif third_digit == 5:
		third_digit_pixels = chars.five(2, 17)
	elif third_digit == 6:
		third_digit_pixels = chars.six(2, 17)
	elif third_digit == 7:
		third_digit_pixels = chars.seven(2, 17)
	elif third_digit == 8:
		third_digit_pixels = chars.eight(2, 17)
	elif third_digit == 9:
		third_digit_pixels = chars.nine(3, 17)


	for i in range(len(third_digit_pixels)):
		strip.setPixelColor(third_digit_pixels[i], numberColour)

def FourthDigit(fourth_digit):

	if fourth_digit == 0:
		fourth_digit_pixels = chars.zero(2, 22)
	elif fourth_digit == 1:
		fourth_digit_pixels = chars.one(2, 22)
	elif fourth_digit == 2:
		fourth_digit_pixels = chars.two(2, 22)
	elif fourth_digit == 3:
		fourth_digit_pixels = chars.three(2, 22)
	elif fourth_digit == 4:
		fourth_digit_pixels = chars.four(2, 22)
	elif fourth_digit == 5:
		fourth_digit_pixels = chars.five(2, 22)
	elif fourth_digit == 6:
		fourth_digit_pixels = chars.six(2, 22)
	elif fourth_digit == 7:
		fourth_digit_pixels = chars.seven(2, 22)
	elif fourth_digit == 8:
		fourth_digit_pixels = chars.eight(2, 22)
	elif fourth_digit == 9:
		fourth_digit_pixels = chars.nine(2, 22)


	for i in range(len(fourth_digit_pixels)):
		strip.setPixelColor(fourth_digit_pixels[i], numberColour)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	pos = pos*2
	if pos > 255:
		temp = pos -255
		pos = 255 - temp
	return( Color(0,255-pos,pos))

a = 0
def Background():
	global a
	a+=5
	if a == 256:
		a = 0
	for b in range(1,28):
		for c in range(0,11):
			strip.setPixelColor(D[c][b], wheel((int(b * 256 / 27) + a) & 255))

while True:
	Wipe()
	Background()
	if clock:
		current_hour = datetime.now().time().strftime("%H")
		current_min = datetime.now().time().strftime("%M")

		first_digit = int(str(current_hour)[:1])
		second_digit = int(str(current_hour)[1:])
		third_digit = int(str(current_min)[:1])
		fourth_digit = int(str(current_min)[1:])

		print(first_digit, second_digit, third_digit, fourth_digit)

		FirstDigit(first_digit)
		SecondDigit(second_digit)
		ThirdDigit(third_digit)
		FourthDigit(fourth_digit)

		strip.setPixelColor(dots[0], Color(255,255,255))
		strip.setPixelColor(dots[1], Color(255,255,255))

		strip.show()
		time.sleep(1)

		strip.setPixelColor(dots[0], Color(0,0,0))
		strip.setPixelColor(dots[1], Color(0,0,0))

		strip.show()
		time.sleep(1)
	else:
		#assume we are scrolling text for now
		letterpixels = chars.A(2, 8)
		for i in range(len(letterpixels)):
			strip.setPixelColor(letterpixels[i], numberColour)

		strip.show()
		time.sleep(1)
			