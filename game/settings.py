import pygame as pg


def display_mode(resolution):
    if resolution == 'FULLSCREEN':
        return (0, 0), pg.FULLSCREEN
    else:
        width, height = resolution
        return (width, height), 0


DISPLAY_MODE = display_mode(resolution="FULLSCREEN")
FPS = 60
GAME_GRAVITY = 0.5
BIRD_VELOCITY = 0
BIRD_JUMP = -10
