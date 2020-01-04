class Screen(object):
    def __init__(self):
        self.on_display = False

    def draw(self):
        pass

    def mouse_clicked(self, x, y):
        pass

    def on_mouse_motion(self, x, y):
        pass

    def on_hover(self, x, y, sprite):
        if sprite.get_x() <= x <= sprite.get_x() + sprite.get_width():
            if sprite.get_y() <= y <= sprite.get_y() + sprite.get_height():
                return True
        return False
