import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.on_ground = True # Set to True initially
        self.can_double_jump = True # New attribute for double jump
        self.lives = 3
        self.last_safe_pos = list(pos) # Store last safe position

        # player status
        self.status = 'idle'
        self.facing_right = True

        # invincibility
        self.invincible = False
        self.invincibility_duration = 2000 # 2 seconds in milliseconds
        self.invincibility_timer = 0
        self.blink_timer = 0

    def import_player_assets(self):
        character_path = os.path.join('platformer', 'assets', 'images', 'player')
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

        # Load images directly from the player directory
        self.animations['idle'].append(pygame.image.load(os.path.join(character_path, 'idle.png')).convert_alpha())
        self.animations['run'].append(pygame.image.load(os.path.join(character_path, 'walk1.png')).convert_alpha())
        self.animations['run'].append(pygame.image.load(os.path.join(character_path, 'walk2.png')).convert_alpha())
        # Placeholder for jump and fall animations for now
        self.animations['jump'].append(pygame.image.load(os.path.join(character_path, 'idle.png')).convert_alpha()) # Using idle for now
        self.animations['fall'].append(pygame.image.load(os.path.join(character_path, 'idle.png')).convert_alpha()) # Using idle for now

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        if self.invincible:
            alpha = 255 - (self.blink_timer * 50) % 256 # Blinking effect
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255) # Fully opaque when not invincible

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.on_ground:
                self.jump()
                self.can_double_jump = True
            elif self.can_double_jump:
                self.jump()
                self.can_double_jump = False

    def get_status(self):
        if self.direction.y < 0: # jumping
            self.status = 'jump'
        elif self.direction.y > 1: # falling (a small threshold to avoid flickering)
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def horizontal_movement_collision(self, platforms):
        self.rect.x += self.direction.x * self.speed
        for sprite in platforms.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0: # moving left
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0: # moving right
                    self.rect.right = sprite.rect.left

    def vertical_movement_collision(self, platforms):
        self.apply_gravity()
        for sprite in platforms.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0: # falling
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_ground = True
                    self.last_safe_pos = list(self.rect.topleft) # Update last safe position
                elif self.direction.y < 0: # jumping
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.direction.y != 0: # if not falling or jumping, not on ground
            self.on_ground = False

    def activate_invincibility(self):
        self.invincible = True
        self.invincibility_timer = pygame.time.get_ticks() # Get current time

    def update(self, platforms, level_start_x):
        self.get_input()
        self.get_status()

        # Handle invincibility
        if self.invincible:
            self.blink_timer += 1
            if pygame.time.get_ticks() - self.invincibility_timer >= self.invincibility_duration:
                self.invincible = False
                self.blink_timer = 0

        self.animate()
        self.horizontal_movement_collision(platforms)

        # Invisible wall at the start
        if self.rect.left < level_start_x and self.direction.x < 0:
            self.rect.left = level_start_x
            self.direction.x = 0

        self.vertical_movement_collision(platforms)