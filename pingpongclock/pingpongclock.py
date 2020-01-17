from datetime import datetime
import random
import time
import numpy as np

current_hour = datetime.now().time().strftime("%H")
current_min = datetime.now().time().strftime("%M")


pixels = [[000, 000, 000]*27]*11

print(repr(pixels))

def hour(int(str(current_hour)[:1])):
	if int(str(current_hour)[:1] == 0:
		#5,2 | 6,2 | 7,2 
		#5,3 |     | 7,3
		#5,4 |     | 7,4
		#5,5 |     | 7,5
		#5,6 |     | 7,6
		#5,7 |     | 7,7
		#5,8 | 6,8 | 7,8

		#add pixels to list of number pixels
		#add non pixels to list of not number pixels

	if int(str(current_hour)[:1] == 1:
		#    |     | 7,2 
		#    |     | 7,3
		#    |     | 7,4
		#    |     | 7,5
		#    |     | 7,6
		#    |     | 7,7
		#    |     | 7,8

def min(current_min):
	print(current_min)