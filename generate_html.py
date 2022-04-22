

def generate_html_start(width: int, height: int, shortcuts: str) -> str:
    return "<style>div i{width: 1px; height: 1px; display: inline-block;} div{ width: " + str(
        width) + "px; height: " + str(height) + "px  }" + shortcuts + '</style><div>'


def generate_html_end() -> str:
    return '</div></body>'
