import pygame

from Utils.Math_utils import distance


class SpriteUtils:

    @staticmethod
    def get_closet_enemy(x, y, max_radius, sprites: [pygame.sprite.Sprite], metric_func):
        radius_sprites = list(
            filter(lambda pos: distance((x, y), (pos.rect.centerx, pos.rect.centery)) <= max_radius, sprites))

        if radius_sprites:
            closet = metric_func(radius_sprites,
                                 key=lambda pos: distance((x, y), (pos.rect.centerx, pos.rect.centery)))
            return closet
        return None
