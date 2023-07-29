import pygame as pg
import os
from game_config import d_gameConfig as c
import sys

def start_game():
    """
    Inicia pygame e suas configurações.
    
    Parâmetros:
        Nenhum
    
    Return:
        window e clock
    """
    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pg.init()
    pg.display.set_caption(c["game_name"])
    window = pg.display.set_mode(c["window_originalSize"])
    set_resolution(window, c["window_resolution"])
    clock = pg.time.Clock()
    
    return window, clock

def exitGame_event(event):
    """
    Encerra o jogo.
    
    Parâmetros:
        event (pygame.event.Event) - evento do pygame
    
    Return:
        exit(0)
    """

    if event.type == pg.QUIT:
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

def set_resolution(window, resolution):
    """
    Atualiza janela.
    
    Parâmetros:
        window (pygame.surface.Surface) - janela do pygame
        resolution (int) - escala da resolução
    
    Return:
        Janela atualizada
    """
    
    c["window_resolution"] = resolution
    if c["window_resolution"] == 0:
        c["window_resolution"] = float(c["monitor_size"][1] / c["window_originalSize"][1])
        x = (c["window_originalSize"][0] * c["window_resolution"], c["window_originalSize"][1] * c["window_resolution"])
        c["window_position"] = ((c["monitor_size"][0] - (c["window_originalSize"][0] * c["window_resolution"])) / 2, 0)
        
        window = pg.display.set_mode(x, pg.FULLSCREEN)
    else:
        x = (c["window_originalSize"][0] * c["window_resolution"], c["window_originalSize"][1] * c["window_resolution"])
        c["window_position"] = (0, 0)
        
        window = pg.display.set_mode(x)

def createObject(d_objects, object):
    """
    Cria objetos.
    
    Parâmetros:
        d_objects (dict) - dicionário de objetos
        object (classe de objetos) - objeto criado
    
    Return:
        d_objects atualizado
    """
    
    d_objects[object.name] = object

def render(window, d_objects):
    """
    Renderiza objetos na tela com ordem definida.
    
    Parâmetros:
        window (pygame.surface.Surface) - janela do pygame
        d_objects (dict) - dicionário de objetos
    
    Return:
        Objetos renderizados na janela
    """

    surface=pg.Surface(c["window_originalSize"])
    surface.fill(c["background_color"])
    for i in sorted(d_objects, key=lambda x: d_objects[x].zOrder):
        d_objects[i].render(surface)
    if c["window_resolution"] > c["monitor_size"][0] - (c["window_originalSize"][0] * c["window_resolution"]):
        window.blit(pg.transform.scale(surface, (c["window_originalSize"][0] * c["window_resolution"], c["window_originalSize"][1] * c["window_resolution"])), c["window_position"])
    else:
        window.blit(pg.transform.scale(surface, (c["window_originalSize"][0] * c["window_resolution"], c["window_originalSize"][1] * c["window_resolution"])), c["window_position"])
 
class Text:
    """
    Classe para criação de objetos do tipo Text.
    """
    def __init__(self, name, font="Comic Sans", size=16, color=[255, 255, 255], text="Olá mundo!", position=[0, 0], zOrder=0, visible=True):
        """
        Constrói objeto Text.
        
        Parâmetros:
            self (game_utils.Text) - objeto da classe Text
            name (str) - nome do objeto
            font (str) - nome da fonte
            size (int) - tamanho da fonte
            color (list) - cor da fonte
            text (str) - texto
            position (list) - posição do Text
            zOrder (int) - ordenação na janela
            visible (bool) - visibilidade do objeto
        
        Return:
            Objeto
        """
        
        self.name = name
        self.font = pg.font.SysFont(font, size)
        self.size = size
        self.color = color
        self.text = text
        self.position = position
        self.zOrder = zOrder
        self.visible = visible
    
    def render(self, window):
        """
        Renderiza objetos do tipo Text.
        
        Parâmetros:
            self (game_utils.Text) - objeto da classe Text
            window (pygame.surface.Surface) - janela do pygame
        
        Return:
            Objeto renderizado na janela
        """
        
        if self.visible == True:
            lines = self.text.split("\n")
            for i in range(len(lines)):
                position = (self.position[0], self.size * i)
                window.blit(self.font.render(lines[i], True, self.color), position)
 
    def switch_visible(self):
        """
        Ativa/desativa visibilidade do objeto.
        
        Parâmetros:
            self (game_utils.Text) - objeto da classe Text
        
        Return:
            Visibilidade do objeto
        """
        
        if self.visible == True:
            self.visible = False
        else:
            self.visible = True

class SpriteObject:
    """
    Classe para criação de objetos do tipo SpriteObject.
    """
    def __init__(self, name, surface=pg.Surface((16, 16)), position=[0, 0], size=[16, 16], color=[255, 0, 0], zOrder=0, visible=True):
        """
        Constrói objeto SpriteObject.
        
        Parâmetros:
            self (game_utils.Text) - objeto da classe Text
            name (str) - nome do objeto
            surface (pygame.surface.Surface) - objeto pygame para representar imagens
            position (list) - posição do SpriteObject
            size (list) - tamanho do SpriteObject
            color (list) - cor do SpriteObject
            zOrder (int) - ordenação na janela
            visible (bool) - visibilidade do objeto
        
        Return:
            Objeto     
        """    
        
        self.name = name
        self.position = position
        self.size = size
        self.color = color
        self.zOrder = zOrder
        self.visible = visible
        self.sprite = surface
        #self.sprite.fill(self.color)
        self.sprite.set_colorkey((253, 77, 211))
    
    def render(self, window):
        """
        Renderiza objetos do tipo SpriteObject.
        
        Parâmetros:
            self (game_utils.SpriteObject) - objeto da classe SpriteObject
            window (pygame.surface.Surface) - janela do pygame
        
        Return:
            Objeto renderizado na janela
        """
        
        if self.visible == True:
            #pg.draw.rect(window, self.color, pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1]))
            window.blit(self.sprite, self.position)