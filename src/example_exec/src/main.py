# it needed for linter. you can skip this line
# ATTENTION: you MUST leave end of line after `jet` in this line
#         ~~
#         |
#         \
#         V
import jet

import pygame as pg

mod = jet.mod.load(jet.path.cwd("example_mod.jet"))

screen = mod.create_window((640, 480), "Example Mod")

run = 1

while run:
    for event in mod.pg.event.get():
        if event.type == mod.pg.QUIT:
            run = 0
    mod.fill_screen(screen, (0, 0, 0))
    mod.draw_rect(screen, (255, 0, 0), (100, 100, 200, 200))
    mod.update_window(screen)

mod.close_window(screen)

jet.exit(0)
