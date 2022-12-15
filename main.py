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

        # variável de controle para os loop's
        self.loop = True

        # janelas
        self.window_init = pygame.image.load('assets/tela_inicial_presskey.png').convert_alpha()
        self.window_end = pygame.image.load('assets/game_over_presskey.png').convert_alpha()
        self.window_manual = pygame.image.load('assets/como_jogar.png').convert_alpha()

        # estado inicial
        self.state = INIT1
    
    def init_screen(self):
        while self.loop:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = INIT2
                        self.loop = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.state = QUIT

            self.screen.blit(self.window_init, self.screen_rect)
            pygame.display.update()
        self.loop = True
        return self.state

    def manual_screen(self):
        while self.loop:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = GAME
                        self.loop = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.state = QUIT

            self.screen.blit(self.window_manual, self.screen_rect)
            pygame.display.update()
        self.loop = True
        return self.state

    def end_screen(self):
        while self.loop:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.KEYDOWN:
                    self.loop = False
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.blit(self.window_end, self.screen_rect)
            pygame.display.update()

    def run(self):
        while self.state != QUIT:
            if self.state == INIT1:
                self.state = self.init_screen()
            elif self.state == INIT2:
                self.state = self.manual_screen()
            elif self.state == GAME:
                self.state = self.gaming()
        self.end_screen()

    def gaming(self):
        # ===== Loop principal =====
        while self.loop:
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
            if self.level.check_death_player():
                self.state = QUIT
                self.loop = False
        self.loop = True
        return self.state


if __name__ == '__main__':
    game = Game()
    game.run()
