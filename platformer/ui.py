import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.font = pygame.font.Font(None, 30)
        self.game_over_font = pygame.font.Font(None, 60)

    def display_lives(self, lives):
        lives_text = self.font.render(f'Lives: {lives}', True, (255, 255, 255))
        self.display_surface.blit(lives_text, (10, 10))

    def display_game_over(self):
        game_over_text = self.game_over_font.render('GAME OVER', True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        self.display_surface.blit(game_over_text, game_over_rect)

        restart_text = self.font.render('Press R to Restart', True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        self.display_surface.blit(restart_text, restart_rect)

        quit_text = self.font.render('Press Q to Quit', True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.display_surface.blit(quit_text, quit_rect)
