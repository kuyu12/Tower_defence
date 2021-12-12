import sys

import pygame
from pygame_widgets.button import Button
import pygame_widgets as pw
from Utils.Colors import GREEN, WHITE, GREY, BLACK
from Utils.Conts import MAP_SIZE
from Views.Sprites.BackgroundSprite import BackgroundSprite


class MapPathPage:

    def __init__(self):
        pass

    def show_map_path_editor(self,stage_location, map_location, dict_json, on_finish):

        self.dict_json = dict_json
        self.on_finish = on_finish
        self.stage_location = stage_location

        pygame.init()
        screen = pygame.display.set_mode(MAP_SIZE)
        background_sprit = pygame.sprite.Group(BackgroundSprite(map_location, use_full_path=True))
        last_pos = None
        drawing = False

        self.paths = {}
        current_path = []
        path_count = 0

        # Done Button
        font = pygame.font.SysFont(pygame.font.get_default_font(), 100)
        text = font.render(str(path_count), True, GREEN)

        button_done = Button(
            screen, 5, 5, 55, 40,
            text='Done',
            fontSize=22, margin=5,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=2,
            onClick=self.onMapPathButtonClick)

        button_cancel = Button(
            screen, 65, 5, 55, 40,
            text='Cancel',
            fontSize=22, margin=5,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=2,
            onClick=self.onCancelButtonClick)

        background_sprit.draw(screen)

        while True:

            events = pygame.event.get()
            pw.update(events)

            for event in events:
                mouse_pos = pygame.mouse.get_pos()
                if not button_done.textRect.collidepoint(mouse_pos) and not button_cancel.textRect.collidepoint(
                        mouse_pos):
                    if event.type == pygame.MOUSEMOTION:
                        if (drawing):
                            mouse_position = pygame.mouse.get_pos()
                            current_path.append(mouse_position)
                            if last_pos is not None:
                                pygame.draw.line(screen, BLACK, last_pos, mouse_position, 5)
                            last_pos = mouse_position
                    elif event.type == pygame.MOUSEBUTTONUP:
                        drawing = False
                        self.paths[path_count] = current_path
                        path_count += 1
                        background_sprit.draw(screen)
                        text = font.render(str(path_count), True, GREEN)
                        screen.blit(text, (MAP_SIZE[0] - 70, MAP_SIZE[1] - 70))

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        drawing = True
                        current_path = []
                        last_pos = None

            pygame.display.update()

    def onMapPathButtonClick(self):
        self.dict_json['paths'] = self.paths
        self.on_finish(self.stage_location,self.dict_json)

    def onCancelButtonClick(self):
        pygame.quit()
        sys.exit()