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
import sys
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
parser.add_argument('-f', '--file', type=str, help='pixel file to print default smiley.pix')
parser.add_argument('-s', '--scroll', type=int, help='1-Down 2-DownLeft 3-Left 4-UpLeft 5-Up 6-UpRight 7-Right 8-DownRight')
parser.add_argument('-d', '--direction', type=str, help='on or off screen default on')

# Parse the arguments
args = parser.parse_args()

path = os.path.dirname(__file__)

# Use the arguments
if args.file:
    print(f'File {args.file}')
    file_path = args.file
else:
    file_path = os.path.join(path, 'smiley.pix')

if args.direction:
    print(f'Direction {args.direction}')
    if args.direction == "off":
      on_screen = False
    elif args.direction == "on":
      on_screen = True
    else:
      print(f"BAD DIRECTION {args.direction}")
      sys.exit(1)
else:
    on_screen = True


result = read_file_to_2d_array(file_path)

matrix=result

wait_ms=100

if on_screen:
  bottom_top=True
  left_right=True
  xoffset=16
  yoffset=16
  if args.scroll:
    print(f'Scroll {args.scroll}')
    scroll = args.scroll
  else:
    scroll = 1
  if scroll == 1:
    xoffset=16; yoffset=0
    left_right=True
    bottom_top=False
  elif scroll == 2:
    xoffset=16; yoffset=16
    left_right=True
    bottom_top=False
  elif scroll == 3:
    xoffset=0; yoffset=16
    left_right=True
    bottom_top=False
  elif scroll == 4:
    xoffset=16; yoffset=16
    left_right=True
    bottom_top=True
  elif scroll == 5:
    xoffset=16; yoffset=0
    left_right=True
    bottom_top=True
  elif scroll == 6:
    xoffset=16; yoffset=16
    left_right=False
    bottom_top=True
  elif scroll == 7:
    xoffset=0; yoffset=16
    left_right=False
    bottom_top=True
  elif scroll == 8:
    xoffset=16; yoffset=16
    left_right=False
    bottom_top=False
  else:
    print("BAD scroll number")
    sys.exit(1)

  for foo in range(17):
    pixel_framebuf.fill(0x000000)
    for row in range(16):
        for column in range(16):
            if matrix[row][column] != " ":
                if bottom_top:
                  if left_right:
                    pixel_framebuf.pixel(column+yoffset, row+xoffset, which_color(matrix[row][column]))
                  else:
                    pixel_framebuf.pixel(column-yoffset, row+xoffset, which_color(matrix[row][column]))
                else:
                  if left_right:
                    pixel_framebuf.pixel(column+yoffset, row-xoffset, which_color(matrix[row][column]))
                  else:
                    pixel_framebuf.pixel(column-yoffset, row-xoffset, which_color(matrix[row][column]))
    if xoffset > 0:
      xoffset-=1
    if yoffset > 0:
      yoffset-=1
    #print(f"xoffset= {xoffset}   yoffset= {yoffset}")
    pixel_framebuf.display()
    time.sleep(wait_ms/1000.0)
else:
  bottom_top=True
  left_right=True
  xoffset=16
  yoffset=16
  if args.scroll:
    print(f'Scroll {args.scroll}')
    scroll = args.scroll
  else:
    scroll = 1
  if scroll == 1:   # FIX
    xoffset=0; yoffset=-1
    left_right=False
    bottom_top=False
  elif scroll == 2:
    xoffset=0; yoffset=0
    left_right=True
    bottom_top=False
  elif scroll == 3:   # FIX
    xoffset=-1; yoffset=0
    left_right=True
    bottom_top=False
  elif scroll == 4:
    xoffset=0; yoffset=0
    left_right=True
    bottom_top=True
  elif scroll == 5:   # FIX
    xoffset=0; yoffset=-1
    left_right=False
    bottom_top=True
  elif scroll == 6:
    xoffset=0; yoffset=0
    left_right=False
    bottom_top=True
  elif scroll == 7:   # FIX
    xoffset=-1; yoffset=0
    left_right=False
    bottom_top=True
  elif scroll == 8:
    xoffset=0; yoffset=0
    left_right=False
    bottom_top=False
  else:
    print("BAD scroll number")
    sys.exit(1)

  for foo in range(17):
    pixel_framebuf.fill(0x000000)
    for row in list(reversed(range(16))):
      for column in list(reversed(range(16))):
        if matrix[row][column] != " ":
          if xoffset == -1:
            xoffset2 = 0
          else:
            xoffset2 = xoffset
          if yoffset == -1:
            yoffset2 = 0
          else:
            yoffset2 = yoffset
          if bottom_top:
            if left_right:
              pixel_framebuf.pixel(column+yoffset2, row+xoffset2, which_color(matrix[row][column]))
            else:
              pixel_framebuf.pixel(column-yoffset2, row+xoffset2, which_color(matrix[row][column]))
          else:
            if left_right:
              pixel_framebuf.pixel(column+yoffset2, row-xoffset2, which_color(matrix[row][column]))
            else:
              pixel_framebuf.pixel(column-yoffset2, row-xoffset2, which_color(matrix[row][column]))
    if xoffset < 16:
      if xoffset > -1:
        xoffset+=1
    if yoffset < 16:
      if yoffset > -1:
        yoffset+=1
    #print(f"xoffset= {xoffset}   yoffset= {yoffset}")
    pixel_framebuf.display()
    time.sleep(wait_ms/1000.0)

