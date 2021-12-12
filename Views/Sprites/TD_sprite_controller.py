import pygame
from Views.Sprites.Explosion_sprite import ExplosionSprite


class TDSpriteController(pygame.sprite.Group):
    def __init__(self, background, *sprites):
        self.background_group = pygame.sprite.Group(background)
        super().__init__(sprites)

    def update(self, *args, **kwargs):
        super().update()
        for sprite in self.sprites():
            if isinstance(sprite, ExplosionSprite):
                sprite.update()
        self.background_group.update()

    def draw(self, surface, game_state=None):
        self.background_group.draw(surface)
        super().draw(surface)
