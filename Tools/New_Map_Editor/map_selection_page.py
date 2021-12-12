import sys
from math import ceil

import numpy as np
import pygame
from pygame_widgets.button import Button

from Utils.Colors import WHITE, GREY, GREEN, RED
from Utils.Conts import MAP_SIZE, stage_mapper
from Views.Sprites.BackgroundSprite import BackgroundSprite
import pygame_widgets as pw


class MapSelectionAreaPage:

    def __init__(self):
        pass

    def show_map_selection_editor(self,stage_location, map_location, dict_json, on_finish):
        self.map_location = map_location
        self.stage_location = stage_location
        self.dict_json = dict_json
        self.on_finish = on_finish

        pygame.init()
        screen = pygame.display.set_mode(MAP_SIZE)
        blockSize = MAP_SIZE[0] / 20

        # Background
        background_sprit = pygame.sprite.Group(BackgroundSprite(map_location, use_full_path=True))

        # Done Button
        button_done = Button(
            screen, 5, 5, 55, 40,
            text='Done',
            fontSize=22, margin=5,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=2,
            onClick=self.onMapSelectionButtonClick)

        button_cancel = Button(
            screen, 65, 5, 55, 40,
            text='Cancel',
            fontSize=22, margin=5,
            inactiveColour=WHITE,
            pressedColour=GREY, radius=2,
            onClick=self.onCancelButtonClick)

        # metrix
        self.board_metrix = np.zeros((ceil(MAP_SIZE[0] / blockSize), ceil(MAP_SIZE[1] / blockSize)))
        rectangles = self.createGrid(blockSize)

        background_sprit.draw(screen)
        for rect, color, _ in rectangles:
            pygame.draw.rect(screen, color, rect, 1)

        while True:
            events = pygame.event.get()
            pw.update(events)

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if not button_done.textRect.collidepoint(mouse_pos) and not button_cancel.textRect.collidepoint(
                            mouse_pos):
                        for index, (rect, color, pos) in enumerate(rectangles):
                            if rect.collidepoint(mouse_pos):
                                self.board_metrix[pos[0], pos[1]] = 0 if (self.board_metrix[pos[0], pos[1]] + 1) > 1 else (
                                        self.board_metrix[pos[0], pos[1]] + 1)
                                color_num = GREEN if self.board_metrix[pos[0], pos[1]] == 0.0 else RED
                                rectangles[index] = (rect, color_num, pos)
                                break

                        pygame.draw.rect(screen, color_num, rect, 1)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                pygame.display.update()

    def createGrid(self,blockSize):
        rects = []
        for x in range(0, MAP_SIZE[0], int(blockSize)):
            for y in range(0, MAP_SIZE[1], int(blockSize)):
                x_pox = int(x / blockSize)
                y_pox = int(y / blockSize)

                rect = pygame.Rect(x, y, blockSize, blockSize)
                rects.append((rect, GREEN, (x_pox, y_pox)))
        return rects

    def onMapSelectionButtonClick(self):
        self.dict_json[stage_mapper['board_matrix']] = self.board_metrix.tolist()
        self.on_finish(self.stage_location, self.map_location, self.dict_json)

    def onCancelButtonClick(self):
        pygame.quit()
        sys.exit()

