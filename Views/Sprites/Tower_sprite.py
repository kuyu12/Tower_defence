import math

import pygame

from Utils.Conts import GRID_BLOCK_SIZE
from Utils.Image_utils import ImageUtils
from Views.Sprites.AnimatedSprite import AnimatedSprite


class TowerSprint(AnimatedSprite):

    def __init__(self, tower):
        self.tower = tower
        self.last_shot_time = 0
        self.range = self.tower.range
        self.shot_speed = self.tower.shot_speed * 10
        self.original_image = pygame.transform.rotate(
            ImageUtils.scale_image(ImageUtils.load_image(tower.image_url), (GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)), 180)
        self.image = self.original_image.copy()
        self.show_radius = False
        super(TowerSprint, self).__init__(tower.pixel_pos, [self.image])

    def update(self, enemy_pos=None):
        if enemy_pos:
            self.check_image_by_direction((self.rect.centerx, self.rect.centery), enemy_pos)

    def shot_if_possible(self, shot_pos, enemy):
        if pygame.time.get_ticks() - self.last_shot_time >= self.shot_speed:
            # TODO add attack sprit.
            self.last_shot_time = pygame.time.get_ticks()
            return self.tower, enemy
