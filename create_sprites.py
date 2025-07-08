import pygame

# Create a surface for the idle sprite
idle_surface = pygame.Surface((40, 40))
idle_surface.fill((0, 255, 0))  # Green
pygame.image.save(idle_surface, "/home/technojihad/game_u_start-o/platformer/assets/images/player/idle.png")

# Create a surface for the first walking sprite
walk1_surface = pygame.Surface((40, 40))
walk1_surface.fill((0, 200, 50))  # A slightly different green
pygame.image.save(walk1_surface, "/home/technojihad/game_u_start-o/platformer/assets/images/player/walk1.png")

# Create a surface for the second walking sprite
walk2_surface = pygame.Surface((40, 40))
walk2_surface.fill((0, 150, 100))  # Another shade of green
pygame.image.save(walk2_surface, "/home/technojihad/game_u_start-o/platformer/assets/images/player/walk2.png")
