import pygame as pg
import sys
from assets.colors import *
from .bird import Bird


class Game:
    def __init__(self, screen, clock, fps):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.clock = clock
        self.fps = fps
        self.bird = Bird(self.screen)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.fps)
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.key == pg.K_SPACE:
                    self.bird.jump()

    def update(self):
        self.bird.fall()

    def draw(self):
        self.screen.fill(black)
        self.bird.draw()
        pg.display.flip()
