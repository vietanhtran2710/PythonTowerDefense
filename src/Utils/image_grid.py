import pyglet
from Utils.drawing_util import Utils

class Grid(Utils):
    def __init__(self, *args):
        # path, row, col
        if len(args) == 3:
            path, row, col = args[0], args[1], args[2]
            self.length = col
            self.grid = pyglet.image.ImageGrid(path, row, col)
            self.sprite = pyglet.sprite.Sprite(self.grid[0])
        # path, row, col, x, y
        if len(args) == 5:
            path, row, col = args[0], args[1], args[2]
            self.grid = pyglet.image.ImageGrid(path, row, col)
            self.sprite = pyglet.sprite.Sprite(self.grid[0])
            x, y = args[-1], args[-2]
            self.set_coordinate(x, y)

    def change(self, cell):
        self.sprite = pyglet.sprite.Sprite(self.grid[cell])

    def change_draw(self, cell):
        self.sprite = pyglet.sprite.Sprite(self.grid[cell])
        self.sprite.draw()

    def draw(self):
        self.sprite.draw()

    def get_width(self):
        return self.sprite.width
