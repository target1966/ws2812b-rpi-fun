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


#### https://learn.adafruit.com/easy-neopixel-graphics-with-the-circuitpython-pixel-framebuf-library/usage

import os
import board
import time
import neopixel
from PIL import Image
from adafruit_pixel_framebuf import PixelFramebuffer

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


# Name	Hex https://en.wikipedia.org/wiki/Web_colors
White	= 0xFFFFFF # W
Silver	= 0xC0C0C0 # S
Gray	= 0x808080 # g little G
Black	= 0x000000 # . or " " Space
Red	= 0xFF0000 # R
Maroon	= 0x800000 # M
Yellow	= 0xFFFF00 # Y
Olive	= 0x808000 # o little O
Lime	= 0x00FF00 # L
Green	= 0x008000 # G
Aqua	= 0x00FFFF # A
Teal	= 0x008080 # T
Blue	= 0x0000FF # B
Navy	= 0x000080 # N
Fuchsia	= 0xFF00FF # F
Purple	= 0x800080 # P


pixel_framebuf.fill(0x000000)

def read_file_to_2d_array(file_path):
    """Reads a file and creates a 2D array from its content."""

    array_2d = []
    with open(file_path, 'r') as file:
        for line in file:
            row = []
            for char in line:
                row.append(char)
            array_2d.append(row)
    return array_2d

def which_color(element):
    if element == "W":
        color = White
    elif element == "S":
        color = Silver
    elif element == "g":
        color = Gray
    elif element == " " or element == ".":
        color = Black
    elif element == "R":
        color = Red
    elif element == "M":
        color = Maroon
    elif element == "Y":
        color = Yellow
    elif element == "o":
        color = Olive
    elif element == "L":
        color = Lime
    elif element == "G":
        color = Green
    elif element == "A":
        color = Aqua
    elif element == "T":
        color = Teal
    elif element == "B":
        color = Blue
    elif element == "N":
        color = Navy
    elif element == "F":
        color = Fuchsia
    elif element == "P":
        color = Purple
    else:
        color = White
        print("BAD COLOR LETTER")
    return color

import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A simple example of using arguments in Python.')

# Add arguments
parser.add_argument('-f', '--file', type=str, help='pixel file to print')

# Parse the arguments
args = parser.parse_args()

path = os.path.dirname(__file__)

# Use the arguments
if args.file:
    print(f'{args.file}')
    file_path = args.file
else:
    file_path = os.path.join(path, 'smiley.pix')


result = read_file_to_2d_array(file_path)

matrix=result

for row in range(16):
    for column in range(16):
        print(matrix[row][column], end='')
        if matrix[row][column] != " ":
            pixel_framebuf.pixel(column, row, which_color(matrix[row][column]))
    print(' ')



pixel_framebuf.display()

