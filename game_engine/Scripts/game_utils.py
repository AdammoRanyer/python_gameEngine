import pygame as pg
import sys
from game_config import d_gameConfig as c
import os

def exitGame_event(event):
    """
    Encerra o jogo.
    
    Parâmetros:
        event (pygame.event.Event) - evento do pygame
    
    Return:
        exit(0)
    """

    if event.type == pg.QUIT:
        pg.quit()
        sys.exit(0)

def checkInput_event(event, key, type=True):
    """
    Checa se um input do tipo pygame event é verdadeiro.
    
    Parâmetros:
        event (pygame.event.Event) - evento do pygame
        key (int) - número da tecla (formato ASCII)
        type (bool) - True = tecla foi precissonada, False = tecla foi despressionada
    
    Return:
        bool
    """
    
    input = False  
    if type == True and event.type == pg.KEYDOWN:
        if event.key == key:
            input = True
    elif type == False and event.type == pg.KEYUP:
        if event.key == key:
            input = True
       
    return input
    
def checkInput(key, type=True):
    """
    Checa se um input é verdadeiro.
    
    Parâmetros:
        key (int) - número da tecla (formato ASCII)
        type (bool) - True = tecla está precissonada, False = tecla não está pressionada
    
    Return:
        bool
    """
    
    input = False
    k = pg.key.get_pressed()
    if type == True and k[key]:
        input = True
    elif type == False and k[key] == False:
        input = True
        
    return input

def set_resolution(window, order):
    """
    Atualiza janela.
    
    Parâmetros:
        window (pygame.surface.Surface) - janela do pygame
        order (str) - ordem de atualização
    
    Return:
        janela atualizada
    """
    
    if order == "x1":
        x = (c["window_size"][0] * 1, c["window_size"][1] * 1)
    elif order == "x2":
        x = (c["window_size"][0] * 2, c["window_size"][1] * 2)
    
    window = pg.display.set_mode(x)
    
def set_windowPosition():
    """
    """

    #pg.display.quit()
    #os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (100, 100)
    #pg.display.set_caption(c["game_name"])
    #window = pg.display.set_mode(c["window_size"])
