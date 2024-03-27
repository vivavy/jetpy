# it needed for linter. you can skip this line
# ATTENTION: you MUST leave end of line after `jet` in this line
#         ~~
#         |
#         \
#         V
import jet

import pygame as pg

pg.init()

def create_window(size, title):
    screen = pg.display.set_mode(size)
    pg.display.set_caption(title)
    return screen

def close_window(screen):
    pg.display.flip()
    pg.quit()

def fill_screen(screen, color):
    screen.fill(color)

def draw_rect(screen, color, rect):
    pg.draw.rect(screen, color, rect)

def update_window(screen):
    pg.display.flip()
