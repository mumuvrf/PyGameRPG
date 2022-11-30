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
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('VILLAGE WARRIOR')
        self.clock = pygame.time.Clock()

        self.level = Level()

        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.play(loops = -1)

        self.loop = True
        self.window = pygame.image.load('assets/penes_de_fundo.png').convert_alpha()
    
    def init_screen(self):
        while self.loop:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        state = GAME
                        self.loop = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    state = QUIT

            self.screen.blit(self.window, self.screen_rect)
            pygame.display.update()
                    
        return state

    def run(self):
        state = INIT
        while state != QUIT:
            if state == INIT:
                state = self.init_screen()
            elif state == GAME:
                state = self.gaming()
            else:
                state = QUIT

    def gaming(self):
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
            self.screen.fill(WATER_COLOR)  # Preenche com a cor branca
            self.level.run()
            # ----- Atualiza estado do jogo
            pygame.display.update()  # Mostra o novo frame para o jogador
            # ----- Limita a 60 frames por segundo
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
