#!/bin/bash

while true
do
  cd ~/ws2812b
  sudo works/pixel-it.py -f works/santa2.pix
  sleep 3
  sudo works/text.py -w "Ho Ho Ho"
  sudo works/pixel-it.py -f works/candycane.pix
  sleep 3
  sudo works/text.py -w "Merry Christmas!" -c 0xff0000
  sudo works/pixel-it.py -f works/tree.pix
  sleep 3
  sudo works/pixel-it.py -f works/santahat.pix
  sleep 3
  sudo works/text.py -w "Happy New Year!"
  sudo works/pixel-it.py -f works/wreath.pix
  sleep 3
done



