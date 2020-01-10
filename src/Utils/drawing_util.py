class Utils(object):
    def __init__(self):
        pass

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
