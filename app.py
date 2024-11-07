import sys

import pygame

from Manager.Stage import Stage
from Utils.Conts import SCREEN_SIZE

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # load data
    stage = Stage('First_wave')

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            else:
                stage.update_event(event)

        stage.draw(screen)
        stage.update()
        pygame.display.update()
