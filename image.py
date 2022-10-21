from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

import phrases

def change_image(img):
    """Add text to the image"""
    width_ratio = 0.8
    font_family = "./font.ttf"
    text = phrases.get_phrase()
    img_byte_array = BytesIO()
    
    image = Image.open(BytesIO(img))
    image_editable = ImageDraw.Draw(image)
    font_size = find_font_size(text, font_family, image, width_ratio)
    font = ImageFont.truetype(font_family, font_size)
    print(f"Font size found = {font_size} - Target ratio = {width_ratio} - Measured ratio = {get_text_size(text, image, font)[0] / image.width}")
    
    image_editable.text((20, image.height - 15), text, (0, 0, 0), font=font, anchor="ld")
    image_editable.text((15, image.height - 20), text, (255, 255, 255), font=font, anchor="ld")
    image.save(img_byte_array, format='JPEG')
    return img_byte_array


def get_text_size(text, image, font):
    im = Image.new('RGB', (image.width, image.height))
    draw = ImageDraw.Draw(im) 
    return draw.textsize(text, font)


def find_font_size(text, font, image, target_width_ratio):
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = tested_font_size / (observed_width / image.width) * target_width_ratio
    return round(estimated_font_size)