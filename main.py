from PIL import Image
from files import create_destination_file, open_source_image, write_to_destination_file
from generate_html import generate_html_start, generate_html_end, create_div_pixel
from image import has_transparency, generate_div_pixels


print('Welcome to the Image to HTML convertor\n')
print('By Ash C\n')

img_path = input('Enter the image name you would like to use:\n')
destination_path = input('Enter the name for the destination file (leave out .html):\n')

img = open_source_image(img_path)
pixels = img.load()
width, height = img.size
img_is_transparent = has_transparency(img)

result = generate_html_start(width, height)
result += generate_div_pixels(width, height, pixels, img_is_transparent)
result += generate_html_end()

file = create_destination_file(destination_path)
write_to_destination_file(file, result)
