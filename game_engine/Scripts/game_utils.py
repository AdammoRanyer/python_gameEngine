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
        window
    """
    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pg.init()
    pg.display.set_caption(c["game_name"])
    window = pg.display.set_mode(c["window_originalSize"])
    set_resolution(window, c["window_resolution"])
    
    return window

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

def createObject(d_objects, object, spriteGroup=None):
    """
    Cria objetos.
    
    Parâmetros:
        d_objects (dict) - dicionário de objetos
        object (classe de objetos) - objeto criado
        spriteGroup (pygame.sprite.LayeredUpdates) - grupo de sprites
    
    Return:
        d_objects atualizado
    """
    
    d_objects[object.name] = object
    if spriteGroup != None: spriteGroup.add(object, layer=object.zOrder)

def drawInScreen(window, spriteGroup):
    """
    Renderiza objetos na tela.
    
    Parâmetros:
        window (pygame.surface.Surface) - janela do pygame
        spriteGroup (pygame.sprite.LayeredUpdates) - grupo de sprites
    
    Return:
        Objetos renderizados na janela    
    """
    
    surface=pg.Surface(c["window_originalSize"])
    surface.fill(c["background_color"])
    spriteGroup.draw(surface)
    if c["window_resolution"] > c["monitor_size"][0] - (c["window_originalSize"][0] * c["window_resolution"]):
        window.blit(pg.transform.scale(surface, (c["window_originalSize"][0] * c["window_resolution"], c["window_originalSize"][1] * c["window_resolution"])), c["window_position"])
    else:
        window.blit(pg.transform.scale(surface, (c["window_originalSize"][0] * c["window_resolution"], c["window_originalSize"][1] * c["window_resolution"])), c["window_position"])

def objects_name(d_objects):
    """
    Varre e captura nome da cada objeto.
    
    Parâmetros:
        d_objects (dict) - dicionário de objetos
    
    Return:
        Lista com nome dos objetos
    """
    
    l_names = []
    for i in d_objects: l_names.append(d_objects[i].name)
    
    return l_names

def objects_position(d_objects):
    """
    Varre e captura nome e posição da cada objeto.
    
    Parâmetros:
        d_objects (dict) - dicionário de objetos
    
    Return:
        String com informações 
    """
    
    positions = ""
    counter = 0
    for i in d_objects: 
        counter += 1
        if counter == len(d_objects):
            positions += d_objects[i].name + ": [" + str(d_objects[i].rect.x) + ", " + str(d_objects[i].rect.y) + "]"
        else:
            positions += d_objects[i].name + ": [" + str(d_objects[i].rect.x) + ", " + str(d_objects[i].rect.y) + "]\n"
    
    return positions

def flipSurface(surface, x=True, y=False):
    """
    Inverte uma superfície do pygame.
    
    Parâmetros:
        surface (pygame.surface.Surface) - imagem
        x (bool) - eixo x
        y (bool) - eixo y
    
    Return:
        Imagem invertida
    """
    
    surface = pg.transform.flip(surface, x, y)
    
    return surface
 
class Text:
    """
    Classe para criação de objetos do tipo Text.
    """
    def __init__(self, name, font="Comic Sans", size=16, color=[255, 255, 255], text="Olá mundo!", position=[0, 0], visible=True, zOrder=0):
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
            visible (bool) - visibilidade do objeto
            zOrder (int) - ordenação na janela
        
        Return:
            Objeto
        """
        
        self.name = name
        self.font = pg.font.SysFont(font, size)
        self.size = size
        self.color = color
        self.text = text
        self.position = position
        self.visible = visible
        self.zOrder = zOrder
    
    def draw(self, window):
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
                position = (self.position[0], (self.size + 4) * i)
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

class SpriteObject(pg.sprite.Sprite):
    """
    Classe para criação de objetos do tipo SpriteObject.
    """
    def __init__(self, name, position=[0, 0], image=pg.Surface((16, 16)), animations={}, visible=True, zOrder=0):
        """
        Constrói objeto SpriteObject.
        
        Parâmetros:
            self (game_utils.Text) - objeto da classe Text
            name (str) - nome do objeto
            rect (pygame.rect.Rect) - objeto pygame para armazenar coordenadas retangulares
            image (pygame.surface.Surface) - objeto pygame para representar imagens
            animations (dict) - dicionário com todas as sprites/animações
            visible (bool) - visibilidade do objeto
            zOrder (int) - ordenação na janela
        
        Return:
            Objeto     
        """    
        
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.rect = pg.Rect((position[0], position[1], 0, 0))
        self.image = image
        self.image.set_colorkey(c["sprites_colorKey"])
        self.animations = animations
        self.visible = visible
        self.zOrder = zOrder
    
    def draw(self, window):
        """
        Renderiza objetos do tipo SpriteObject.
        
        Parâmetros:
            self (game_utils.SpriteObject) - objeto da classe SpriteObject
            window (pygame.surface.Surface) - janela do pygame
        
        Return:
            Objeto renderizado na janela
        """
        
        if self.visible == True:
            window.blit(self.image, self.position)