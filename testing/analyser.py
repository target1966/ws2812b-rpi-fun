#!/usr/bin/env python3

import board
import time
import neopixel
import random
from PIL import Image
from adafruit_pixel_framebuf import PixelFramebuffer

# Name  Hex https://en.wikipedia.org/wiki/Web_colors
White   = 0xFFFFFF # W
Silver  = 0xC0C0C0 # S
Gray    = 0x808080 # g little G
Black   = 0x000000 # . or " " Space
Red     = 0xFF0000 # R
Maroon  = 0x800000 # M
Yellow  = 0xFFFF00 # Y
Olive   = 0x808000 # o little O
Lime    = 0x00FF00 # L
Green   = 0x008000 # G
Aqua    = 0x00FFFF # A
Teal    = 0x008080 # T
Blue    = 0x0000FF # B
Navy    = 0x000080 # N
Fuchsia = 0xFF00FF # F
Purple  = 0x800080 # P

def which_color(element):
    if element == "W" or element == "1":
        color = White
    elif element == "S" or element == "2":
        color = Silver
    elif element == "g" or element == "3":
        color = Gray
    elif element == " " or element == "." or element == "4":
        color = Black
    elif element == "R" or element == "5":
        color = Red
    elif element == "M" or element == "6":
        color = Maroon
    elif element == "Y" or element == "7":
        color = Yellow
    elif element == "o" or element == "8":
        color = Olive
    elif element == "L" or element == "9":
        color = Lime
    elif element == "G" or element == "10":
        color = Green
    elif element == "A" or element == "11":
        color = Aqua
    elif element == "T" or element == "12":
        color = Teal
    elif element == "B" or element == "13":
        color = Blue
    elif element == "N" or element == "14":
        color = Navy
    elif element == "F" or element == "15":
        color = Fuchsia
    elif element == "P" or element == "16":
        color = Purple
    else:
        color = White
        print(f"BAD COLOR LETTER {element}")
    return color

pixel_pin = board.D18
pixel_width = 16
pixel_height = 16

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.01,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    reverse_x=True,
)

blue=0x0000FF
red=0xFF0000
green=0x00FF00

pixel_framebuf.fill(0x0)
pixel_framebuf.display()

wait_ms=250
x=7
y=9
L=1
for loop in range(16):
#for loop in range(1):
  print(f"### {loop} ###")
  pixel_framebuf.fill(0x0)
  for x in range(16):
    y = random.randint(0, 15)
    if y < 3:
      color=Red
      pixel_framebuf.vline(x, y, 16, Red)
      pixel_framebuf.vline(x, 3, 16, Yellow)
      pixel_framebuf.vline(x, 8, 16, Lime)
      pixel_framebuf.vline(x, 12, 16, Teal)
    elif y < 8:
      color=Yellow
      pixel_framebuf.vline(x, y, 16, Yellow)
      pixel_framebuf.vline(x, 8, 16, Lime)
      pixel_framebuf.vline(x, 12, 16, Teal)
    elif y < 12:
      color=Lime
      pixel_framebuf.vline(x, y, 16, Lime)
      pixel_framebuf.vline(x, 12, 16, Teal)
    else:
      color=Teal
      pixel_framebuf.vline(x, y, 16, Teal)
    print(y, end=" ")
    #pixel_framebuf.vline(x, y, 15, which_color(str(y)))
    #pixel_framebuf.vline(x, x, 16, which_color(str(x+1)))
    #pixel_framebuf.vline(x, y, 16, color)
  print(" ")
  pixel_framebuf.display()
  time.sleep(wait_ms/1000.0)

