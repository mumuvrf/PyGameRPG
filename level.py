import pygame

class Level:
    def __init__(self):

        # Obter a janela de qualquer lugar
        self.display_surface = pygame.display.get_surface()

        # Criando o grupo de todas as sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        # Atualizar e desenhar o jogo
        pass