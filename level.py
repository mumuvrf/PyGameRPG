import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # Obter a janela de qualquer lugar
        self.display_surface = pygame.display.get_surface() # Pega a tela principal 

        # Criando o grupo de todas as sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # Setup da sprite
        self.create_map()
    
    def create_map(self):
        # Criar o mapa
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y =  row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites])


    def run(self):
        # Atualizar e desenhar o jogo
        self.visible_sprites.draw(self.display_surface)