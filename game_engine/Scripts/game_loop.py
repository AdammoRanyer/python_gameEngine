import pygame as pg
from game_config import d_gameConfig as c
import utils as u
import game_utils as gu
import time
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
    spriteGroup = pg.sprite.LayeredUpdates()
    def load_sprites(spriteSheet, order):
        """
        Carrega sprites de um objeto.
        
        Parâmetros:
            spriteSheet (pygame.surface.Surface) - folha de sprites
            order (str) - regra de negócio
        
        Return:
            Dicionário com todas as sprites/animações
        """
        
        if order == "p1":
            d_animations = {
                "idle_0": [d_sprites["spriteSheet_0"].subsurface(0, 0, 16, 16)],
                "idle_1": [d_sprites["spriteSheet_0"].subsurface(16, 0, 16, 16)],
            }
        elif order == "bg_0":
            bg = pg.Surface((256, 240))
            bg.fill((255, 255, 255))
            for row in range(int(bg.get_size()[1]/16)): 
                for i in range(int(bg.get_size()[0]/16)): 
                    if i == 0:
                        bg.blit(d_sprites["spriteSheet_0"].subsurface(0, 16, 16, 16), (i * 16, row * 16))
                    elif i == 15:
                        bg.blit(gu.flipSurface(d_sprites["spriteSheet_0"].subsurface(0, 16, 16, 16)), (i * 16, row * 16))
                    else:
                        bg.blit(d_sprites["spriteSheet_0"].subsurface(16, 16, 16, 16), (i * 16, row * 16))
            
            d_animations = {
                "bg_0": [bg]
            }
        
        return d_animations
    
    if scene == "stage 1":
        d_sprites = {
            "spriteSheet_0": pg.image.load(os.path.join(c["dir_assets"], "spriteSheet_0.png")).convert()
        }
        d_animations = load_sprites(d_sprites["spriteSheet_0"], "p1")
        gu.createObject(d_objects, gu.SpriteObject(name="p1", position=[120, 112], image=d_animations["idle_1"][0], animations=d_animations), spriteGroup)
        d_animations = load_sprites(d_sprites["spriteSheet_0"], "bg_0")
        gu.createObject(d_objects, gu.SpriteObject(name="bg_0", position=[0, 0], image=d_animations["bg_0"][0], zOrder=-1), spriteGroup)
        gu.createObject(d_objects, gu.SpriteObject(name="bg_1", position=[0, -240], image=d_animations["bg_0"][0], zOrder=-2), spriteGroup)
        
    return d_objects, spriteGroup

def play_scene(canRender, d_objects, spriteGroup, scene):
    """
    Toca a cena.
    
    Parâmetros:
        canRender (bool) - 
        d_objects (dict) - objetos que compõem a cena
        spriteGroup (pygame.sprite.LayeredUpdates) - grupo de sprites
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

        if canRender:
            d_objects["bg_0"].rect.y+=2
            if d_objects["bg_0"].rect.y >= 240:
                d_objects["bg_0"].rect.y = 0
            d_objects["bg_1"].rect.y = d_objects["bg_0"].rect.y-240            
            
            if(gu.checkInput(c["key_rightArrow"])): d_objects["p1"].rect.x+=2
            if(gu.checkInput(c["key_leftArrow"])): d_objects["p1"].rect.x-=2
            if(gu.checkInput(c["key_upArrow"])): d_objects["p1"].rect.y-=2
            if(gu.checkInput(c["key_downArrow"])): d_objects["p1"].rect.y+=2
            
            gu.drawInScreen(window, spriteGroup)

window = gu.start_game()
#clock = pg.time.Clock()
frame = 1 / c["FPS"]
canRender = True
unprocessed = 0
time_1 = time.perf_counter()
debugText_0 = gu.Text(name="debugText_0")
#debugText_0.switch_visible()
d_objects, spriteGroup = load_scene(c["scene"])

while 1:
    canRender = False
    time_2 = time.perf_counter()
    unprocessed += time_2 - time_1
    time_1 = time_2
    while unprocessed >= frame:
        unprocessed -= frame
        canRender = True

    scene = play_scene(canRender, d_objects, spriteGroup, c["scene"])
    if scene != None and scene[0] == "restart scene": 
        d_objects, spriteGroup = load_scene(scene[1])   
    
    if canRender == True:
        text_debug = \
            "qtd_objs: " + str(len(d_objects)) + "\n" \
            + gu.objects_position(d_objects)
        debugText_0.text = text_debug        
        debugText_0.draw(window)
        pg.display.update()
    
    #clock.tick(c["FPS"])