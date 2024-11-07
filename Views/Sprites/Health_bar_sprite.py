import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite
from Utils import Sprite_utils
from Utils.Colors import BLACK, GREEN, RED


class HealthBarSprite(Sprite):
    def __init__(self, rect, max_health):
        super().__init__()
        self.rect = rect
        self.max_health = max_health
        self.current_health = max_health
        self.image = Surface(self.rect.size)
        self.image.fill(BLACK)  # Set the background color to black

    def update_health(self, new_health):
        self.current_health = max(0, min(new_health, self.max_health))

    def draw(self, surface):
        # Draw the green portion (full health)
        full_health_rect = Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        pygame.draw.rect(surface, RED, full_health_rect)

        # Draw the red portion (current health)
        current_health_rect = Rect(self.rect.left, self.rect.top,
                                          int(self.rect.width * (self.current_health / self.max_health)),
                                          self.rect.height)
        pygame.draw.rect(surface, GREEN, current_health_rect)

        # Draw the black outline
        pygame.draw.rect(surface, BLACK, self.rect, 2)
