import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        if self.direction.magnitude() > 1:
            self.direction.x = 0
            self.direction.y = 0

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # se movendo para a direita
                        # a extrema direita do nosso Player coincide com a extrema esquerda do obstáculo que se está colidindo
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # se movendo para a esquerda
                        # a extrema esquerda do nosso Player coincide com a extrema direita do obstáculo que se está colidindo
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # se movendo para baixo
                        # a extrema inferior do nosso Player coincide com a extrema superior do obstáculo que se está colidindo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # se movendo para cima
                        # a extrema superior do nosso Player coincide com a extrema inferior do obstáculo que se está colidindo
                        self.hitbox.top = sprite.hitbox.bottom