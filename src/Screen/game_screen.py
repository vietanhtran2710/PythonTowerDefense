from Utils.texture import Texture
from Screen.screen import Screen
from Entity.game_field import GameField
from Entity.menu import Menu
from Entity.player import Player

class GameScreen(Screen):
    def __init__(self, x, y):
        self.on_display = False
        self.width, self.height = x, y
        self.background = Texture("./../res/res/GFX/Game/Tilemap/Ground/Background.png")
        self.background.scale = self.width / self.background.sprite.width
        self.field = GameField()
        self.menu = Menu()

    def draw(self):
        self.background.draw()
        self.field.draw_entities()
        self.menu.draw()

    def on_mouse_motion(self, x, y):
        pass

    def on_mouse_click(self, x, y):
        pass
