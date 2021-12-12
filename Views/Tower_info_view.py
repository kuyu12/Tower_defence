import pygame
from pygame_widgets.button import Button
from Utils.Colors import WHITE, GREY, LIGHT_BLUE, BLUE, BLACK
from Utils.Conts import TOWER_INFO_SIZE
from Utils.Enums import Signals
from Utils.Image_utils import ImageUtils
from Utils.Paths import TOWER_INFO_BACKGROUND_PATH
import pygame_widgets as pw
from Views.Surface_interface import SurfaceInterface


class TowerInfoView(SurfaceInterface):

    def __init__(self, tower, tower_rect):
        super().__init__(TOWER_INFO_SIZE)
        self.first_time_draw = True
        self.offset = 50

        self.tower = tower
        self.rect = tower_rect
        self.method_func = tower.attack_method
        self.draw_location = self.rect.x + self.offset, self.rect.y + self.offset
        self.draw_rect = pygame.Rect(self.draw_location[0],self.draw_location[1],TOWER_INFO_SIZE[0],TOWER_INFO_SIZE[1])
        self.name = self.tower.name
        self.damage = self.tower.damage
        self.shot_speed = self.tower.shot_speed
        self.range = self.tower.range
        self.upgrade_price = self.tower.upgrade_price

        self.background = pygame.transform.scale(ImageUtils.load_image(TOWER_INFO_BACKGROUND_PATH),
                                                 TOWER_INFO_SIZE)
        self.small_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.big_font = pygame.font.SysFont(pygame.font.get_default_font(), 25)

        self.textNameSurface = self.small_font.render(self.name, True, GREY)
        self.texDamageSurface = self.small_font.render('Damage: ' + str(self.damage), True, GREY)
        self.texShotSurface = self.small_font.render('Shot speed: ' + str(self.shot_speed), True, GREY)
        self.texRangeSurface = self.small_font.render('Range: ' + str(self.range), True, GREY)

        self.texAttackFocusSurface = self.small_font.render('Attack Focus', True, GREY)

        self.button_attack_method_max = Button(
            None, self.draw_location[0] + 200, self.draw_location[1] + 80, 50, 35,
            text='farthest',
            fontSize=20, margin=5,
            inactiveColour=GREY,
            textColour= BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness = 2,
            onClick=self.on_max_click)

        self.button_attack_method_min = Button(
            None, self.draw_location[0] + 200, self.draw_location[1] + 120, 50, 35,
            text='closest',
            fontSize=20, margin=5,
            inactiveColour=GREY,
            textColour=BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness=2,
            onClick=self.on_min_click)

    def on_max_click(self):
        self.method_func = max
        self.send_signal(Signals.Tower_Attack_Method_Change, {'method': self.method_func,'index': self.tower.index})

    def on_min_click(self):
        self.method_func = min
        self.send_signal(Signals.Tower_Attack_Method_Change, {'method': self.method_func,'index': self.tower.index})

    def set_button_active(self):
        self.button_attack_method_min.setInactiveColour(LIGHT_BLUE if self.method_func == min else GREY)
        self.button_attack_method_max.setInactiveColour(LIGHT_BLUE if self.method_func == max else GREY)

    def update(self):
        self.set_button_active()

    def update_event(self, event):
        if not self.first_time_draw:
            pw.update(event)

    def draw(self, surface):
        if self.first_time_draw:
            self.button_attack_method_max.win = surface
            self.button_attack_method_min.win = surface

        surface.blit(self.background, (self.draw_location[0], self.draw_location[1]))
        surface.blit(self.textNameSurface,
                     [self.draw_location[0] + (TOWER_INFO_SIZE[0] / 2) - 20, self.draw_location[1] + 40])
        surface.blit(self.texDamageSurface, [self.draw_location[0] + 50, self.draw_location[1] + 60])
        surface.blit(self.texShotSurface, [self.draw_location[0] + 50, self.draw_location[1] + 80])
        surface.blit(self.texRangeSurface, [self.draw_location[0] + 50, self.draw_location[1] + 100])

        surface.blit(self.texAttackFocusSurface, [self.draw_location[0] + 180, self.draw_location[1] + 60])

        self.button_attack_method_max.draw()
        self.button_attack_method_min.draw()
        self.first_time_draw = False
