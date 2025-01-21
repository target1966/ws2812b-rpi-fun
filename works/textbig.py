#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams, written for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
Be sure to check the learn guides for more usage information.

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!

Author(s): Melissa LeBlanc-Williams for Adafruit Industries
"""
import board
import time
import neopixel
from PIL import Image
from adafruit_pixel_framebuf import PixelFramebuffer

import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A simple example of using arguments in Python.')

# Add arguments
parser.add_argument('-w', '--words', type=str, help='Words to print')
parser.add_argument('-c', '--color', type=lambda x: int(x,0), help='Color code')

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.words:
    print(f'{args.words}')
    word=args.words
else:
    word="Hello World!"
if args.color:
    print(f'{args.color}')
    color=args.color
else:
    color=0x00FF00


pixel_pin = board.D18
pixel_width = 16
pixel_height = 16

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.05,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    reverse_x=True,
)

wait_ms=100
x=(len(word)*6)*2
s=15
while x > -15 :
    #pixel_framebuf.scroll(-1, 0)
    pixel_framebuf.fill(0x000000)
    pixel_framebuf.text(word, s, 0, color, size=2)
    pixel_framebuf.display()
    x-=1
    s-=1
    time.sleep(wait_ms/1000.0)

