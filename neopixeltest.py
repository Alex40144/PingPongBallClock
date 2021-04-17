import sys

import pygame

from chars import D


class Adafruit_NeoPixel (object):
    def __init__(self, LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL):
        self.led_data = [0]*LED_COUNT
        self.LED_COUNT = LED_COUNT
        return

    def begin(self):
        self.screen = pygame.display.set_mode((1080,440))
        pygame.display.set_caption("NeoPixelTester")
        return

    def setPixelColor(self, n, color):
        self.led_data[n] = color

    def show(self):
        #we need to go through again, but assign the correct colour to the pixel
        square_size = 40
        for x in range(0, 11):
            for y in range(0,27):
                # draw grid
                rectColor = self.led_data[D[x][y+1]]
                rect = pygame.Rect(y * square_size, x * square_size, square_size, square_size)
                pygame.draw.rect(self.screen, rectColor, rect, 0)
        #pygame update screen
        pygame.display.flip()
        print("updated")

    def numPixels(self):
        return self.LED_COUNT


def Color(red, green, blue, white = 0):
	return (white << 24) | (red << 16)| (green << 8) | blue



if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1000,500))
    pygame.display.set_caption("NeoPixelTester")
        