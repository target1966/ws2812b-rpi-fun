#!/usr/bin/env python3

import board
import time
import sys
import neopixel
import random
from PIL import Image
from adafruit_pixel_framebuf import PixelFramebuffer
from color import *

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

pixel_framebuf.fill(Black)
pixel_framebuf.display()

wait_ms=100

def star(x, y, c):
  x2=x
  x3=x
  y2=y
  y3=y
  l=1
  while l <= 15:
    #pixel_framebuf.fill(Blue)
    #if x3 % 2:
    if True:
      pixel_framebuf.hline(x2, y, l, c)
      pixel_framebuf.vline(x, y2, l, c)
    #else:
      if l <= 11:
        pixel_framebuf.line(x2, y2, x3, y3, c)
        pixel_framebuf.line(x2, y3, x3, y2, c)
    pixel_framebuf.display()
    x2-=1
    y2-=1
    x3+=1
    y3+=1
    l+=2
    time.sleep(wait_ms/1000.0)

colors = [
  White,
  Silver,
  Gray,
  Red,
  Maroon,
  Yellow,
  Olive,
  Lime,
  Green,
  Aqua,
  Teal,
  Blue,
  Navy,
  Fuchsia,
  Purple
]
for c in colors:
  star(random.randint(0,15),random.randint(0,15),c)
#star(random.randint(0,15),random.randint(0,15),Green)
#star(random.randint(0,15),random.randint(0,15),Purple)
sys.exit()

wait_ms=100
s=15
while s > -1 :
    pixel_framebuf.line(0, 0, 15, s, 0xFF0000)
    pixel_framebuf.line(0, 0, s, 15, 0x00FF00)
    pixel_framebuf.display()
    s-=1
    time.sleep(wait_ms/1000.0)

pixel_framebuf.fill(0x0000FF)
pixel_framebuf.display()

wait_ms=100
s=15
e=0
while s > -1 :
    pixel_framebuf.line(0, 0, e, s, 0x00FF00)
    pixel_framebuf.display()
    if e >= 16:
        s-=1
    else:
        e+=1
    time.sleep(wait_ms/1000.0)

pixel_framebuf.fill(0x0000FF)
pixel_framebuf.display()

wait_ms=100
s=15
while s > -1 :
    pixel_framebuf.hline(0, s, 16, 0xFF0000)
    pixel_framebuf.vline(s, 0, 16, 0x00FF00)
    pixel_framebuf.display()
    s-=1
    time.sleep(wait_ms/1000.0)

pixel_framebuf.fill(0x0000FF)
pixel_framebuf.display()

wait_ms=100
s=7
e=2
while s > -1 :
    pixel_framebuf.rect(s, s, e, e, 0xFF0000)
    s-=1
    e+=2
    pixel_framebuf.rect(s, s, e, e, 0x00FF00)
    pixel_framebuf.display()
    s-=1
    e+=2
    time.sleep(wait_ms/1000.0)

pixel_framebuf.fill(0x0000FF)
pixel_framebuf.display()

wait_ms=100
s=0
e=16
while e > -1 :
    pixel_framebuf.fill_rect(s, s, e, e, 0x0000FF)
    s+=1
    e-=2
    pixel_framebuf.rect(s, s, e, e, 0x00FF00)
    pixel_framebuf.display()
    s+=1
    e-=2
    time.sleep(wait_ms/1000.0)

