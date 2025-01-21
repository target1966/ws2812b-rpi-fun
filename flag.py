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

pixel_framebuf.fill(0x000000)
# line across top  sx, sy, ex, ey, color
#pixel_framebuf.line(0, 0, 15, 0, 0xFF0000)
# diaginal line across top
#pixel_framebuf.line(0, 0, 15, 15, 0x0000FF)

## 13 stripes
# H line sx, sy, length
sy=1
pixel_framebuf.hline(7, sy, 16, 0xFF0000)
pixel_framebuf.hline(7, sy+1, 16, 0xFFFFFF)
pixel_framebuf.hline(7, sy+2, 16, 0xFF0000)
pixel_framebuf.hline(7, sy+3, 16, 0xFFFFFF)
pixel_framebuf.hline(7, sy+4, 16, 0xFF0000)
pixel_framebuf.hline(7, sy+5, 16, 0xFFFFFF)
pixel_framebuf.hline(7, sy+6, 16, 0xFF0000)
pixel_framebuf.hline(0, sy+7, 16, 0xFFFFFF)
pixel_framebuf.hline(0, sy+8, 16, 0xFF0000)
pixel_framebuf.hline(0, sy+9, 16, 0xFFFFFF)
pixel_framebuf.hline(0, sy+10, 16, 0xFF0000)
pixel_framebuf.hline(0, sy+11, 16, 0xFFFFFF)
pixel_framebuf.hline(0, sy+12, 16, 0xFF0000)

## Field of blue
pixel_framebuf.fill_rect(0, sy, 7, sy+6, 0x0000FF)

## Stars
pixel_framebuf.pixel(1, sy+1, 0xFFFFFF)
pixel_framebuf.pixel(3, sy+1, 0xFFFFFF)
pixel_framebuf.pixel(5, sy+1, 0xFFFFFF)
pixel_framebuf.pixel(2, sy+2, 0xFFFFFF)
pixel_framebuf.pixel(4, sy+2, 0xFFFFFF)
pixel_framebuf.pixel(1, sy+3, 0xFFFFFF)
pixel_framebuf.pixel(3, sy+3, 0xFFFFFF)
pixel_framebuf.pixel(5, sy+3, 0xFFFFFF)
pixel_framebuf.pixel(2, sy+4, 0xFFFFFF)
pixel_framebuf.pixel(4, sy+4, 0xFFFFFF)
pixel_framebuf.pixel(1, sy+5, 0xFFFFFF)
pixel_framebuf.pixel(3, sy+5, 0xFFFFFF)
pixel_framebuf.pixel(5, sy+5, 0xFFFFFF)

pixel_framebuf.display()

