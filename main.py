# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import sys
from settings import *
from level import Level


class Game():
    def __init__(self):
        # inicia pygame e cria janela, ou seja, gera tela principal
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('NOSSO JOGO')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        # ===== Loop principal =====
        while True:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
                    sys.exit()  # Função do Python que finaliza o programa
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

                # ----- Gera saídas
            self.screen.fill((255, 255, 255))  # Preenche com a cor branca
            self.level.run()
            # ----- Atualiza estado do jogo
            pygame.display.update()  # Mostra o novo frame para o jogador
            # ----- Limita a 60 frames por segundo
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
