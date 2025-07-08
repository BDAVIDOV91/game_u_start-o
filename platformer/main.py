# main.py

import pygame
import sys
from settings import *
from core.player import Player
from core.platform import Platform
from core.camera import Camera
from core.enemy import Enemy
from ui import UI
from core.level import Level
from save_manager import SaveManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "menu"
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player(self, 100, 100)
        self.all_sprites.add(self.player)
        self.level = Level("/home/technojihad/game_u_start-o/platformer/assets/levels/level1.txt")
        self.level.add_sprites(self.all_sprites)
        for p in self.level.platforms:
            self.platforms.add(p)
        e1 = Enemy(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80, TILE_SIZE, TILE_SIZE)
        self.all_sprites.add(e1)
        self.enemies.add(e1)
        self.camera = Camera(len(self.level.platforms) * TILE_SIZE, SCREEN_HEIGHT)
        self.ui = UI()
        self.score = 0
        self.save_manager = SaveManager("save.json")


    def run(self):
        while self.running:
            self.clock.tick(FPS)
            if self.game_state == "menu":
                self.menu_events()
                self.menu_draw()
            elif self.game_state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.game_state == "game_over":
                self.game_over_events()
                self.game_over_draw()

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_state = "playing"

    def menu_draw(self):
        self.screen.fill(BLACK)
        self.ui.draw_text(self.screen, "Press SPACE to start", SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2)
        pygame.display.flip()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()
                if event.key == pygame.K_s:
                    self.save_game()
                if event.key == pygame.K_l:
                    self.load_game()

    def playing_update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        # Check for collisions between player and platforms
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if self.player.vel.y > 0 and hits:
            self.player.rect.bottom = hits[0].rect.top
            self.player.vel.y = 0

        # Check for collisions between player and enemies
        enemy_hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if enemy_hits:
            self.game_state = "game_over"
        self.score += 1

    def playing_draw(self):
        self.screen.fill(BLACK)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.ui.draw_text(self.screen, f"Score: {self.score}", 10, 10)
        pygame.display.flip()

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.__init__() # cheap restart

    def game_over_draw(self):
        self.screen.fill(BLACK)
        self.ui.draw_text(self.screen, "Game Over", SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2)
        self.ui.draw_text(self.screen, "Press R to restart", SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 50)
        pygame.display.flip()

    def save_game(self):
        data = {
            "player_pos": (self.player.rect.x, self.player.rect.y),
            "score": self.score
        }
        self.save_manager.save_game(data)

    def load_game(self):
        data = self.save_manager.load_game()
        if data:
            self.player.rect.x = data["player_pos"][0]
            self.player.rect.y = data["player_pos"][1]
            self.score = data["score"]

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
