def create_div_pixel(r, g, b, a=False) -> str:
    if a:
        return f"<i style='background: rgba({r}, {g}, {b}, {a});'></i>"
    else:
        return f"<i style='background: rgb({r}, {g}, {b});'></i>"


def generate_html_start(width: int, height: int) -> str:
    return "<style>.img i{ width: 1px; height: 1px; display: inline-block; } .img{ width: " + str(
        width) + "px; height: " + str(height) + "px  }</style><body><div class='img'>"


def generate_html_end() -> str:
    return '</div></body>'
