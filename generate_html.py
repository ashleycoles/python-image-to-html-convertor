def create_div_pixel(r, g, b, a=False) -> str:
    if a:
        return f"<div class='pixel' style='background-color: rgba({r}, {g}, {b}, {a});'></div>"
    else:
        return f"<div class='pixel' style='background-color: rgb({r}, {g}, {b});'></div>"


def generate_html_start(width: int, height: int) -> str:
    return "<style>.pixel{ width: 1px; height: 1px; display: inline-block; } .img{ width: " + str(
        width) + "px; height: " + str(height) + "px  }</style><body><div class='img'>"


def generate_html_end() -> str:
    return '</div></body>'
