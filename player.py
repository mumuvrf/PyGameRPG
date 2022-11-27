import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, grupo, obstacle_sprites):
        super().__init__(grupo)
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
    def move(self,speed):
        if self.direction.magnitude() > 1:
            self.direction.x = 0
            self.direction.y = 0
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
		# self.rect.center += self.direction * speed

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # se movendo para a direita
                        self.rect.right = sprite.rect.left # a extrema direita do nosso Player coincide com a extrema esquerda do obstáculo que se está colidindo
                    if self.direction.x < 0: # se movendo para a esquerda 
                        self.rect.left = sprite.rect.right #a extrema esquerda do nosso Player coincide com a extrema direita do obstáculo que se está colidindo

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # se movendo para baixo
                        self.rect.bottom = sprite.rect.top # a extrema inferior do nosso Player coincide com a extrema superior do obstáculo que se está colidindo
                    if self.direction.y < 0: # se movendo para cima
                        self.rect.top = sprite.rect.bottom # a extrema superior do nosso Player coincide com a extrema inferior do obstáculo que se está colidindo

    def update(self):
        self.input()
        self.move(self.speed)