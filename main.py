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

        self.state = INIT

        self.font = pygame.font.SysFont(None, 120)
        self.text1 = self.font.render('WELCOME, VILLAGE WARRIOR', True, (255, 165, 0))
        self.text3 = self.font.render('GAME OVER!', True, (255, 0, 0))
        self.font2 = pygame.font.SysFont(None, 60)
        self.text2 = self.font2.render('Press ENTER to start', True, (255, 255, 255))
        self.text4 = self.font2.render('Pressione qualquer tecla para sair.', True, (255, 255, 255))
    
    def init_screen(self):
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

            self.screen.blit(self.window, self.screen_rect)
            self.screen.blit(self.text1, self.text1.get_rect(center=(WIDTH/2, HEIGHT/2.3)))
            self.screen.blit(self.text2, self.text2.get_rect(center=(WIDTH/2, HEIGHT/1.2)))
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

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text3, self.text3.get_rect(center=(WIDTH/2, HEIGHT/2.3)))
            self.screen.blit(self.text4, self.text4.get_rect(center=(WIDTH/2, HEIGHT/1.2)))
            pygame.display.update()

    def run(self):
        while self.state != QUIT:
            if self.state == INIT:
                self.state = self.init_screen()
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
