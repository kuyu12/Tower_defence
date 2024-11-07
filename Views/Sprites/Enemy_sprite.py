import pygame

from Utils.Sprite_utils import SpriteUtils
from Utils.Conts import ENEMY_SIZE
from Utils.Image_utils import ImageUtils
from Views.Sprites.AnimatedSprite import Update_Type
from Views.Sprites.Extra_draw_sprite import ExtraDrawSprite
from Views.Sprites.Health_bar_sprite import HealthBarSprite


class EnemySprite(ExtraDrawSprite):
    def __init__(self, enemy, path):
        self.enemy = enemy

        self.original_image = pygame.transform.rotate(
            ImageUtils.scale_image(ImageUtils.load_image(enemy.image_url), ENEMY_SIZE), 180)
        self.image = self.original_image.copy()

        self.speed = enemy.speed
        self.health = enemy.health
        self.speed_counter = 0

        self.path = path
        self.next_path_location = 1
        self.current_degree = None

        # set location by center X and Y.
        start_location = (path[0][0] - (self.image.get_size()[0] / 2), path[0][1] - (self.image.get_size()[1] / 2))
        super(EnemySprite, self).__init__(start_location, [self.image])

        topleft = self.rect.topleft
        self.healthBar = HealthBarSprite(pygame.Rect(topleft[0], topleft[1], self.rect.width, 20), self.health)

    def update(self):
        self._check_next_path_location()
        super().update(Update_Type.TIME)
        move_x, move_y = self._get_location_to_path()
        self.speed_counter += 1
        if self.speed_counter % self.speed == 0:
            self.check_image_by_direction(self.path[self.next_path_location - 1],
                                          self.path[self.next_path_location])
            self.rect.x += move_x
            self.rect.y += move_y
            self.speed_counter = 0
        self.healthBar.rect = SpriteUtils.get_health_bar_size(self.rect)

    def _check_next_path_location(self):
        if self.next_path_location == len(self.path):
            print("finish")
            # TODO: send signal.

        if self.rect.centerx == self.path[self.next_path_location][0] and self.rect.centery == \
                self.path[self.next_path_location][1]:
            self.next_path_location += 1

    def set_health(self, health):
        self.health = health
        self.healthBar.update_health(health)

    def drawExtra(self, surface):
        super().drawExtra(surface)
        self.healthBar.draw(surface)

    def _get_location_to_path(self):
        current_x = self.rect.centerx
        current_y = self.rect.centery
        next_x = self.path[self.next_path_location][0]
        next_y = self.path[self.next_path_location][1]
        def_x = 0
        def_y = 0

        if next_x > current_x:
            def_x = 1
        if next_x < current_x:
            def_x = -1
        if next_y > current_y:
            def_y = 1
        if next_y < current_y:
            def_y = -1

        return def_x, def_y
