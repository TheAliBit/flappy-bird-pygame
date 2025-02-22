from game.settings import *
import os


class Bird:
    def __init__(self, screen):
        self.screen = screen
        self.x = screen.get_width() // 2 - 200
        self.y = screen.get_height() // 2 - 200
        self.velocity = BIRD_VELOCITY
        self.jump_force = BIRD_JUMP
        self.gravity = GAME_GRAVITY

        img_path = os.path.join(os.path.dirname(__file__), '../assets/images/bird.png')
        img = pg.image.load(img_path)
        self.img = pg.transform.scale(img, (50, 50))
        self.bird_rect = img.get_rect(midbottom=(self.x, self.y))

    def run(self):
        self.draw()
        self.fall()
        self.jump()

    def fall(self):
        self.velocity += self.gravity
        self.bird_rect.y += self.velocity

    def jump(self):
        self.velocity = self.jump_force

    def draw(self):
        self.screen.blit(self.img, self.bird_rect)
