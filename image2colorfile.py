#!/usr/bin/env python3

import os

path = os.path.dirname(__file__)
im = os.path.join(path, 'sample.png')

import argparse
from PIL import Image, ImageSequence
from queue import Queue
import rpi_ws281x as ws
from threading import Timer

def __rgb_translate(im):
    """Translates a given image object to corresponding RGB frame.
       Args:
         im: image object
       Returns:
         rgb translated values centered on the given matrix.
    """
    pad_size = __pad_size(im.size)
    pad = Image.new("RGB", pad_size, (0, 0, 0, 0))
    pad.paste(im, (int((pad_size[0]-im.size[0])*0.5),
                   int((pad_size[1]-im.size[1])*0.5)))
    new_size = (16, 16)
    pad.thumbnail(new_size)

    pix = pad.load()

    frame = []
    for i in range(new_size[0]):
        row = []
        for j in range(new_size[1]):
            row.append(pix[i,j])
        frame.append(row)
    return frame

def __pad_size(size):
    """Calculates the padding required to render and center the image on
       the matrix
       Args:
         size: of the image to be displayed.
       Returns:
         calculated size.
    """
    (w,h) = size
    wh_ratio = float(w) / h
    if float(w)/h != wh_ratio:
        if max(size) == w:
            return (w, int(w/wh_ratio))
        return (int(h*wh_ratio), h)
    return size

def render_image_file(image_path):
    im = Image.open(image_path)
    r_im = im.rotate(90)
    frame = __rgb_translate(r_im)
    f = open(image_path + ".color", "w")
    print(frame,file=f)
    #f.write(frame)
    f.close()

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
    im = args.file
else:
    im = os.path.join(path, 'sample.png')

print('Image')
render_image_file(im)

