import pyglet
from Utils.image_grid import Grid

class Menu(object):
    def __init__(self):
        self.selling_towers = []
        images_path = [
        "../res/res/GFX/Game/Tower/Normal Tower/NormalTower.png",
        "../res/res/GFX/Game/Tower/Sniper Tower/SniperTower.png",
        "../res/res/GFX/Game/Tower/Machine Gun Tower/MachineGunTower.png"
        ]
        self.grid = [Grid(pyglet.image.load(path), 1, 5) for path in images_path]
        self.grid[0].scale(1.5)
        self.grid[0].set_coordinate(50, 30)

        self.grid[1].scale(1.5)
        self.grid[1].set_coordinate(50 + self.grid[0].get_width() + 50, 30)

        self.grid[2].scale(1.5)
        self.grid[2].set_coordinate(self.grid[1].get_x() + self.grid[0].get_width() + 50, 30)

    def draw(self):
        for item in self.grid:
            item.draw()
