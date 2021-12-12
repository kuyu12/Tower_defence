import pygame
from pygame.rect import Rect

from Utils.Colors import GREEN, RED, BLACK, BLUE
from Utils.Conts import MAP_SIZE, GRID_BLOCK_SIZE
from Utils.Enums import Signals
from Views.Surface_view import SurfaceView


class GridView(SurfaceView):

    def __init__(self, board_matrix):
        self.board_matrix = board_matrix
        self.rectangles = []
        self.setup()
        self.is_show = False

    def setup(self):
        self.rectangles = self.createGrid()

    def update(self):
        pass

    def update_event(self, event):
        # don't update event when no show
        if not self.is_show:
            return

        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            for index, (rect, color, pos) in enumerate(self.rectangles):
                color_num = BLUE if bool(rect.collidepoint(mouse_pos)) else BLACK
                self.rectangles[index] = (rect, color_num, pos)
        if event.type == pygame.MOUSEBUTTONUP:
            for rect, color, pos in self.rectangles:
                if rect.collidepoint(mouse_pos):
                    self.send_signal(Signals.Tower_Placed, {'pos': pos})
            if Rect(0, 0, MAP_SIZE[0], MAP_SIZE[1]).collidepoint(mouse_pos):
                self.send_signal(Signals.Tower_Deselected, None)

    def draw(self, surface):
        if self.is_show:
            for rect, color, _ in self.rectangles:
                pygame.draw.rect(surface, color, rect, 2)

    def createGrid(self):
        blockSize = GRID_BLOCK_SIZE
        rects = []
        for x in range(0, MAP_SIZE[0], int(blockSize)):
            for y in range(0, MAP_SIZE[1], int(blockSize)):
                x_pox = int(x / blockSize)
                y_pox = int(y / blockSize)
                if self.board_matrix[x_pox][y_pox] == 0.0:
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    rects.append((rect, BLACK, (x_pox, y_pox)))
        return rects
