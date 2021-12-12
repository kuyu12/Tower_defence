import pygame

from Utils.Colors import WHITE, GREEN, GREY, BLUE
from Utils.Image_utils import ImageUtils
from Views.Surface_interface import SurfaceInterface


class TowerButton(SurfaceInterface):

    def __init__(self, tower, location, size):
        super().__init__(size, pygame.SRCALPHA)
        self.index = tower.index
        self.tower = tower
        self.location = location
        self.size = size
        self.active = tower.active
        self.selected = False
        self.over = False
        self.price = str(tower.price)
        self.image_url = tower.image_url
        self.image = ImageUtils.load_image(self.image_url)

        if not self.active:
            self.set_alpha(128)
        self.tower_image = pygame.transform.scale(self.image, size)
        self.blit(self.tower_image, (0, 0))

        self.small_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.textSurface = self.small_font.render(self.price, True, WHITE)
        self.blit(self.textSurface, [1, 1])

        self.rect = pygame.Rect(self.location[0], self.location[1], self.size[0], self.size[1])

    def get_draw_color(self):
        if self.selected:
            return GREEN
        if self.over and self.active:
            return BLUE
        return WHITE

    def draw(self, surface):
        surface.blit(self, (self.location[0], self.location[1]))
        draw_color = self.get_draw_color()
        pygame.draw.rect(surface, draw_color,self.rect, 1)
