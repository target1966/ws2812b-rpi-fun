import time
import board
import neopixel

# Define the matrix dimensions
MATRIX_WIDTH = 16
MATRIX_HEIGHT = 16
LED_COUNT = MATRIX_WIDTH * MATRIX_HEIGHT

# Configure the GPIO pin used for data output
PIXEL_PIN = board.D18

# Create the NeoPixel object
pixels = neopixel.NeoPixel(PIXEL_PIN, LED_COUNT, brightness=0.05, auto_write=False)

# Function to clear the matrix
def clear():
    pixels.fill((0, 0, 0))
    pixels.show()

# Function to set the color of a single pixel
def set_pixel(x, y, color):
    index = y * MATRIX_WIDTH + x 
    pixels[index] = color

# Example: Display a scrolling message
message = "Hello World!"
color = (255, 0, 0)  # Red

try:
    while True:
        for i in range(len(message) + MATRIX_WIDTH):
            clear()
            for j in range(len(message)):
                char_x = i + j - MATRIX_WIDTH
                if 0 <= char_x < MATRIX_WIDTH:
                    char_y = MATRIX_HEIGHT // 2
                    for k in range(MATRIX_HEIGHT):
                        if message[j] == " ":
                            continue
                        set_pixel(char_x, char_y + k, (255,0,0))
                        #set_pixel(char_x, char_y + k, color)
            pixels.show()
            time.sleep(0.1)

except KeyboardInterrupt:
    clear()

