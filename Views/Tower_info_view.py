import pygame
from pygame_widgets.button import Button
from Utils.Colors import WHITE, GREY, LIGHT_BLUE, BLUE, BLACK
from Utils.Conts import TOWER_INFO_SIZE
from Utils.Enums import Signals, TowerUpgrade
from Utils.Image_utils import ImageUtils
from Utils.Paths import TOWER_INFO_BACKGROUND_PATH
import pygame_widgets as pw
from Views.Surface_interface import SurfaceInterface
from Views.TD_button import TDButton


class TowerInfoView(SurfaceInterface):

    def __init__(self, tower, tower_rect):
        super().__init__(TOWER_INFO_SIZE)
        self.first_time_draw = True
        self.offset = 50

        self.tower = tower
        self.rect = tower_rect
        self.method_func = tower.attack_method
        self.draw_location = self.rect.x + self.offset, self.rect.y + self.offset
        self.draw_rect = pygame.Rect(self.draw_location[0], self.draw_location[1], TOWER_INFO_SIZE[0],
                                     TOWER_INFO_SIZE[1])
        self.name = self.tower.name
        self.damage = self.tower.damage
        self.shot_speed = self.tower.shot_speed
        self.range = self.tower.range
        self.upgrade_price = self.tower.upgrade_price

        self.background = pygame.transform.scale(ImageUtils.load_image(TOWER_INFO_BACKGROUND_PATH),
                                                 TOWER_INFO_SIZE)
        self.small_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.big_font = pygame.font.SysFont(pygame.font.get_default_font(), 25)

        self.textNameSurface = self.small_font.render(self.name, True, WHITE)
        self.texDamageSurface = self.small_font.render('Damage: ' + str(self.damage), True, WHITE)
        self.texShotSurface = self.small_font.render('Shot speed: ' + str(self.shot_speed), True, WHITE)
        self.texRangeSurface = self.small_font.render('Range: ' + str(self.range), True, WHITE)

        self.texAttackFocusSurface = self.small_font.render('Attack Upgrade', True, WHITE)

        self.button_attack_upgrade_speed = TDButton(
            None, self.draw_location[0] + 180, self.draw_location[1] + 80, 80, 35,
            text=f'Speed {self.upgrade_price}$',
            fontSize=18, margin=5,
            inactiveColour=GREY,
            textColour=BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness=2,
            onClick=self.on_speed_click)

        self.button_attack_upgrade_damage = TDButton(
            None, self.draw_location[0] + 180, self.draw_location[1] + 120, 80, 35,
            text=f'Damage {self.upgrade_price}$',
            fontSize=18, margin=5,
            inactiveColour=GREY,
            textColour=BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness=2,
            onClick=self.on_damage_click)

    def update_view(self):
        self.name = self.tower.name
        self.damage = self.tower.damage
        self.shot_speed = self.tower.shot_speed
        self.range = self.tower.range
        self.upgrade_price = self.tower.upgrade_price

        self.small_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.big_font = pygame.font.SysFont(pygame.font.get_default_font(), 25)

        self.textNameSurface = self.small_font.render(self.name, True, WHITE)
        self.texDamageSurface = self.small_font.render('Damage: ' + str(self.damage), True, WHITE)
        self.texShotSurface = self.small_font.render('Shot speed: ' + str(self.shot_speed), True, WHITE)
        self.texRangeSurface = self.small_font.render('Range: ' + str(self.range), True, WHITE)

        self.texAttackFocusSurface = self.small_font.render('Attack Upgrade', True, WHITE)

        self.button_attack_upgrade_speed.update_text(f'Speed {self.upgrade_price}$')
        self.button_attack_upgrade_damage.update_text(f'Damage {self.upgrade_price}$')

    def on_speed_click(self):
        self.send_signal(Signals.Tower_Upgrade,
                         {'upgrade': TowerUpgrade.Speed, 'cost': self.tower.upgrade_price, 'index': self.tower.index})

    def on_damage_click(self):
        self.send_signal(Signals.Tower_Upgrade,
                         {'upgrade': TowerUpgrade.Damage, 'cost': self.tower.upgrade_price, 'index': self.tower.index})

    def update(self):
        pass

    def update_event(self, event):
        if not self.first_time_draw:
            pw.update(event)

    def draw(self, surface):
        if self.first_time_draw:
            self.button_attack_upgrade_speed.win = surface
            self.button_attack_upgrade_damage.win = surface

        surface.blit(self.background, (self.draw_location[0], self.draw_location[1]))
        surface.blit(self.textNameSurface,
                     [self.draw_location[0] + (TOWER_INFO_SIZE[0] / 2) - 20, self.draw_location[1] + 40])
        surface.blit(self.texDamageSurface, [self.draw_location[0] + 50, self.draw_location[1] + 60])
        surface.blit(self.texShotSurface, [self.draw_location[0] + 50, self.draw_location[1] + 80])
        surface.blit(self.texRangeSurface, [self.draw_location[0] + 50, self.draw_location[1] + 100])

        surface.blit(self.texAttackFocusSurface, [self.draw_location[0] + 160, self.draw_location[1] + 60])

        self.button_attack_upgrade_speed.draw()
        self.button_attack_upgrade_damage.draw()
        self.first_time_draw = False
