from generate_html import create_div_pixel


def has_transparency(img) -> bool:
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    return False


def generate_div_pixels(width: int, height: int, pixels, img_is_transparent: bool) -> str:
    div_pixels = ''
    for y in range(height):
        for x in range(width):
            if img_is_transparent:
                r, g, b, a = pixels[x, y]
                div_pixels += create_div_pixel(r, g, b, a)
            else:
                r, g, b = pixels[x, y]
                div_pixels += create_div_pixel(r, g, b)
    return div_pixels
