from Utils.texture import Texture
from Screen.screen import Screen
import pyglet

class StartScreen(Screen):
    def __init__(self, x, y):
        self.on_display = True
        self.width, self.height = x, y
        self.start_button_on_hover, self.load_button_on_hover = False, False
        self.switched, self.load = False, False

        path = ["./../res/res/GFX/GUI/Background/Background_main_screen.jpg",
                "./../res/res/GFX/GUI/Button/button.png",
                "./../res/res/GFX/GUI/Button/button-selected.png",
                "./../res/res/GFX/GUI/Button/LoadButton.png",
                "./../res/res/GFX/GUI/Button/LoadButton_selected.png",]
        background_image_path = path[0]
        self.start_button_image_path = [path[1], path[2]]
        self.load_button_image_path = [path[3], path[4]]

        self.background = Texture(path[0])
        self.background.scale(self.width / self.background.get_width())

        self.start_button = Texture(self.start_button_image_path[0])
        x = self.width // 2 - (self.start_button.get_width() // 2)
        y = self.height // 2 - 150
        self.start_button.set_coordinate(x, y)

        self.load_button = Texture(self.load_button_image_path[0])
        x = self.width // 2 - (self.start_button.get_width() // 2)
        y = self.height // 2 - self.start_button.get_height() - 150
        scale_ratio = self.start_button.get_width() / self.load_button.get_width()
        self.load_button.set_coordinate(x, y)
        self.load_button.scale(scale_ratio)

    def draw(self):
        self.background.draw()
        self.start_button.draw()
        self.load_button.draw()

    def mouse_clicked(self, x, y):
        if self.start_button_on_hover:
            self.on_display, self.switched = False, True
        elif self.load_button_on_hover:
            try:
                with open("save_data.txt", "r") as f:
                    self.on_display, self.switched = False, True
                    self.load = True
            except FileNotFoundError:
                pass

    def on_mouse_motion(self, x, y):
        if self.on_hover(x, y, self.start_button):
            if not self.start_button_on_hover:
                self.start_button.change_image(self.start_button_image_path[1])
                self.start_button_on_hover = True
        elif self.start_button_on_hover:
                self.start_button.change_image(self.start_button_image_path[0])
                self.start_button_on_hover = False
        if self.on_hover(x, y, self.load_button):
            if not self.load_button_on_hover:
                self.load_button.change_image(self.load_button_image_path[1])
                self.load_button_on_hover = True
        elif self.load_button_on_hover:
                self.load_button.change_image(self.load_button_image_path[0])
                self.load_button_on_hover = False
