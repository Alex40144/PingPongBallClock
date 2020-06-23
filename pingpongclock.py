from datetime import datetime
import random
import time
from neopixel import *

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

D       =  [[0,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
		    [0, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27],
		    [0, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
		    [0,107,106,105,104,103,102,101,100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],
		    [0,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134],
		    [0,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135],
		    [0,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188],
		    [0,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199,198,197,196,195,194,193,192,191,190,189],
		    [0,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242],
		    [0,269,268,267,266,265,264,263,262,261,260,259,258,257,256,255,254,253,252,251,250,249,248,247,246,245,244,243],
		    [0,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296]]


dots = [D[4][14], D[6][14]]

numberColour = Color(255,0,0)

def Wipe():
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))

def zero(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])

def one(origin_x, origin_y):
	return(D[origin_x][origin_y+2],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y+2])

def two(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])

def three(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])

def four(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+2],D[origin_x+1][origin_y],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y+2])

def five(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])

def six(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])

def seven(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y+2])

def eight(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])

def nine(origin_x, origin_y):
	return(D[origin_x][origin_y],D[origin_x][origin_y+1],D[origin_x][origin_y+2],D[origin_x+1][origin_y],D[origin_x+1][origin_y+2],D[origin_x+2][origin_y],D[origin_x+2][origin_y+1],D[origin_x+2][origin_y+2],D[origin_x+3][origin_y+2],D[origin_x+4][origin_y],D[origin_x+4][origin_y+1],D[origin_x+4][origin_y+2])




def FirstDigit(first_digit):

	if first_digit == 0:
		first_digit_pixels = zero(3,5)
	elif first_digit == 1:
		first_digit_pixels = one(3,5)
	elif first_digit == 2:
		first_digit_pixels = two(3,5)
	elif first_digit == 3:
		first_digit_pixels = three(3,5)
	elif first_digit == 4:
		first_digit_pixels = four(3,5)
	elif first_digit == 5:
		first_digit_pixels = five(3,5)
	elif first_digit == 6:
		first_digit_pixels = six(3,5)
	elif first_digit == 7:
		first_digit_pixels = seven(3,5)
	elif first_digit == 8:
		first_digit_pixels = eight(3,5)
	elif first_digit == 9:
		first_digit_pixels = nine(3,5)


	for i in range(len(first_digit_pixels)):
		strip.setPixelColor(first_digit_pixels[i], numberColour)

def SecondDigit(second_digit):

	if second_digit == 0:
		second_digit_pixels = zero(3, 9)
	elif second_digit == 1:
		second_digit_pixels = one(3, 9)
	elif second_digit == 2:
		second_digit_pixels = two(3, 9)
	elif second_digit == 3:
		second_digit_pixels = three(3, 9)
	elif second_digit == 4:
		second_digit_pixels = four(3, 9)
	elif second_digit == 5:
		second_digit_pixels = five(3, 9)
	elif second_digit == 6:
		second_digit_pixels = six(3, 9)
	elif second_digit == 7:
		second_digit_pixels = seven(3, 9)
	elif second_digit == 8:
		second_digit_pixels = eight(3, 9)
	elif second_digit == 9:
		second_digit_pixels = nine(3, 9)


	for i in range(len(second_digit_pixels)):
		strip.setPixelColor(second_digit_pixels[i], numberColour)

def ThirdDigit(third_digit):

	if third_digit == 0:
		third_digit_pixels = zero(3, 17)
	elif third_digit == 1:
		third_digit_pixels = one(3, 17)
	elif third_digit == 2:
		third_digit_pixels = two(3, 17)
	elif third_digit == 3:
		third_digit_pixels = three(3, 17)
	elif third_digit == 4:
		third_digit_pixels = four(3, 17)
	elif third_digit == 5:
		third_digit_pixels = five(3, 17)
	elif third_digit == 6:
		third_digit_pixels = six(3, 17)
	elif third_digit == 7:
		third_digit_pixels = seven(3, 17)
	elif third_digit == 8:
		third_digit_pixels = eight(3, 17)
	elif third_digit == 17:
		third_digit_pixels = nine(3, 17)


	for i in range(len(third_digit_pixels)):
		strip.setPixelColor(third_digit_pixels[i], numberColour)

def FourthDigit(fourth_digit):

	if fourth_digit == 0:
		fourth_digit_pixels = zero(3, 21)
	elif fourth_digit == 1:
		fourth_digit_pixels = one(3, 21)
	elif fourth_digit == 2:
		fourth_digit_pixels = two(3, 21)
	elif fourth_digit == 3:
		fourth_digit_pixels = three(3, 21)
	elif fourth_digit == 4:
		fourth_digit_pixels = four(3, 21)
	elif fourth_digit == 5:
		fourth_digit_pixels = five(3, 21)
	elif fourth_digit == 6:
		fourth_digit_pixels = six(3, 21)
	elif fourth_digit == 7:
		fourth_digit_pixels = seven(3, 21)
	elif fourth_digit == 8:
		fourth_digit_pixels = eight(3, 21)
	elif fourth_digit == 9:
		fourth_digit_pixels = nine(3, 21)


	for i in range(len(fourth_digit_pixels)):
		strip.setPixelColor(fourth_digit_pixels[i], numberColour)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	return(Color(0,255-pos,pos))

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

	strip.setPixelColor(dots[0], numberColour)
	strip.setPixelColor(dots[1], numberColour)

	strip.show()
	time.sleep(1)

	strip.setPixelColor(dots[0], Color(0,0,0))
	strip.setPixelColor(dots[1], Color(0,0,0))

	strip.show()
	time.sleep(1)