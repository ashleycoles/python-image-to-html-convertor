def create_div_pixel(r, g, b, a=False) -> str:
    if a is not False:
        if a == 255:  # If the pixel has no alpha, just use a hex code
            hex_code = '#%02x%02x%02x' % (r, g, b)
            return f"<i style='background: {hex_code};'></i>"
        elif a == 0:  # If the pixel is totally invisible, just skip assigning a background
            return f"<i></i>"
        # Otherwise, use rgba
        adjusted_a = a / 255  # the a in RGBA should be from 0 to 1, so account for that here
        return f"<i style='background: rgba({r}, {g}, {b}, {adjusted_a});'></i>"
    else:
        hex_code = '#%02x%02x%02x' % (r, g, b)
        return f"<i style='background: {hex_code};'></i>"


def generate_html_start(width: int, height: int) -> str:
    return "<style>.img i{ width: 1px; height: 1px; display: inline-block; } .img{ width: " + str(
        width) + "px; height: " + str(height) + "px  }</style><body><div class='img'>"


def generate_html_end() -> str:
    return '</div></body>'
