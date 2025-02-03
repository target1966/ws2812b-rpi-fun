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
parser.add_argument('-w', '--word1', type=str, help='Words to print')
parser.add_argument('-W', '--word2', type=str, help='Words to print')
parser.add_argument('-c', '--color1', type=lambda x: int(x,0), help='Color code')
parser.add_argument('-C', '--color2', type=lambda x: int(x,0), help='Color code')

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.word1:
    print(f'{args.word1}')
    word=args.word1
else:
    word="Hello!"
if args.word2:
    print(f'{args.word2}')
    word2=args.word2
else:
    word2="      World!"
if args.color1:
    print(f'{args.color1}')
    color=args.color1
else:
    color=0x00FF00
if args.color2:
    print(f'{args.color2}')
    color2=args.color2
else:
    color2=0xFF0000

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
x1=(len(word)*6)
x2=(len(word2)*6)
if x1 >= x2:
    x=x1
else:
    x=x2
s=15
while x > -15 :
    #pixel_framebuf.scroll(-1, 0)
    pixel_framebuf.fill(0x000000)
    pixel_framebuf.text(word, s, 0, color)
    pixel_framebuf.text(word2, s, 8, color2)
    pixel_framebuf.display()
    x-=1
    s-=1
    time.sleep(wait_ms/1000.0)

