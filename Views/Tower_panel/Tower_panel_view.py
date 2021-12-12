from math import ceil
import pygame
from pygame import Rect
from Model.Factory.Towers_factory import TowerFactory
from Utils.Conts import PANEL_SIZE, stage_mapper, TOWER_BUTTON_SIZE
from Utils.Enums import Signals
from Utils.Image_utils import ImageUtils
from Utils.Paths import TOWER_PANEL_INFO_BACKGROUND_PATH
from Views.Sprites.BackgroundSprite import BackgroundSprite
from Views.Surface_view import SurfaceView
from Views.Tower_panel.Stage_info_view import StageInfoView
from Views.Tower_panel.Tower_button import TowerButton


class TowerPanelView(SurfaceView):

    def __init__(self, stage_data, x, y):
        self.panel_size = PANEL_SIZE
        self.stage_data = stage_data
        self.tower_options = stage_data[stage_mapper['tower_sprits']]
        self.towers = []
        self.towers_buttons = []
        self.panel_rect = Rect(x, y, x + self.panel_size[0], y + self.panel_size[1])
        self.tower_grid_location = (x, y + int(self.panel_size[1] / 4))
        self.tower_image_location = (x, y + int(self.panel_size[1] / 6))
        self.tower_size = (self.panel_size[0], self.panel_size[1] - int(self.panel_size[1] / 2))
        self.stage_info = StageInfoView((self.panel_size[0], int(self.panel_size[1] / 6)), (x, y), self.stage_data)
        self.setup()

    def setup(self):
        self.towers = TowerFactory.GetAllTowers(self.tower_options)
        self.setup_tower_buttons(self.towers, self.tower_grid_location, self.tower_size)

        self.background = pygame.transform.scale(ImageUtils.load_image(TOWER_PANEL_INFO_BACKGROUND_PATH),
                                                 (self.panel_size[0], self.panel_size[1] - int(self.panel_size[1] / 6)))
        self.background_sprite = BackgroundSprite(self.background, is_image=True, location=self.tower_image_location)
        self.background_view = pygame.sprite.Group(self.background_sprite)

    def setup_tower_buttons(self, towers, location, size):
        for index, tower in enumerate(towers, start=1):
            y_gap = size[1] / 4
            location_x = location[0] + int(size[0] / 3 if index % 2 == 0 else (size[0] / 3 * 2))
            location_x = location_x - (TOWER_BUTTON_SIZE[0] / 2)  # center
            location_y = location[1] + ceil(index / 2) * y_gap
            location_y = location_y - (TOWER_BUTTON_SIZE[1] / 2)  # center
            self.towers_buttons.append(TowerButton(tower, (location_x, location_y), TOWER_BUTTON_SIZE))

    def update(self):
        pass

    def update_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            for button in self.towers_buttons:
                button.over = bool(button.rect.collidepoint(mouse_pos))
        if event.type == pygame.MOUSEBUTTONUP:
            for button in self.towers_buttons:
                button.selected = bool(button.rect.collidepoint(mouse_pos)) & button.active
                if button.selected:
                    self.send_signal(Signals.Tower_Selected, {'tower': button.tower})

    def draw(self, surface):
        self.background_view.draw(surface)
        self.stage_info.draw(surface)
        for button in self.towers_buttons:
            button.draw(surface)
