from PIL import Image


def generate_thumbnail(file):
    i = Image.open(file)
    width, height = i.size
    side = min(width, height)
    left, upper = (width - side) // 2, (height - side) // 2
    right, lower = left + side, upper + side
    i = i.crop((left, upper, right, lower))
    i.thumbnail((200, 200))
    return i