import pyglet
from pyglet.gl import gl
from pkg_resources import parse_version
from Screen.start_screen import StartScreen
from Screen.game_screen import GameScreen

window = pyglet.window.Window(fullscreen=True)
win_max_x = window.width
win_max_y = window.height

start_screen = StartScreen(win_max_x, win_max_y)
game_screen = GameScreen(win_max_x, win_max_y)

@window.event
def on_draw():
    if start_screen.on_display:
        start_screen.draw()
    else:
        game_screen.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    if start_screen.on_display:
        start_screen.on_mouse_motion(x, y)
    else:
        game_screen.on_mouse_montion(x, y)

@window.event
def mouse_clicked(x, y, button, modifiers):
    if start_screen.on_display:
        start_screen.mouse_clicked(x, y)
    else:
        game_screen.mouse_clicked(x, y)

if __name__ == "__main__":
    screen_index = 0
    pyglet.app.run()
