import pygame

from Utils.Colors import BLACK, RED, GREY, WHITE
from Utils.Conts import stage_mapper
from Utils.Image_utils import ImageUtils
from Utils.Paths import USER_INFO_BACKGROUND_PATH
from Views.Surface_interface import SurfaceInterface


class StageInfoView(SurfaceInterface):

    def __init__(self, size, draw_location, stage_data):
        super().__init__(size)
        self.stage_data = stage_data
        self.draw_location = draw_location
        self.stage_name = stage_data[stage_mapper['map_name']]
        self.health_base = stage_data[stage_mapper['start_health']]
        self.health = self.health_base
        self.money = stage_data[stage_mapper['start_money']]
        self.background = pygame.transform.scale(ImageUtils.load_image(USER_INFO_BACKGROUND_PATH), size)
        self.build_view()

    def build_view(self):
        self.blit(self.background, (0, 0))

        self.small_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

        textHealthSurface = self.small_font.render("Health:", True, GREY)
        self.blit(textHealthSurface, [40, 40])

        textManaSurface = self.small_font.render("Money:", True, GREY)
        self.blit(textManaSurface, [40, 65])

        self.healthSurface = self.small_font.render(str(self.health), True, WHITE)
        self.blit(self.healthSurface, [90, 40])

        self.moneySurface = self.small_font.render(str(self.money), True, WHITE)
        self.blit(self.moneySurface, [90, 65])

    def set_health(self, health):
        self.health = health
        self.build_view()

    def set_money(self, money):
        self.money = money
        self.build_view()

    def update(self):
        pass

    def update_event(self, event):
        # TODO get click event
        pass

    def draw(self, surface):
        surface.blit(self, (self.draw_location[0], self.draw_location[1]))
