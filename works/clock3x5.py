#!/usr/bin/env python3
import board
import time
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer
from color import *
import argparse
import python_weather
import asyncio
import signal
import sys

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A simple example of using arguments in Python.')

# Add arguments
parser.add_argument('-e', '--end', type=int, help='hour to blank display for the night [18]')
parser.add_argument('-s', '--start', type=int, help='hour to un-blank display for the day [8]')
parser.add_argument('-c', '--timecolor', type=lambda x: int(x,0), help='Time Color code [Lime]')
parser.add_argument('--coloncolor', type=str, help='Colon Color code [Blue]')
parser.add_argument('--ampmcolor', type=lambda x: int(x,0), help='Colon Color code [Navy]')
parser.add_argument('--monthcolor', type=lambda x: int(x,0), help='Month Color code [Aqua]')
parser.add_argument('--daycolor', type=lambda x: int(x,0), help='Day Color code [Fuchsia]')
parser.add_argument('--dowcolor', type=lambda x: int(x,0), help='DOW Color code [Teal]')
parser.add_argument('--tempcolor', type=lambda x: int(x,0), help='Temp Color code [Teal]')
parser.add_argument('-C', '--city', type=str, help='City for weather [Chili, NY]')
parser.add_argument('-U', '--update', type=int, help='Seconds between updates [15]')
parser.add_argument('-B', '--brightness', type=float, help='Brightness value float between 0-0.5 [0.01]')
parser.add_argument('-H', '--hour', type=int, help='DEBUG hour to print')
parser.add_argument('-M', '--min', type=int, help='DEBUG minute to print')

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.timecolor:
    print(f'{args.timecolor}')
    if valid_color(args.timecolor):
      timecolor=args.timecolor
    else:
      print("BAD timecolor option using default")
      timecolor=Lime
else:
    timecolor=Lime

if args.brightness:
    print(f'{args.brightness}')
    if args.brightness > 0 and args.brightness <= 0.5:
      bright=args.brightness
    else:
      print("BAD brightness value using default")
      bright=0.01
else:
    bright=0.01

if args.update:
    print(f'{args.update}')
    update=args.update
else:
    update=15

if args.end:
    print(f'{args.end}')
    end=args.end
else:
    end=18

if args.start:
    print(f'{args.start}')
    start=args.start
else:
    start=8

if args.city:
    print(f'{args.city}')
    city=args.city
else:
    city="Chili, NY"

get_weather = 0 #only get weather ever 5 minutes
last_weather = "" 
async def getweather() -> None:
  global last_weather
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get(city) # Rochester
    # returns the current day's forecast temperature (int)
    last_weather = f"{weather.temperature}{chr(176)}"

# Function to clear the matrix
def clear():
    pixel_framebuf.fill(0x000000)
    pixel_framebuf.display()

def sigterm_handler(signal, frame):
    clear()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

pixel_pin = board.D18
pixel_width = 16
pixel_height = 16

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=bright,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    reverse_x=True,
)

def get_dayofweek(w):
  if w == 0:
    return "Mon"
  if w == 1:
    return "Tue"
  if w == 2:
    return "Wed"
  if w == 3:
    return "Thu"
  if w == 4:
    return "Fri"
  if w == 5:
    return "Sat"
  if w == 6:
    return "Sun"

def get_month(m):
  if m == 1:
    return "Jan"
  if m == 2:
    return "Feb"
  if m == 3:
    return "Mar"
  if m == 4:
    return "Apr"
  if m == 5:
    return "May"
  if m == 6:
    return "Jun"
  if m == 7:
    return "Jul"
  if m == 8:
    return "Aug"
  if m == 9:
    return "Sep"
  if m == 10:
    return "Oct"
  if m == 11:
    return "Nov"
  if m == 12:
    return "Dec"

font="font3x5.bin"

try:
  while True:
    result = time.localtime()
    #Debug?
    #print(result)
    my_hour=result.tm_hour
    my_min=result.tm_min
    if args.hour:
      print(f'{args.hour}')
      my_hour=args.hour
    if args.min:
      print(f'{args.min}')
      my_min=args.min
  
    if my_hour > 12:
      my_hour-=12

    if get_weather > 19:
      get_weather = 0
    #print(get_weather)
    #print(last_weather)
    if get_weather == 0:
      asyncio.run(getweather())
    get_weather += 1
  
    pixel_framebuf.fill(0x000000)
    if result.tm_hour <= end and result.tm_hour >= start:
      # Print time
      pixel_framebuf.text(f"{str(my_hour).rjust(2)}{my_min:02d}",0,0,timecolor,font_name=font)
      # Colon
      pixel_framebuf.pixel(7,1,Blue)
      pixel_framebuf.pixel(7,3,Blue)
      # AM/PM only display p if PM
      if result.tm_hour > 11:
        pixel_framebuf.text("p",13,4,Navy,font_name=font)
      # Flip Month/day with Day of Week every 30 sec
      #if result.tm_sec < 30:
      if result.tm_sec < 15 or ( result.tm_sec > 30 and result.tm_sec < 45):
        # Month
        pixel_framebuf.text(get_month(result.tm_mon),0,6,Aqua,font_name=font)
        # Day
        pixel_framebuf.text(str(result.tm_mday).rjust(2),8,11,Fuchsia,font_name=font)
      elif result.tm_sec > 30:  # Temp
        start_x = 14 - len(last_weather) * 4
        if len(last_weather) > 3:
          start_x = 1
        elif len(last_weather) == 3:
          start_x = 2
        else:
          start_x = 6
        pixel_framebuf.text(last_weather,start_x,9,Teal,font_name=font)
      else:  # DOW
        pixel_framebuf.text(get_dayofweek(result.tm_wday),2,9,Teal,font_name=font)

    pixel_framebuf.display()
    time.sleep(update)
except KeyboardInterrupt:
  clear()
#finally:
#  clear()

