#!/bin/bash

cd ~/ws2812b
sudo works/pixel-it.py -f works/santa.pix
sleep 5
sudo works/text.py -w "Merry Xmas!"
sudo works/pixel-it.py -f works/tree.pix
sleep 5
sudo ./color.py -f ./mario.png.color
sleep 5
sudo works/clear.py

sudo python3 rpi-ws281x-matrix-python/animation.py



