import pygame, sys
from settings import *
from core.player import Player
from core.level import Level
from core.camera import Camera
from ui import UI # Import the UI class

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()

        self.game_state = 'GAME_RUNNING' # Initial game state
        self.setup_game()

        # UI elements
        self.ui = UI(self.screen)

    def setup_game(self):
        # Load level data
        with open('platformer/assets/levels/level1.txt', 'r') as f:
            level_layout = [line.strip() for line in f.readlines()]

        self.level = Level(level_layout)
        self.player = Player(self.level.player_start)
        self.player_group = pygame.sprite.GroupSingle(self.player)

        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, self.level.level_width, self.level.level_height)

    def reset_game(self):
        self.game_state = 'GAME_RUNNING'
        self.setup_game()

    def check_game_over(self):
        if self.player.rect.top > self.level.level_height + 200: # Fall detection threshold increased
            self.player.lives -= 1
            if self.player.lives > 0:
                self.player.rect.topleft = self.player.last_safe_pos # Respawn at last safe position
                self.player.direction.y = 0 # Reset vertical movement
            else:
                self.game_state = 'GAME_OVER'

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.game_state == 'GAME_OVER':
                        if event.key == pygame.K_r: # Press R to restart
                            self.reset_game()
                        elif event.key == pygame.K_q: # Press Q to quit
                            pygame.quit()
                            sys.exit()

            if self.game_state == 'GAME_RUNNING':
                self.screen.fill((0, 0, 0)) # Black background

                self.player_group.update(self.level.platforms, self.level.player_start[0]) # Pass level_start_x
                self.level.enemies.update(self.level.platforms) # Pass platforms to enemy update

                # Player-enemy collision
                if not self.player.invincible and pygame.sprite.spritecollideany(self.player, self.level.enemies):
                    self.player.lives -= 1
                    self.player.activate_invincibility()
                    if self.player.lives <= 0:
                        self.game_state = 'GAME_OVER'

                self.camera.update(self.player)

                self.level.run(self.camera)
                self.screen.blit(self.player.image, self.camera.apply(self.player))

                self.ui.display_lives(self.player.lives) # Use the UI class to display lives
                self.check_game_over()

            elif self.game_state == 'GAME_OVER':
                self.screen.fill((0, 0, 0)) # Black background
                self.ui.display_game_over() # Display game over message

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()