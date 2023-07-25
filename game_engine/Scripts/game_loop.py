import pygame as pg
from game_config import d_gameConfig as c
import utils as u
import game_utils as gu

pg.init()
pg.display.set_caption(c["game_name"])
window = pg.display.set_mode(c["window_size"])

while 1:
    window
    
    for event in pg.event.get():
        gu.exitGame_event(event)
        if(gu.checkInput_event(event, c["key_1"])): gu.set_resolution(window, "x1")
        if(gu.checkInput_event(event, c["key_2"])): gu.set_resolution(window, "x2")
        if(gu.checkInput_event(event, c["key_3"])): gu.set_windowPosition()

    window.fill((0, 0, 0))
    pg.draw.rect(window, (255, 0, 0), (0, 0, 100, 100))
    pg.display.update()