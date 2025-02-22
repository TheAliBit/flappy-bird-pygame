import sys

import pygame as pg

from assets.colors import white


class Menu:
    def __init__(self, screen, state):
        self.screen = screen
        self.state = state
        self.screen_width, self.screen_height = screen.get_size()
        self.font = pg.font.Font(None, 32)
        self.running = True
        self.text = None
        self.text_rect = None

    def run(self):
        while self.state["running"] and not self.state["playing"]:
            self.start_menu()
            self.event()
            self.draw()

    def start_menu(self):
        self.text = self.font.render("Press SPACE to Start", True, white)
        self.text_rect = self.text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))

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
                    self.state['playing'] = True

    def draw(self):
        pg.display.flip()
        self.screen.blit(self.text, self.text_rect)
