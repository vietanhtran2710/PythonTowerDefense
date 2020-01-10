import pyglet
from Utils.drawing_util import Utils

class Animation(Utils):
    def __init__(self, *args):
        # path, row, col, period
        if len(args) == 4:
            path, row, col, period = args[0], args[1], args[2], args[3]
            self.raw = pyglet.image.load(path)
            self.images = pyglet.image.ImageGrid(self.raw, row, col)
            self.animation = pyglet.image.Animation.from_image_sequence(self.images, period)
            self.sprite = pyglet.sprite.Sprite(self.animation)
        else:
            # path, row, col, period, x, y
            path, row, col, period = args[0], args[1], args[2], args[3]
            x, y = args[-2], args[-1]
            self.raw = pyglet.image.load(path)
            self.images = pyglet.image.ImageGrid(self.raw, row, col)
            self.animation = pyglet.image.Animation.from_image_sequence(self.images, period)
            self.sprite = pyglet.sprite.Sprite(self.animation)
            self.set_coordinate(x, y)
