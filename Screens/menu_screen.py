from Screens.base_screen import BaseScreen
from Utils.Conts import SCREEN_SIZE
from Views.TD_menu import Menu


class MenuScreen(BaseScreen):
    def __init__(self, screen, on_start_stage):
        self.menu = Menu(SCREEN_SIZE, screen=screen, on_start_stage=on_start_stage)
        self.on_start_stage = on_start_stage

    def handel_event(self, event):
        self.menu.update_event(event)

    def draw_screen(self, screen):
        self.menu.draw(screen)
        self.menu.update()
