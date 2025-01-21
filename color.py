
# Name	Hex https://en.wikipedia.org/wiki/Web_colors
White	= 0xFFFFFF # W
Silver	= 0xC0C0C0 # S
Gray	= 0x808080 # g little G
Black	= 0x000000 # . or " " Space
Red	= 0xFF0000 # R
Maroon	= 0x800000 # M
Yellow	= 0xFFFF00 # Y
Olive	= 0x808000 # o little O
Lime	= 0x00FF00 # L
Green	= 0x008000 # G
Aqua	= 0x00FFFF # A
Teal	= 0x008080 # T
Blue	= 0x0000FF # B
Navy	= 0x000080 # N
Fuchsia	= 0xFF00FF # F
Purple	= 0x800080 # P


def which_color(element):
    if element == "W":
        color = White
    elif element == "S":
        color = Silver
    elif element == "g":
        color = Gray
    elif element == " " or element == ".":
        color = Black
    elif element == "R":
        color = Red
    elif element == "M":
        color = Maroon
    elif element == "Y":
        color = Yellow
    elif element == "o":
        color = Olive
    elif element == "L":
        color = Lime
    elif element == "G":
        color = Green
    elif element == "A":
        color = Aqua
    elif element == "T":
        color = Teal
    elif element == "B":
        color = Blue
    elif element == "N":
        color = Navy
    elif element == "F":
        color = Fuchsia
    elif element == "P":
        color = Purple
    else:
        color = White
        print("BAD COLOR LETTER")
    return color

def valid_color(c):
  if str(c) == "White" or str(c) == "Silver" or str(c) == "Gray" or str(c) == "Black" or str(c) == "Red" or str(c) == "Maroon" or str(c) == "Yellow" or str(c) == "Olive" or str(c) == "Lime" or str(c) == "Green" or str(c) == "Aqua" or str(c) == "Teal" or str(c) == "Blue" or str(c) == "Navy" or str(c) == "Fuchsia" or str(c) == "Purple":
    return True
  if isinstance(c, int):
    return True
  return False

