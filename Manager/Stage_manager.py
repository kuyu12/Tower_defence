from pydispatch import dispatcher
import random
import pygame

from Model.Signal_data import SignalData
from Utils.Conts import stage_mapper, TOWERS_DATA, ENEMY_MAX_WAVE_TIME, ENEMY_MIN_WAVE_TIME
from Utils.Enums import Map_State, Signals


class StageManager:

    def __init__(self, stage_data, wave_data):
        self.stage_data = stage_data
        self.health = stage_data[stage_mapper['start_health']]
        self.money = stage_data[stage_mapper['start_money']]
        self.build_towers = []
        self.waves_data = wave_data
        self.wave_number = 0
        self.tower_current_selected = None
        self.map_state = None
        self.timer = None
        self.clock = pygame.time.Clock()
        self.enemy_send_time = 0
        self.next_wave_random_time = 0
        self._is_wave_start = False
        self.parsing_wave = []

    def start_stage(self, delay):
        self.enemy_send_time = pygame.time.get_ticks()
        self.current_wave = self.waves_data[str(self.wave_number)]

        self.next_wave_random_time = delay * 1000

        for enemy_key in self.current_wave:
            enemy_counts = self.current_wave[enemy_key]
            self.parsing_wave.extend([enemy_key] * int(enemy_counts))
        self._is_wave_start = True

    def send_next_wave(self, delay=10):
        self.enemy_send_time = pygame.time.get_ticks()
        self.wave_number += 1

        if self.wave_number >= len(self.waves_data):
            # TODO finish screen
            return

        self.current_wave = self.waves_data[str(self.wave_number)]
        self.next_wave_random_time = delay * 1000

        for enemy_key in self.current_wave:
            enemy_counts = self.current_wave[enemy_key]
            self.parsing_wave.extend([enemy_key] * int(enemy_counts))

    def send_wave_if_needed(self, time):
        if not self._is_wave_start:
            return

        if len(self.parsing_wave) == 0:
            self.send_next_wave(delay=7)
            return

        time_pass = time - self.enemy_send_time
        if time_pass >= self.next_wave_random_time:
            self.enemy_send_time = pygame.time.get_ticks()

            enemy = self.parsing_wave.pop(random.randrange(len(self.parsing_wave)))

            self.next_wave_random_time = random.randint(ENEMY_MIN_WAVE_TIME, ENEMY_MAX_WAVE_TIME)
            signal_data = SignalData(sender=self.__class__.__name__, signal=Signals.Add_Enemy, data={'enemy': enemy})
            dispatcher.send(signal=Signals.Add_Enemy,
                            event=signal_data)

    def set_stage_state(self, state, event):
        self.map_state = Map_State.state_init(state)
        self.tower_current_selected = event.data if self.map_state == Map_State.Tower_Selected else None

    def buy_tower(self, pos_event):
        tower = self.tower_current_selected['tower']
        tower_data = TOWERS_DATA[tower.name]
        cost = tower_data['price']

        if self.money >= cost and self._check_tower_location(pos_event.data['pos']):
            self.money -= cost
            build_tower = tower.copy_new_tower(pos_event.data['pos'])
            self.build_towers.append(build_tower)
            return {'tower': build_tower, 'money': self.money}

        return False

    def enemy_has_remove(self, enemy):
        self.money += enemy.worth_money
        return self.money

    def _check_tower_location(self, pos):
        for current_tower in self.build_towers:
            if current_tower.pos == pos:
                return False
        return True

    def update(self):
        self.send_wave_if_needed(pygame.time.get_ticks())
