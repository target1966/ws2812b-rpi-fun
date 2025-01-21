#!/usr/bin/env python3

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

pixel_framebuf.fill(blue)
pixel_framebuf.display()

wait_ms=250
x=7
y=9
L=1
while y > -1 :
    if y % 2:
        color=red
    else:
        color=green
    pixel_framebuf.hline(y, 7, L, color)
    pixel_framebuf.vline(7, y, L, color)
    pixel_framebuf.display()
    y-=1
    L+=2
    time.sleep(wait_ms/1000.0)

wait_ms=250
x=8
y=8
L=1
while y > -1 :
    if y % 2:
        color=red
    else:
        color=green
    pixel_framebuf.line(x, y, x+L, y+L, color)
    pixel_framebuf.line(y, x, y-L, x-L, color)
    pixel_framebuf.display()
    x-=1
    y+=1
    L+=2
    time.sleep(wait_ms/1000.0)


wait_ms=250
#pixel_framebuf.fill(blue)
#pixel_framebuf.display()

pixel_framebuf.hline(7, 7, 1, red)
pixel_framebuf.vline(7, 7, 1, red)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(6, 7, 3, green)
pixel_framebuf.vline(7, 6, 3, green)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(5, 7, 5, red)
pixel_framebuf.vline(7, 5, 5, red)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(4, 7, 7, green)
pixel_framebuf.vline(7, 4, 7, green)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(3, 7, 9, red)
pixel_framebuf.vline(7, 3, 9, red)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(2, 7, 11, green)
pixel_framebuf.vline(7, 2, 11, green)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(1, 7, 13, red)
pixel_framebuf.vline(7, 1, 13, red)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)
pixel_framebuf.hline(0, 7, 15, green)
pixel_framebuf.vline(7, 0, 15, green)
pixel_framebuf.display()
time.sleep(wait_ms/1000.0)

