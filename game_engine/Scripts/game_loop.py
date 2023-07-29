import pygame as pg
from game_config import d_gameConfig as c
import utils as u
import game_utils as gu
import os

def load_scene(scene=c["scene"]):
    """
    Carrega objetos da cena.
    
    Parâmetros:
        scene (str) - nome da cena
    
    Return:
        Objetos da cena criados
    """
    
    d_objects = {}
    
    if scene == "stage 1":
        d_sprites = {
            "spriteSheet_0": pg.image.load(os.path.join(c["dir_assets"], "spriteSheet_0.png")).convert()
        }
        gu.createObject(d_objects, gu.SpriteObject(name="obj_p1", position=[100, 100], surface=d_sprites["spriteSheet_0"]))
        
    return d_objects

def play_scene(d_objects, scene):
    """
    Toca a cena.
    
    Parâmetros:
        d_objects (dict) - objetos que compõem a cena
        scene (str) - nome da cena
    
    Return:
        Retorna o desfecho da cena
    """
    
    if scene == "stage 1":
        for event in pg.event.get():
            gu.exitGame_event(event)
            if(gu.checkInput_event(event, c["key_1"])): 
                if c["window_resolution"] != 1:
                    gu.set_resolution(window, 1)
                    debugText_0.position[0] = c["window_position"][0]
            elif(gu.checkInput_event(event, c["key_2"])): 
                if c["window_resolution"] != 2:
                    gu.set_resolution(window, 2)
                    debugText_0.position[0] = c["window_position"][0]
            elif(gu.checkInput_event(event, c["key_3"])): 
                if c["window_resolution"] != 3:
                    gu.set_resolution(window, 3)
                    debugText_0.position[0] = c["window_position"][0]
            elif(gu.checkInput_event(event, c["key_4"])): 
                if c["window_resolution"] != 4:
                    gu.set_resolution(window, 4)
                    debugText_0.position[0] = c["window_position"][0]                    
            elif(gu.checkInput_event(event, c["key_5"])): 
                if c["window_resolution"] != 0:
                    gu.set_resolution(window, 0)
                    debugText_0.position[0] = c["window_position"][0]
            if(gu.checkInput_event(event, c["key_r"])): return ("restart scene", scene)
            if(gu.checkInput_event(event, c["key_t"])): debugText_0.switch_visible()
        
        if(gu.checkInput(c["key_rightArrow"])): d_objects["obj_p1"].position[0]+=2
        if(gu.checkInput(c["key_leftArrow"])): d_objects["obj_p1"].position[0]-=2
        if(gu.checkInput(c["key_upArrow"])): d_objects["obj_p1"].position[1]-=2
        if(gu.checkInput(c["key_downArrow"])): d_objects["obj_p1"].position[1]+=2
    
        gu.render(window, d_objects)

window, clock = gu.start_game()
debugText_0 = gu.Text(name="debugText_0")
#debugText_0.switch_visible()
d_objects = load_scene(c["scene"])

while 1:
    clock.tick(c["FPS"])
    text_debug = \
        "FPS: " + str(int(clock.get_fps())) + \
        "\nqtd_objs: " + str(len(d_objects) + 1)
    debugText_0.text = text_debug
    scene = play_scene(d_objects, c["scene"])
    debugText_0.render(window)
    pg.display.update()
    
    if scene != None and scene[0] == "restart scene":
        d_objects = load_scene(scene[1])