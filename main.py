import pygame as pg
from game.game import Game
from game.settings import FPS, DISPLAY_MODE

pg.init()


def main():
    running = True
    playing = True

    pg.init()
    resolution, flag = DISPLAY_MODE
    screen = pg.display.set_mode(resolution, flag)
    clock = pg.time.Clock()
    fps = FPS

    # Implementing Menus

    # Implementing Game
    game = Game(screen, clock, fps)

    while running:
        # Start Menu Here ...

        while playing:
            # Game Logic Here ...
            game.run()


if __name__ == '__main__':
    main()
