import pygame as pg
from game.game import Game
from game.menu import Menu
from game.settings import FPS, DISPLAY_MODE


def main():
    running = True
    playing = False

    pg.init()
    resolution, flag = DISPLAY_MODE
    screen = pg.display.set_mode(resolution, flag)
    clock = pg.time.Clock()
    fps = FPS

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


if __name__ == '__main__':
    main()
