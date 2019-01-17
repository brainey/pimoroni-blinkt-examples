#!/usr/bin/env python

from blinkt import set_pixel, show, set_brightness
from random import random, randint
from time import sleep

while True:
    pixel = randint(0,7)
    lum = random()
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    #set_brightness(lum)
    set_pixel(pixel, r, g, b)
    show()
    sleep(0.05)
