from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from string import ascii_letters

import phrases
import textwrap

def change_image(img):
    """Add text to the image"""
    font_family = "./resources/font.ttf"
    text = phrases.get_phrase()
    img_byte_array = BytesIO()
    
    image = Image.open(BytesIO(img))
    image_editable = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_family, 60)

    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    max_char_count = int(image.size[0] / avg_char_width)
    text = textwrap.fill(text=text, width=max_char_count)
    image_editable.text(xy=(image.size[0]/2, image.size[1]-20), fill=(0,0,0), text=text, font=font, anchor='md')
    image_editable.text(xy=(image.size[0]/2+5, image.size[1]-25), fill=(255,255,255), text=text, font=font, anchor='md')

    
#   image_editable.text((20, image.height - 15), text, (0, 0, 0), font=font, anchor="ld")
#   image_editable.text((15, image.height - 20), text, (255, 255, 255), font=font, anchor="ld")
    image.save(img_byte_array, format='JPEG')
    return img_byte_array