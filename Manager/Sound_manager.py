import pygame

from Utils.Enums import EnemyType
from Utils.Paths import ERROR_SOUND_PATH, DRILL_SOUND_PATH, EXPLOSION_1_SOUND_PATH, EXPLOSION_2_SOUND_PATH, COIN_SOUND_PATH


class SoundManager:
    def __init__(self):
        self.error_effect = pygame.mixer.Sound(ERROR_SOUND_PATH)
        self.drill_effect = pygame.mixer.Sound(DRILL_SOUND_PATH)
        self.explosion_effect1 = pygame.mixer.Sound(EXPLOSION_1_SOUND_PATH)
        self.explosion_effect2 = pygame.mixer.Sound(EXPLOSION_2_SOUND_PATH)
        self.coin_effect = pygame.mixer.Sound(COIN_SOUND_PATH)

        self.explosion_effect1.set_volume(0.1)
        self.explosion_effect1.fadeout(2)

    def play_error_sound(self):
        self.error_effect.play()

    def play_drill_sound(self):
        self.drill_effect.play()

    def play_explosion_sound(self):
        self.explosion_effect1.play()

    def play_coin_sound(self):
        self.coin_effect.play()
