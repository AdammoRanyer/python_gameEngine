import pygame as pg
from game_config import d_gameConfig as c
import utils as u

pg.init()
pg.display.set_caption(c["game_name"])
window = pg.display.set_mode(c["window_size"])

while 1:
    window
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit(0)