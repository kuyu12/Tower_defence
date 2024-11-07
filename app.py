import sys
import pygame
from Screens.game_screen import GameScreen
from Screens.menu_screen import MenuScreen
from Utils.Conts import SCREEN_SIZE
from Utils.Enums import ScreenType


def start_game(stage_name):
    global screenManager
    screenManager = GameScreen()
    screenManager.start_stage(stage_name)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Romi TD')
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen_status = ScreenType.Menu

    # Start on menu screen
    screenManager = MenuScreen(screen, start_game)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            else:
                screenManager.handel_event(event)

        screenManager.draw_screen(screen)
        pygame.display.update()
