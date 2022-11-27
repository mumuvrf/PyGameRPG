import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # Obter a janela de qualquer lugar
        self.display_surface = pygame.display.get_surface() # Pega a tela principal 

        # Criando o grupo de todas as sprites
        self.visible_sprites = YSortCameraGroup()
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
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)


    def run(self):
        # Atualizar e desenhar o jogo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

    
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # Configuração geral
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # Conseguindo o deslocamento (offset) para a câmera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Desenhar sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - (self.offset)
            self.display_surface.blit(sprite.image, offset_position)
