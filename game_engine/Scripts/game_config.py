import pygame as pg
import os
import screeninfo

d_gameConfig = {
        "game_name": "Galactic Racer",
        "window_originalSize": (256, 240),
        "window_resolution": 2,
        "monitor_size": (screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height),
        "window_position": (0, 0),
        "FPS": 60,
        "dir_assets": os.getcwd()[:-8] + r"\Assets",
        "background_color": (0, 0, 50),
        "scene": "stage 1",
        "key_1": pg.K_1,
        "key_2": pg.K_2,
        "key_3": pg.K_3,
        "key_4": pg.K_4,
        "key_5": pg.K_5,
        "key_rightArrow": pg.K_RIGHT,
        "key_leftArrow": pg.K_LEFT,
        "key_upArrow": pg.K_UP,
        "key_downArrow": pg.K_DOWN,
        "key_r": pg.K_r,
        "key_t": pg.K_t,
    }
