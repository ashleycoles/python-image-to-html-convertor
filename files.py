from PIL import Image


def create_destination_file(file_path: str):
    try:
        return open(file_path + '.html', 'x')
    except FileExistsError:
        print('Error: Destination file already exists\n')
        exit(0)


def write_to_destination_file(file, content: str):
    file.write(content)
    file.close()


def open_source_image(file_path: str):
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        print('Error: Source image file does not exist\n')
        exit(0)
