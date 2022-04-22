from PIL import Image
from files import create_destination_file, open_source_image, write_to_destination_file
from generate_html import generate_html_start, generate_html_end


def create_hex_colour_string(red: int, green: int, blue: int):
    return '%02x%02x%02x' % (red, green, blue)


def generate_rgb_shortcuts(width: int, height: int, pixels):
    shortcut_num = 0
    hex_shortcuts = {}
    for y in range(height):  # Loop through each row of pixels
        for x in range(width):  # Loop through each column of pixels
            red, green, blue = pixels[x, y]
            hex_string = create_hex_colour_string(red, green, blue)
            if hex_string not in hex_shortcuts:  # Add all unique RGB codes to the list of shortcuts
                # Use an incrementing number for each unique RGB code encountered
                hex_shortcuts[hex_string] = 's' + str(shortcut_num)
                shortcut_num += 1
    return hex_shortcuts


def map_rgb_shortcuts_to_image(img_width: int, img_height: int, img_pixels, img_rgb_shortcuts):
    mapped_shortcuts = []
    # Generate a nested list of each row in the image, containing the unique attribute for each pixel
    for y in range(img_height):  # Loop through each row of pixels
        # Add a new row into the mapped list of pixels
        mapped_shortcuts.append([])
        for x in range(img_width):  # Loop through each column of pixels
            red, green, blue = img_pixels[x, y]
            rgb_string = create_hex_colour_string(red, green, blue)
            mapped_shortcuts[y].append(img_rgb_shortcuts[rgb_string])  # Get the RGB shortcut for each pixel
    return mapped_shortcuts


def generate_shortcut_css(img_hex_shortcuts: dict) -> str:
    css = ''
    for hex_code in img_hex_shortcuts:
        css += 'i[' + img_hex_shortcuts[hex_code] + ']{' + 'background:#' + hex_code + '}'
    return css


def generate_html_pixels(shortcuts):
    html_pixels = ''
    for row in shortcuts:
        for pixel_hex in row:
            html_pixels += f"<i {pixel_hex}></i>"
    return html_pixels


print('Welcome to the Image to HTML convertor\n')
print('By Ash C\n')

img_path = input('Enter the image name you would like to use:\n')
destination_path = input('Enter the name for the destination file (leave out .html):\n')

image = open_source_image(img_path)
pixels = image.load()
width, height = image.size

rgb_shortcuts = generate_rgb_shortcuts(width, height, pixels)
mapped_rgb_shortcuts = map_rgb_shortcuts_to_image(width, height, pixels, rgb_shortcuts)

rgb_css = generate_shortcut_css(rgb_shortcuts)

result = generate_html_start(width, height, rgb_css)
result += generate_html_pixels(mapped_rgb_shortcuts)
result += generate_html_end()

# print(mapped_rgb_shortcuts)

file = create_destination_file(destination_path)
write_to_destination_file(file, result)
