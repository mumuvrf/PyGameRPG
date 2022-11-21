import pygame

class Level:
    def __init__(self):

        # Obter a janela de qualquer lugar
        self.display_surface = pygame.display.get_surface() # Pega a tela principal 

        # Criando o grupo de todas as sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
    
    def create_map(self):
        # Criar o mapa
        for row in WORLD_MAP:
            print(row)

    def run(self):
        # Atualizar e desenhar o jogo
        pass