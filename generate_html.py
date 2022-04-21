def create_div_pixel_shortcut(r, g, b):
    if r == 0 & g == 0 & b == 0:
        return "<i b></i>"
    elif r == 255 & g == 255 & b == 255:
        return "<i w></i>"
    elif r == 255 & g == 0 & b == 0:
        return "<i r></i>"
    elif r == 0 & g == 255 & b == 0:
        return "<i g></i>"
    elif r == 0 & g == 0 & b == 255:
        return "<i bl></i>"
    return False


def create_div_pixel(r, g, b, a=False) -> str:
    if a is not False:
        if a == 255:  # If the pixel has no alpha, just use a hex code
            shortcut = create_div_pixel_shortcut(r, g, b)  # Attempt to generate a shortcut to save room in the HTML
            if shortcut:
                return shortcut

            hex_code = '#%02x%02x%02x' % (r, g, b)
            return f"<i style='background: {hex_code};'></i>"
        elif a == 0:  # If the pixel is totally invisible, just skip assigning a background
            return f"<i></i>"
        # Otherwise, use rgba
        adjusted_a = a / 255  # the a in RGBA should be from 0 to 1, so account for that here
        return f"<i style='background: rgba({r}, {g}, {b}, {adjusted_a});'></i>"
    else:
        shortcut = create_div_pixel_shortcut(r, g, b)  # Attempt to generate a shortcut to save room in the HTML
        if shortcut:
            return shortcut
        hex_code = '#%02x%02x%02x' % (r, g, b)
        return f"<i style='background: {hex_code};'></i>"


def generate_html_start(width: int, height: int) -> str:
    return "<style>.img i{ width: 1px; height: 1px; display: inline-block; } .img{ width: " + str(
        width) + "px; height: " + str(height) + "px  }" \
                                                "i[b] {background: #000;} " \
                                                "i[w] {background: #fff;}" \
                                                "i[r] {background: #ff0000;}" \
                                                "i[g] {background: #00ff00;}" \
                                                "i[bl] {background: #00ff00;}" \
                                                "</style><body><div class='img'>"


def generate_html_end() -> str:
    return '</div></body>'
