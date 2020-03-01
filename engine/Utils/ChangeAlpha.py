
def ChangeAlpha(image, alpha) -> None:
    _width, _height = image.get_size()
    
    for i in range(_width * _height):
        x = i // _width
        y = i % _height
        r, g, b, old_alpha = image.get_at((x, y))
        if (old_alpha > 0): image.set_at((x, y), (r, g, b, alpha))
