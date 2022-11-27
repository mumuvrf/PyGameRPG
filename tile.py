import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, grupo):
        super().__init__(grupo)
        self.image = pygame.image.load('assets/obstacle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
