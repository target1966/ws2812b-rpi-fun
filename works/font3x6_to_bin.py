# SPDX-FileCopyrightText: 2018 Tony DiCola for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# https://www.fontspace.com/teeny-tiny-pixls-font-f30095

""" Quick script to convert Adafruit GFX font into binary file.
Taken from glcdfont.c from Adafruit GFX Arduino library. """
# pylint: disable=too-many-lines
# fmt: off
WIDTH = 3
HEIGHT = 6
FONT = (  # Code Page 437 https://www.ascii-codes.com/
    # 0  0x00     NUL (Null)
    "...",
    "...",
    "...",
    "...",
    "...",
    "...",

    # 1  0x01     SOH (Start of Header)
    ".#.",
    "#.#",
    "###",
    "#.#",
    ".#.",
    "...",

    # 2  0x02     STX (Start of Text)
    ".#.",
    "#.#",
    "###",
    "###",
    ".#.",
    "...",

    # 3  0x03     ETX (End of Text)
    "...",
    ".#.",
    "###",
    "###",
    ".#.",
    "...",

    # 4  0x04     EOT (End of Transmission)
    "...",
    ".#.",
    "###",
    "###",
    ".#.",
    ".#.",

    # 5  0x05     ENQ (Enquiry)
    "...",
    ".#.",
    "###",
    "###",
    ".#.",
    "###",

    # 6  0x06     ACK (Acknowledge)
    "...",
    ".##",
    "###",
    "###",
    "##.",
    "###",

    # 7  0x07     BEL (Bell)
    "...",
    ".#.",
    "###",
    "###",
    ".#.",
    "...",

    # 8  0x08     BS  (BackSpace)
    "...",
    "###",
    "###",
    "#.#",
    "###",
    "###",

    # 9  0x09     HT  (Horizontal Tabulation)
    "...",
    ".#.",
    "#.#",
    ".#.",
    "...",
    "...",

    # 10  0x0A     LF  (Line Feed)
    "...",
    "###",
    "###",
    "#.#",
    "#.#",
    "###",

    # 11  0x0B     VT  (Vertical Tabulation)
    "...",
    ".##",
    "..#",
    ".##",
    "#.#",
    ".#.",

    # 12  0x0C     FF  (Form Feed)
    "...",
    "###",
    "###",
    ".#.",
    "###",
    ".#.",

    # 13  0x0D     CR  (Carriage Return)
    "...",
    ".##",
    ".##",
    ".##",
    ".#.",
    "##.",

    # 14  0x0E     SO  (Shift Out)
    "...",
    ".##",
    ".##",
    ".##",
    ".##",
    "##.",

    # 15  0x0F     SI  (Shift In)
    "...",
    ".#.",
    "#.#",
    "#.#",
    ".#.",
    "#.#",

    # 16  0x10     DLE (Data Link Escape)
    "...",
    "#..",
    "##.",
    "###",
    "##.",
    "#..",

    # 17  0x11     DC1 (Device Control 1)
    "...",
    "..#",
    ".##",
    "###",
    ".##",
    "..#",

    # 18  0x12     DC2 (Device Control 2)
    "...",
    ".#.",
    "###",
    ".#.",
    "###",
    ".#.",

    # 19  0x13     DC3 (Device Control 3)
    "#.#",
    "#.#",
    "#.#",
    "...",
    "...",
    "#.#",

    # 20  0x14     DC4 (Device Control 4)
    "...",
    "###",
    "#.#",
    "#.#",
    "#.#",
    "#.#",

    # 21  0x15     NAK (Negative Acknowledge)
    "...",
    ".#.",
    "##.",
    ".#.",
    "#.#",
    ".#.",

    # 22  0x16     SYN (Synchronous Idle)
    "...",
    "...",
    "...",
    "...",
    "###",
    "###",

    # 23  0x17     ETB (End of Transmission Block)
    "...",
    ".#.",
    "###",
    "###",
    ".#.",
    "###",

    # 24  0x18     CAN (Cancel)
    "...",
    ".#.",
    "###",
    ".#.",
    ".#.",
    ".#.",

    # 25  0x19     EM  (End of Medium)
    "...",
    ".#.",
    ".#.",
    ".#.",
    "###",
    ".#.",

    # 26  0x1A     SUB (Substitute)
    "...",
    "#..",
    ".#.",
    "###",
    ".#.",
    "#..",

    # 27  0x1B     ESC (Escape)
    "...",
    "..#",
    ".#.",
    "###",
    ".#.",
    "..#",

    # 28  0x1C     FS  (File Separator)
    "...",
    "...",
    "#..",
    "#..",
    "###",
    "...",

    # 29  0x1D     GS  (Group Separator)
    "...",
    "...",
    ".##",
    "###",
    ".##",
    "...",

    # 30  0x1E     RS  (Record Separator)
    "...",
    "...",
    ".#.",
    "###",
    "###",
    "...",

    # 31  0x1F     US  (Unit Separator)
    "...",
    "...",
    "###",
    "###",
    ".#.",
    "...",

    # 32  0x20     Space
    "...",
    "...",
    "...",
    "...",
    "...",
    "...",

    # 33  0x21  !  Exclamation mark
    ".#.",
    ".#.",
    ".#.",
    ".#.",
    "...",
    ".#.",

    # 34  0x22  "  Quotation Mark
    "#.#",
    "#.#",
    "...",
    "...",
    "...",
    "...",

    # 35  0x23
    "...",
    ".##",
    "###",
    ".##",
    "###",
    ".##",

    # 36  0x24  $  Dollar
    "...",
    ".#.",
    "###",
    "#.#",
    "###",
    ".#.",

    # 37  0x25  %  Percent
    "...",
    "#..",
    "..#",
    ".#.",
    "#..",
    "..#",

    # 38  0x26  &  Ampersand
    "...",
    ".#.",
    "#.#",
    ".#.",
    "#.#",
    ".##",

    # 39  0x27  '  Apostrophe
    "..#",
    ".#.",
    "...",
    "...",
    "...",
    "...",

    # 40  0x28  (  Open bracket
    ".#.",
    "#..",
    "#..",
    "#..",
    "#..",
    ".#.",

    # 41  0x29  )  Close bracket
    ".#.",
    "..#",
    "..#",
    "..#",
    "..#",
    ".#.",

    # 42  0x2A  *  Asterisk
    "...",
    "#.#",
    ".#.",
    "#.#",
    "...",
    "...",

    # 43  0x2B  +  Plus
    "...",
    ".#.",
    "###",
    ".#.",
    "...",
    "...",

    # 44  0x2C  ,  Comma
    "...",
    "...",
    "...",
    "...",
    "..#",
    ".#.",

    # 45  0x2D  -  Dash
    "...",
    "...",
    "###",
    "...",
    "...",
    "...",

    # 46  0x2E  .  Full stop
    "...",
    "...",
    "...",
    "...",
    ".##",
    ".##",

    # 47  0x2F  /  Slash
    "...",
    "..#",
    "..#",
    ".#.",
    "#..",
    "#..",

    # 48  0x30  0  Zero
    "###",
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "###",

    # 49  0x31  1  One
    "##.",
    ".#.",
    ".#.",
    ".#.",
    ".#.",
    "###",

    # 50  0x32  2  Two
    "###",
    "..#",
    "###",
    "#..",
    "#..",
    "###",

    # 51  0x33  3  Three
    "###",
    "..#",
    "###",
    "..#",
    "..#",
    "###",

    # 52  0x34  4  Four
    "#.#",
    "#.#",
    "###",
    "..#",
    "..#",
    "..#",

    # 53  0x35  5  Five
    "###",
    "#..",
    "###",
    "..#",
    "..#",
    "###",

    # 54  0x36  6  Six
    "###",
    "#..",
    "###",
    "#.#",
    "#.#",
    "###",

    # 55  0x37  7  Seven
    "###",
    "#.#",
    "..#",
    "..#",
    "..#",
    "..#",

    # 56  0x38  8  Eight
    "###",
    "#.#",
    "###",
    "#.#",
    "#.#",
    "###",

    # 57  0x39  9  Nine
    "###",
    "#.#",
    "###",
    "..#",
    "..#",
    "..#",

    # 58  0x3A  :  Colon
    "...",
    "...",
    ".#.",
    "...",
    ".#.",
    "...",

    # 59  0x3B  ;  Semicolon
    "...",
    "...",
    ".#.",
    "...",
    ".#.",
    ".#.",

    # 60  0x3C  <  Less than
    "...",
    "..#",
    ".#.",
    "#..",
    ".#.",
    "..#",

    # 61  0x3D  =  Equals sign
    "...",
    "###",
    "...",
    "###",
    "...",
    "...",

    # 62  0x3E  >  Greater than
    "...",
    "#..",
    ".#.",
    "..#",
    ".#.",
    "#..",

    # 63  0x3F  ?  Question mark
    "###",
    "..#",
    "..#",
    ".##",
    "...",
    ".#.",

    # 64  0x40  @  At
    "...",
    "###",
    "#.#",
    "#.#",
    "#..",
    "###",

    # 65  0x41  A  Upper case A
    "###",
    "#.#",
    "###",
    "#.#",
    "#.#",
    "#.#",

    # 66  0x42  B  Upper case B
    "###",
    "#.#",
    "##.",
    "#.#",
    "#.#",
    "###",

    # 67  0x43  C  Upper case C
    "###",
    "#..",
    "#..",
    "#..",
    "#..",
    "###",

    # 68  0x44  D  Upper case D
    "##.",
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "##.",

    # 69  0x45  E  Upper case E
    "###",
    "#..",
    "###",
    "#..",
    "#..",
    "###",

    # 70  0x46  F  Upper case F
    "###",
    "#..",
    "###",
    "#..",
    "#..",
    "#..",

    # 71  0x47  G  Upper case G
    "###",
    "#..",
    "#..",
    "#.#",
    "#.#",
    "###",

    # 72  0x48  H  Upper case H
    "#.#",
    "#.#",
    "###",
    "#.#",
    "#.#",
    "#.#",

    # 73  0x49  I  Upper case I
    "###",
    ".#.",
    ".#.",
    ".#.",
    ".#.",
    "###",

    # 74  0x4A  J  Upper case J
    "..#",
    "..#",
    "..#",
    "..#",
    "#.#",
    "###",

    # 75  0x4B  K  Upper case K
    "#.#",
    "#.#",
    "##.",
    "#.#",
    "#.#",
    "#.#",

    # 76  0x4C  L  Upper case L
    "#..",
    "#..",
    "#..",
    "#..",
    "#..",
    "###",

    # 77  0x4D  M  Upper case M
    "#.#",
    "###",
    "#.#",
    "#.#",
    "#.#",
    "#.#",

    # 78  0x4E  N  Upper case N
    "###",
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "#.#",

    # 79  0x4F  O  Upper case O
    "###",
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "###",

    # 80  0x50  P  Upper case P
    "###",
    "#.#",
    "###",
    "#..",
    "#..",
    "#..",

    # 81  0x51  Q  Upper case Q
    "###",
    "#.#",
    "#.#",
    "#.#",
    "##.",
    "#.#",

    # 82  0x52  R  Upper case R
    "###",
    "#.#",
    "##.",
    "#.#",
    "#.#",
    "#.#",

    # 83  0x53  S  Upper case S
    "###",
    "#..",
    "###",
    "..#",
    "..#",
    "###",

    # 84  0x54  T  Upper case T
    "###",
    ".#.",
    ".#.",
    ".#.",
    ".#.",
    ".#.",

    # 85  0x55  U  Upper case U
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "###",

    # 86  0x56  V  Upper case V
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    ".#.",

    # 87  0x57  W  Upper case W
    "#.#",
    "#.#",
    "#.#",
    "#.#",
    "###",
    "#.#",

    # 88  0x58  X  Upper case X
    "#.#",
    "#.#",
    ".#.",
    "#.#",
    "#.#",
    "#.#",

    # 89  0x59  Y  Upper case Y
    "#.#",
    "#.#",
    "###",
    ".#.",
    ".#.",
    ".#.",

    # 90  0x5A  Z  Upper case Z
    "###",
    "..#",
    ".#.",
    "#..",
    "#..",
    "###",

    # 91  0x5B  [  Open square bracket
    "###",
    "#..",
    "#..",
    "#..",
    "#..",
    "###",

    # 92  0x5C  \  Backslash
    "#..",
    "#..",
    ".#.",
    ".#.",
    "..#",
    "..#",

    # 93  0x5D  ]  Close square bracket
    "###",
    "..#",
    "..#",
    "..#",
    "..#",
    "###",

    # 94  0x5E  ^  Caret
    ".#.",
    "#.#",
    "...",
    "...",
    "...",
    "...",

    # 95  0x5F  _  Underscore
    "...",
    "...",
    "...",
    "...",
    "...",
    "###",

    # 96  0x60  @  Grave accent
    "#..",
    ".#.",
    "...",
    "...",
    "...",
    "...",

    # 97  0x61  a  Lower case a
    "...",
    "...",
    ".##",
    "#.#",
    "#.#",
    ".##",

    # 98  0x62  b  Lower case b
    "...",
    "#..",
    "#..",
    "###",
    "#.#",
    "###",

    # 99  0x63  c  Lower case c
    "...",
    "...",
    "###",
    "#..",
    "#..",
    "###",

    # 100  0x64  d  Lower case d
    "...",
    "..#",
    "..#",
    "###",
    "#.#",
    "###",

    # 101  0x65  e  Lower case e
    "...",
    "...",
    ".##",
    "#.#",
    "##.",
    ".##",

    # 102  0x66  f  Lower case f
    "...",
    "..#",
    ".#.",
    "###",
    ".#.",
    ".#.",

    # 103  0x67  g  Lower case g
    "...",
    "...",
    "##.",
    "#.#",
    ".##",
    "##.",

    # 104  0x68  h  Lower case h
    "...",
    "#..",
    "#..",
    "###",
    "#.#",
    "#.#",

    # 105  0x69  i  Lower case i
    "...",
    ".#.",
    "...",
    ".#.",
    ".#.",
    "###",

    # 106  0x6A  j  Lower case j
    "...",
    "..#",
    "...",
    "..#",
    "..#",
    "##.",

    # 107  0x6B  k  Lower case k
    "...",
    "#..",
    "#.#",
    "##.",
    "#.#",
    "#.#",

    # 108  0x6C  l  Lower case l
    "...",
    "##.",
    ".#.",
    ".#.",
    ".#.",
    ".##",

    # 109  0x6D  m  Lower case m
    "...",
    "...",
    "#.#",
    "###",
    "#.#",
    "#.#",

    # 110  0x6E  n  Lower case n
    "...",
    "...",
    "###",
    "#.#",
    "#.#",
    "#.#",

    # 111  0x6F  o  Lower case o
    "...",
    "...",
    "...",
    "###",
    "#.#",
    "###",

    # 112  0x70  p  Lower case p
    "...",
    "...",
    "###",
    "#.#",
    "###",
    "#..",

    # 113  0x71  q  Lower case q
    "...",
    "...",
    "###",
    "#.#",
    "###",
    "..#",

    # 114  0x72  r  Lower case r
    "...",
    "...",
    "###",
    "#..",
    "#..",
    "#..",

    # 115  0x73  s  Lower case s
    "...",
    "...",
    ".##",
    "##.",
    ".##",
    "##.",

    # 116  0x74  t  Lower case t
    "...",
    ".#.",
    "###",
    ".#.",
    ".#.",
    ".##",

    # 117  0x75  u  Lower case u
    "...",
    "...",
    "...",
    "#.#",
    "#.#",
    "###",

    # 118  0x76  v  Lower case v
    "...",
    "...",
    "...",
    "#.#",
    "#.#",
    ".#.",

    # 119  0x77  w  Lower case w
    "...",
    "...",
    "#.#",
    "#.#",
    "###",
    "#.#",

    # 120  0x78  x  Lower case x
    "...",
    "...",
    "#.#",
    ".#.",
    "#.#",
    "#.#",

    # 121  0x79  y  Lower case y
    "...",
    "...",
    "#.#",
    "#.#",
    "###",
    "..#",

    # 122  0x7A  z  Lower case z
    "...",
    "...",
    "###",
    ".##",
    "#..",
    "###",

    # 123  0x7B  {  Open brace
    "...",
    ".##",
    ".#.",
    "##.",
    ".#.",
    ".##",

    # 124  0x7C  |  Pipe
    ".#.",
    ".#.",
    ".#.",
    ".#.",
    ".#.",
    ".#.",

    # 125  0x7D  }  Close brace
    "...",
    "##.",
    ".#.",
    ".##",
    ".#.",
    "##.",

    # 126  0x7E  ~  Tilde
    "..#",
    "###",
    "#..",
    "...",
    "...",
    "...",

    # 127  0x7F     Delete
    "...",
    ".#.",
    "###",
    "#.#",
    "###",
    "...",

    # 128  0x80     Upper case C with cedilla
    "...",
    "###",
    "#..",
    "#..",
    "###",
    ".#.",

    # 129  0x81     Lower case u with diaeresis
    "...",
    "...",
    "#.#",
    "#.#",
    "#.#",
    "###",

    # 130  0x82     Lower case e with acute
    "...",
    "..#",
    "###",
    "###",
    "#..",
    ".##",

    # 131  0x83     Lower case a with circumflex
    "...",
    "###",
    ".#.",
    ".##",
    "#.#",
    ".##",

    # 132  0x84     Lower case a with diaeresis
    "...",
    "#.#",
    ".#.",
    ".##",
    "#.#",
    ".##",

    # 133  0x85     Lower case a with grave
    "...",
    "#..",
    ".#.",
    ".##",
    "#.#",
    ".##",

    # 134  0x86     Lower case a with ring above
    "...",
    "..#",
    ".##",
    ".##",
    "#..",
    ".##",

    # 135  0x87     Lower case c with cedilla
    "...",
    ".##",
    "##.",
    "##.",
    ".##",
    "..#",

    # 136  0x88     Lower case e with circumflex
    "...",
    "###",
    ".#.",
    "###",
    "#..",
    ".##",

    # 137  0x89     Lower case e with diaeresis
    "...",
    "#.#",
    ".#.",
    "###",
    "#..",
    ".##",

    # 138  0x8A     Lower case e with grave
    "...",
    "#..",
    ".#.",
    "###",
    "#..",
    ".##",

    # 139  0x8B     Lower case i with diaeresis
    "...",
    "#.#",
    ".#.",
    ".#.",
    ".#.",
    "###",

    # 140  0x8C     Lower case i with circumflex
    "...",
    "##.",
    "#.#",
    ".#.",
    ".#.",
    "###",

    # 141  0x8D     Lower case i with grave
    "...",
    "##.",
    ".##",
    ".#.",
    ".#.",
    "###",

    # 142  0x8E     Upper case A with diaeresis
    "...",
    "#.#",
    ".#.",
    "#.#",
    "###",
    "#.#",

    # 143  0x8F     Upper case A with ring above
    "...",
    ".#.",
    ".#.",
    "#.#",
    "###",
    "#.#",

    # 144  0x90     Upper case E with acute
    "...",
    "..#",
    "###",
    "##.",
    "#..",
    "###",

    # 145  0x91     Lower case ae
    "...",
    ".##",
    "..#",
    ".##",
    "#.#",
    ".##",

    # 146  0x92     Upper case AE
    "...",
    ".##",
    "#.#",
    "###",
    "#.#",
    "#.#",

    # 147  0x93     Lower case o with circumflex
    "###",
    "...",
    "###",
    "#.#",
    "###",
    "...",

    # 148  0x94     Lower case o with diaeresis
    "...",
    "#.#",
    "###",
    "#.#",
    "#.#",
    "###",

    # 149  0x95     Lower case o with grave
    "#..",
    "...",
    "###",
    "#.#",
    "###",
    "...",

    # 150  0x96     Lower case u with circumflex
    "###",
    "...",
    "#.#",
    "###",
    "###",
    "...",

    # 151  0x97     Lower case u with grave
    "#..",
    "...",
    "#.#",
    "#.#",
    "#.#",
    "...",

    # 152  0x98     Lower case y with diaeresis
    "#.#",
    "...",
    "#.#",
    "###",
    "..#",
    "...",

    # 153  0x99     Upper case O with diaeresis
    "#.#",
    ".#.",
    "#.#",
    "#.#",
    "###",
    "...",

    # 154  0x9A     Upper case U with diaeresis
    "#.#",
    "...",
    "#.#",
    "#.#",
    "###",
    "...",

    # 155  0x9B     Cent sign
    "...",
    ".#.",
    "###",
    "##.",
    "###",
    ".#.",

    # 156  0x9C     Pound sign
    "...",
    "..#",
    ".#.",
    "##.",
    ".#.",
    "###",

    # 157  0x9D     Yen sign
    "...",
    "#.#",
    "###",
    ".#.",
    "###",
    ".#.",

    # 158  0x9E     Peseta sign
    "...",
    "##.",
    "#.#",
    "##.",
    "###",
    "#.#",

    # 159  0x9F     Lower case f with hook
    "...",
    ".##",
    ".#.",
    "###",
    ".#.",
    "##.",

    # 160  0xA0     Lower case a with acute
    "...",
    "..#",
    "##.",
    "###",
    "#.#",
    ".##",

    # 161  0xA1     Lower case i with acute
    "...",
    ".##",
    "...",
    ".#.",
    ".#.",
    "###",

    # 162  0xA2     Lower case o with acute
    "...",
    ".##",
    "...",
    "###",
    "#.#",
    "###",

    # 163  0xA3     Lower case u with acute
    "...",
    ".##",
    "...",
    "#.#",
    "#.#",
    "###",

    # 164  0xA4     Lower case n with tilde
    "...",
    "###",
    "...",
    "##.",
    "#.#",
    "#.#",

    # 165  0xA5     Upper case N with tilde
    "###",
    "...",
    "###",
    "#.#",
    "#.#",
    "#.#",

    # 166  0xA6     Feminine ordinal indicator
    "...",
    "###",
    "#.#",
    ".##",
    "...",
    "###",

    # 167  0xA7     Masculine ordinal indicator
    "...",
    "###",
    "#.#",
    "###",
    "...",
    "###",

    # 168  0xA8     Inverted question mark
    ".#.",
    "...",
    ".#.",
    "#..",
    "#..",
    "###",

    # 169  0xA9     Reversed not sign
    "...",
    "...",
    "###",
    "#..",
    "#..",
    "...",

    # 170  0xAA     Not sign
    "...",
    "...",
    "###",
    "..#",
    "..#",
    "...",

    # 171  0xAB     Vulgar fraction one half
    "...",
    "#.#",
    "##.",
    "###",
    "###",
    ".##",

    # 172  0xAC     Vulgar fraction one quarter
    "...",
    "#.#",
    "##.",
    ".##",
    "###",
    "..#",

    # 173  0xAD     Inverted exclamation mark
    ".#.",
    "...",
    ".#.",
    ".#.",
    ".#.",
    ".#.",

    # 174  0xAE     Left-pointing double angle quotation mark
    "...",
    "..#",
    ".#.",
    "#.#",
    ".#.",
    "..#",

    # 175  0xAF     Right-pointing double angle quotation mark
    "...",
    "#..",
    ".#.",
    "#.#",
    ".#.",
    "#..",

    # 176  0xB0     Light shade
    "...",
    "###",
    "#.#",
    "###",
    "...",
    "...",

    # 177  0xB1     Medium shade
    ".#.",
    "#.#",
    ".#.",
    "#.#",
    ".#.",
    "#.#",

    # 178  0xB2     Dark shade
    "###",
    "##.",
    "###",
    "###",
    ".##",
    "###",

    # 179  0xB3     Box drawings light vertical
    "..#",
    "..#",
    "..#",
    "..#",
    "..#",
    "..#",

    # 180  0xB4     Box drawings light vertical and left
    "..#",
    "..#",
    "###",
    "..#",
    "..#",
    "..#",

    # 181  0xB5     Box drawings vertical single and left double
    "..#",
    "###",
    "..#",
    "###",
    "..#",
    "..#",

    # 182  0xB6     Box drawings vertical double and left single
    ".##",
    ".##",
    "###",
    ".##",
    ".##",
    ".##",

    # 183  0xB7     Box drawings down double and left single
    "...",
    "...",
    "...",
    "###",
    ".##",
    ".##",

    # 184  0xB8     Box drawings down single and left double
    ".##",
    "..#",
    "###",
    "..#",
    "..#",
    "..#",

    # 185  0xB9     Box drawings double vertical and left
    ".##",
    "###",
    "..#",
    "###",
    ".##",
    ".##",

    # 186  0xBA     Box drawings double vertical
    ".##",
    ".##",
    ".##",
    ".##",
    ".##",
    ".##",

    # 187  0xBB     Box drawings double down and left
    "...",
    "###",
    "..#",
    "###",
    ".##",
    ".##",

    # 188  0xBC     Box drawings double up and left
    ".##",
    "###",
    "..#",
    "###",
    "...",
    "...",

    # 189  0xBD     Box drawings up double and left single
    ".##",
    ".##",
    ".##",
    "###",
    "...",
    "...",

    # 190  0xBE     Box drawings up single and left double
    "..#",
    "###",
    "..#",
    "###",
    "...",
    "...",

    # 191  0xBF     Box drawings light down and left
    "...",
    "...",
    "###",
    "..#",
    "..#",
    "..#",

    # 192  0xC0     Box drawings light up and right
    ".#.",
    ".#.",
    ".#.",
    ".##",
    "...",
    "...",

    # 193  0xC1     Box drawings light up and horizontal
    ".#.",
    ".#.",
    ".#.",
    "###",
    "...",
    "...",

    # 194  0xC2     Box drawings light down and horizontal
    "...",
    "...",
    "###",
    ".#.",
    ".#.",
    ".#.",

    # 195  0xC3     Box drawings light vertical and right
    ".#.",
    ".#.",
    ".##",
    ".#.",
    ".#.",
    ".#.",

    # 196  0xC4     Box drawings light horizontal
    "...",
    "...",
    "###",
    "...",
    "...",
    "...",

    # 197  0xC5     Box drawings light vertical and horizontal
    ".#.",
    ".#.",
    "###",
    ".#.",
    ".#.",
    ".#.",

    # 198  0xC6     Box drawings vertical single and right double
    ".#.",
    ".##",
    ".#.",
    ".##",
    ".#.",
    ".#.",

    # 199  0xC7     Box drawings vertical double and right single
    ".##",
    ".##",
    ".##",
    ".##",
    ".##",
    ".##",

    # 200  0xC8     Box drawings double up and right
    ".##",
    ".##",
    ".#.",
    ".##",
    "...",
    "...",

    # 201  0xC9     Box drawings double down and right
    "...",
    ".##",
    ".#.",
    ".##",
    ".##",
    ".##",

    # 202  0xCA     Box drawings double up and horizontal
    ".##",
    "###",
    "...",
    "###",
    "...",
    "...",

    # 203  0xCB     Box drawings double down and horizontal
    "...",
    "###",
    "###",
    ".##",
    ".##",
    ".##",

    # 204  0xCC     Box drawings double vertical and right
    ".##",
    ".##",
    ".#.",
    ".##",
    ".##",
    ".##",

    # 205  0xCD     Box drawings double horizontal
    "...",
    "...",
    "###",
    "###",
    "...",
    "...",

    # 206  0xCE     Box drawings double vertical and horizontal
    ".##",
    ".##",
    "###",
    "###",
    ".##",
    ".##",

    # 207  0xCF     Box drawings up single and horizontal double
    ".#.",
    ".#.",
    "###",
    "###",
    "...",
    "...",

    # 208  0xD0     Box drawings up double and horizontal single
    ".##",
    ".##",
    ".##",
    "###",
    "...",
    "...",

    # 209  0xD1     Box drawings down single and horizontal double
    "...",
    "...",
    "###",
    "###",
    ".#.",
    ".#.",

    # 210  0xD2     Box drawings down double and horizontal single
    "...",
    "...",
    "###",
    ".##",
    ".##",
    ".##",

    # 211  0xD3     Box drawings up double and right single
    ".##",
    ".##",
    ".##",
    "...",
    "...",
    "...",

    # 212  0xD4     Box drawings up single and right double
    ".#.",
    ".##",
    ".#.",
    ".##",
    "...",
    "...",

    # 213  0xD5     Box drawings down single and right double
    "...",
    "...",
    ".##",
    ".##",
    ".#.",
    ".#.",

    # 214  0xD6     Box drawings down double and right single
    "...",
    "...",
    "...",
    ".##",
    ".##",
    ".##",

    # 215  0xD7     Box drawings vertical double and horizontal single
    ".##",
    ".##",
    "###",
    ".##",
    ".##",
    ".##",

    # 216  0xD8     Box drawings vertical single and horizontal double
    ".#.",
    "###",
    ".#.",
    "###",
    ".#.",
    ".#.",

    # 217  0xD9     Box drawings light up and left
    ".#.",
    "##.",
    "...",
    "...",
    "...",
    "...",

    # 218  0xDA     Box drawings light down and right
    "...",
    "...",
    "...",
    ".##",
    ".#.",
    ".#.",

    # 219  0xDB     Full block
    "###",
    "###",
    "###",
    "###",
    "###",
    "###",

    # 220  0xDC     Lower half block
    "...",
    "...",
    "...",
    "###",
    "###",
    "###",

    # 221  0xDD     Left half block
    "##.",
    "##.",
    "##.",
    "##.",
    "##.",
    "##.",

    # 222  0xDE     Right half block
    ".##",
    ".##",
    ".##",
    ".##",
    ".##",
    ".##",

    # 223  0xDF     Upper half block
    "###",
    "###",
    "###",
    "...",
    "...",
    "...",

    # 224  0xE0     Greek lower case alpha
    "...",
    "...",
    ".##",
    "#.#",
    "#.#",
    ".##",

    # 225  0xE1     Lower case sharp s
    "...",
    "##.",
    "#.#",
    "##.",
    "#.#",
    "###",

    # 226  0xE2     Greek upper case letter gamma
    "...",
    "###",
    "#.#",
    "#..",
    "#..",
    "#..",

    # 227  0xE3     Greek lower case pi
    "...",
    "...",
    "###",
    "...",
    "#.#",
    "#.#",

    # 228  0xE4     Greek upper case letter sigma
    "...",
    "###",
    "#.#",
    ".#.",
    "#.#",
    "###",

    # 229  0xE5     Greek lower case sigma
    "...",
    "...",
    ".##",
    "#.#",
    "#.#",
    ".#.",

    # 230  0xE6     Micro sign
    "...",
    "#.#",
    "#.#",
    "#.#",
    ".##",
    "#..",

    # 231  0xE7     Greek lower case tau
    "...",
    "###",
    "##.",
    ".#.",
    ".#.",
    ".#.",

    # 232  0xE8     Greek upper case letter phi
    "###",
    ".#.",
    "#.#",
    "#.#",
    ".#.",
    "###",

    # 233  0xE9     Greek upper case letter theta
    "...",
    ".#.",
    "#.#",
    "###",
    "#.#",
    ".#.",

    # 234  0xEA     Greek upper case letter omega
    ".#.",
    ".#.",
    "#.#",
    "#.#",
    ".#.",
    "#.#",

    # 235  0xEB     Greek lower case delta
    "...",
    ".#.",
    "#..",
    ".#.",
    "#.#",
    ".#.",

    # 236  0xEC     Infinity
    "...",
    ".#.",
    "###",
    "###",
    ".#.",
    "...",

    # 237  0xED     Greek lower case phi
    "...",
    "..#",
    ".#.",
    "#.#",
    ".#.",
    "#..",

    # 238  0xEE     Greek lower case epsilon
    "...",
    ".##",
    "#..",
    "##.",
    "#..",
    ".##",

    # 239  0xEF     Intersection
    "...",
    ".#.",
    "#.#",
    "#.#",
    "#.#",
    "#.#",

    # 240  0xF0     Identical to
    "...",
    "###",
    "...",
    "###",
    "...",
    "###",

    # 241  0xF1     Plus-minus sign
    "...",
    ".#.",
    "###",
    ".#.",
    "...",
    "###",

    # 242  0xF2     Greater-than or equal to
    "#..",
    ".#.",
    "..#",
    ".#.",
    "#..",
    "###",

    # 243  0xF3     Less-than or equal to
    "..#",
    ".#.",
    "#..",
    ".#.",
    "..#",
    "###",

    # 244  0xF4     Top half integral
    "###",
    "#.#",
    "#..",
    "#..",
    "#..",
    "#..",

    # 245  0xF5     Bottom half integral
    "..#",
    "..#",
    "..#",
    "..#",
    "#.#",
    "###",

    # 246  0xF6     Division sign
    ".#.",
    "...",
    "###",
    "...",
    ".#.",
    "...",

    # 247  0xF7     Almost equal to
    "...",
    "#.#",
    "#.#",
    "#.#",
    "...",
    "...",

    # 248  0xF8     Degree sign
    ".#.",
    "#.#",
    ".#.",
    "...",
    "...",
    "...",

    # 249  0xF9     Bullet operator
    "...",
    "...",
    ".##",
    "...",
    "...",
    "...",

    # 250  0xFA     Middle dot
    "...",
    "...",
    ".#.",
    "...",
    "...",
    "...",

    # 251  0xFB     Square root
    ".##",
    ".#.",
    ".#.",
    ".#.",
    "##.",
    ".#.",

    # 252  0xFC     Superscript lower case n
    "##.",
    "#.#",
    "#.#",
    "#.#",
    "...",
    "...",

    # 253  0xFD     Superscript two
    "##.",
    "..#",
    "##.",
    ".##",
    "...",
    "...",

    # 254  0xFE     Black square
    "...",
    ".##",
    ".##",
    ".##",
    "...",
    "...",

    # 255  0xFF     No-break space
    "...",
    "...",
    "...",
    "...",
    "...",
    "...",
)
# fmt: on

if __name__ == "__main__":
    # Rotate all character to be able to generate the correct data
    rotated_font = []
    char = []
    for i, col in enumerate(FONT):
        char.append(col)
        # Has all character data been appended
        if (i + 1) % HEIGHT == 0:
            rot = list(zip(*char[::-1]))
            for r in rot:
                rotated_font.append("".join(r))
            char = []

    with open(f"font{WIDTH}x{HEIGHT}.bin", "wb") as outfile:
        # Write a byte each for the character width, character height.
        outfile.write(bytes((WIDTH, HEIGHT)))
        # Now write all of the font character bytes.
        for string in rotated_font:
            DATA = int(string.replace(".", "0").replace("#", "1"), 2)
            outfile.write(DATA.to_bytes(1, "big"))
