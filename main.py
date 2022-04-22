from PIL import Image
from files import create_destination_file, open_source_image, write_to_destination_file
from generate_html import generate_html_start, generate_html_end


def create_rgb_string(red: int, green: int, blue: int):
    return f"{red}, {green}, {blue}"


def generate_rgb_shortcuts(width: int, height: int, pixels):
    shortcut_num = 0
    rgb_shortcuts = {}
    for y in range(height):  # Loop through each row of pixels
        for x in range(width):  # Loop through each column of pixels
            red, green, blue = pixels[x, y]
            rgb_string = create_rgb_string(red, green, blue)
            if rgb_string not in rgb_shortcuts:  # Add all unique RGB codes to the list of shortcuts
                # Use an incrementing number for each unique RGB code encountered
                rgb_shortcuts[rgb_string] = 's' + str(shortcut_num)
                shortcut_num += 1
    return rgb_shortcuts


def map_rgb_shortcuts_to_image(img_width: int, img_height: int, img_pixels, img_rgb_shortcuts):
    mapped_shortcuts = []
    # Generate a nested list of each row in the image, containing the unique attribute for each pixel
    for y in range(img_height):  # Loop through each row of pixels
        # Add a new row into the mapped list of pixels
        mapped_shortcuts.append([])
        for x in range(img_width):  # Loop through each column of pixels
            red, green, blue = img_pixels[x, y]
            rgb_string = create_rgb_string(red, green, blue)
            mapped_shortcuts[y].append(img_rgb_shortcuts[rgb_string])  # Get the RGB shortcut for each pixel
    return mapped_shortcuts


def generate_rgb_shortcut_css(img_rgb_shortcuts: dict) -> str:
    css = ''
    for rgb in img_rgb_shortcuts:
        css += 'i[' + img_rgb_shortcuts[rgb] + ']{' + 'background:rgb(' + rgb + ')}'
    return css


def generate_html_pixels(shortcuts):
    html_pixels = ''
    for row in shortcuts:
        for pixel in row:
            html_pixels += f"<i {pixel}></i>"
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

rgb_css = generate_rgb_shortcut_css(rgb_shortcuts)

result = generate_html_start(width, height, rgb_css)
result += generate_html_pixels(mapped_rgb_shortcuts)
result += generate_html_end()

# print(mapped_rgb_shortcuts)

file = create_destination_file(destination_path)
write_to_destination_file(file, result)
