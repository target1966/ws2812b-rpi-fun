from PIL import Image, ImageDraw, ImageFont
import emoji

def emoji_to_bitmap(emoji_char, size=64):
    """Converts an emoji character to a bitmap image."""

    # Create a new image with white background
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    # Render the emoji text
    #font = ImageFont.truetype("Arial.ttf", size)  # Use your desired font
    #font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size)  # Use your desired font
    font = ImageFont.truetype("cour.ttf", size)  # Use your desired font
    #font = ImageFont.load_default()
    print(emoji.emojize(emoji_char))
    draw.text((0, 0), emoji.emojize(emoji_char), font=font, fill="black")

    return img

if __name__ == "__main__":
    emoji_char = ":thumbs_up:"
    emoji_char = ":sun_behind_cloud:"
    bitmap_img = emoji_to_bitmap(emoji_char)
    bitmap_img.save("thumbs_up.bmp")

