import pyglet

class Texture(object):
    def __init__(self, *args):
        print(len(args))
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

    def get_x(self):
        return self.sprite.x

    def get_y(self):
        return self.sprite.y

    def set_x(self, value):
        self.sprite.x = value

    def set_y(self, value):
        self.sprite.y = value

    def set_coordinate(self, x, y):
        self.sprite.x, self.sprite.y = x, y

    def scale(self, ratio):
        self.sprite.scale = ratio

    def get_width(self):
        return self.sprite.width

    def get_height(self):
        return self.sprite.height

    def set_width(self, value):
        self.sprite.width = value

    def set_height(self, value):
        self.sprite.height = value

    def draw(self):
        self.sprite.draw()
