import pyglet
from Utils.drawing_util import Utils

class Texture(Utils):
    def __init__(self, *args):
        if len(args) == 1:
            path = args[0]
            self.image = pyglet.image.load(path)
            self.sprite = pyglet.sprite.Sprite(self.image)
        elif len(args) == 3:
            path, x, y = args[0], args[1], args[2]
            self.image = pyglet.image.load(path)
            self.sprite = pyglet.sprite.Sprite(self.image)
            self.sprite.x, self.sprite.y = x, y

    def change_image(self, path):
        backup_data = (self.sprite.scale, self.sprite.x, self.sprite.y)
        self.image = pyglet.image.load(path)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.sprite.scale = backup_data[0]
        self.sprite.x, self.sprite.y = backup_data[1], backup_data[2]
