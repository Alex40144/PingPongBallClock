
from setup import Color
import time
from chars import D
import setup 
strip = setup.start()


###################################################################################
#Display has range:
#                 D[0][0] to D[10][27]
#
#  left number  = y
#  right number = x
#
#  Color(RED,GREEN,BLUE)
# where R/G/B is an integer from 0 to 255


#change the colour of a pixel:

strip.setPixelColor( D[0][0], Color(255,255,255))
strip.setPixelColor( D[10][27], Color(255,255,255))

#update display

strip.show()