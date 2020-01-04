from Utils.texture import Texture
from Screen.screen import Screen

class GameScreen(Screen):
    def __init__(self, x, y):
        self.on_display = False
        self.width, self.height = x, y
        self.background = Texture("./../res/res/GFX/GUI/Background/Background_main_screen.jpg")
        self.background.scale = self.width / self.background.sprite.width

    def draw(self):
        pass

    def on_mouse_click(self, x, y):
        pass
