#!/bin/bash

if [ -f works/clear.py ]; then
  CLEAR=works/clear.py
elif [ -f ./clear.py ]; then
  CLEAR=./clear.py
fi
if [ -s "$CLEAR" ]; then
  sudo $CLEAR
else
  echo "clear.py not fount"
fi
