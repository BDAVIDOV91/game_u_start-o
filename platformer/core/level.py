import pygame
from .platform import Platform
from .enemy import Enemy

class Level:
    def __init__(self, level_data):
        self.display_surface = pygame.display.get_surface()
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group() # New group for enemies
        self.player_start = None
        tile_size = 32 # Assuming 32x32 tiles for now

        self.level_width = len(layout[0]) * tile_size
        self.level_height = len(layout) * tile_size

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    platform = Platform((x, y), (tile_size, tile_size))
                    self.platforms.add(platform)
                elif cell == 'P': # New: Spawn enemy
                    self.player_start = (x, y - tile_size) # Adjust player start y to be on top of platform

                elif cell == 'E': # New: Spawn enemy
                    enemy = Enemy((x, y), 2) # Speed of 2 for now
                    self.enemies.add(enemy)

    def run(self, camera):
        for platform in self.platforms:
            self.display_surface.blit(platform.image, camera.apply(platform))

        for enemy in self.enemies:
            self.display_surface.blit(enemy.image, camera.apply(enemy))
