import sys

import pygame

from Utils.Colors import GREY, WHITE, BLACK
from Utils.Image_utils import ImageUtils
from Utils.Paths import MENU_BACKGROUND_PATH
from Views.Surface_interface import SurfaceInterface
from Views.TD_button import TDButton
import pygame_widgets as pw

BUTTON_SIZE = 400


class Menu(SurfaceInterface):

    def __init__(self, size, screen,on_start_stage):
        super().__init__(size)
        self.background = pygame.transform.scale(ImageUtils.load_image(MENU_BACKGROUND_PATH), size)
        self.build_view(screen)
        self.on_start_stage = on_start_stage

    def build_view(self, screen):
        self.blit(self.background, (0, 0))

        self.button_play = TDButton(
            screen, (self.get_size()[0] / 2) - (BUTTON_SIZE / 2), (self.get_size()[1] / 2)+80, BUTTON_SIZE, 60,
            text='Play',
            fontSize=30, margin=10,
            inactiveColour=GREY,
            textColour=BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness=5,
            onClick=self.on_play_click)

        self.button_setting = TDButton(
            screen, (self.get_size()[0] / 2) - (BUTTON_SIZE / 2), (self.get_size()[1] / 2) + 150, BUTTON_SIZE, 60,
            text='Setting',
            fontSize=30, margin=10,
            inactiveColour=GREY,
            textColour=BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness=5)
            # onClick=self.on_play_click)

        self.button_quit = TDButton(
            screen, (self.get_size()[0] / 2) - (BUTTON_SIZE / 2), (self.get_size()[1] / 2) + 220, BUTTON_SIZE, 60,
            text='Quit',
            fontSize=30, margin=10,
            inactiveColour=GREY,
            textColour=BLACK,
            pressedColour=WHITE, radius=10,
            borderColour=BLACK,
            borderThickness=5,
            onClick=self.on_quit_click)

    def on_quit_click(self):
        pygame.quit()
        sys.exit()

    def on_play_click(self):
        print('on play click')
        self.on_start_stage('First_wave')

    def update(self):
        pass

    def update_event(self, event):
        pw.update(event)

    def draw(self, surface):
        surface.blit(self, (0, 0))
        self.button_play.draw()
        self.button_setting.draw()
        self.button_quit.draw()
