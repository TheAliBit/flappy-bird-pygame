import pygame as pg

from assets.colors import white


class Boundary:
    def __init__(self, screen):
        self.screen = screen
        self.color = white
        self.top = pg.Rect(0, 0, screen.get_width(), 10)
        self.bottom = pg.Rect(0, screen.get_height() - 10, screen.get_width(), 10)

    def run(self):
        self.draw()

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.top)
        pg.draw.rect(self.screen, self.color, self.bottom)
