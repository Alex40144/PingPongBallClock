from datetime import datetime
import random
import time
import numpy as np

current_hour = datetime.now().time().strftime("%H")
current_min = datetime.now().time().strftime("%M")

first_digit = int(str(current_hour)[:1])
second_digit = int(str(current_hour)[1:])
third_digit = int(str(current_min)[:1])
fourth_digit = int(str(current_min)[1:])


print(first_digit, second_digit, third_digit, fourth_digit)

dots = [95, 203]
not_digit_pixels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,63,67,68,69,73,77,78,79,80,81]

def hour(first_digit):
	if first_digit == 0:
		#5,2 | 6,2 | 7,2 
		#5,3 |     | 7,3
		#5,4 |     | 7,4
		#5,5 |     | 7,5
		#5,6 |     | 7,6
		#5,7 |     | 7,7
		#5,8 | 6,8 | 7,8
		first_digit_pixels = [60, 61, 62, 101, 103, 114, 116, 155, 156, 157, 168, 170, 209, 211, 222, 223, 224]
		not_first_digit_pixels = [112, 115,156, 169, 210]

	if first_digit == 1:
		#    |     | 7,2 
		#    |     | 7,3
		#    |     | 7,4
		#    |     | 7,5
		#    |     | 7,6
		#    |     | 7,7
		#    |     | 7,8
		print()
def min(current_min):
	print(current_min)