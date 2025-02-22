import pygame as pg
from game.game import Game
from game.menu import Menu
from game.settings import FPS, DISPLAY_MODE
import os


def main():
    pg.init()
    pg.mixer.init()

    resolution, flag = DISPLAY_MODE
    screen = pg.display.set_mode(resolution, flag)
    clock = pg.time.Clock()
    fps = FPS

    music_path = os.path.join(os.path.dirname(__file__), 'assets/musics/The-Rolling-Stones-Paint-It-Black.mp3')
    pg.mixer.music.load(music_path)
    pg.mixer.music.play(-1, 0, 0)

    state = {
        "running": True,
        "playing": False
    }

    # Implementing Menus
    menu = Menu(screen, state)

    # Implementing Game
    game = Game(screen, state, clock, fps)

    while state['running']:
        if state['playing']:
            # Game Logic Here ...
            game.run()
        # Start Menu Here ...
        menu.run()


    pg.mixer.stop()

if __name__ == '__main__':
    main()
