# it needed for linter. you can skip this line
# ATTENTION: you MUST leave end of line after `jet` in this line
#         ~~
#         |
#         \
#         V
import jet

import pygame as pg

pg.init()

screen = pg.display.set_mode(jet.to_list(jet.config.WindowMain.Size))

pg.display.set_caption(jet.string(jet.config.WindowMain.Title))

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pg.display.flip()

pg.quit()

jet.exit(0)
