import json

from Manager.Enemy_manager import EnemiesManager
from Manager.Event_manager import EventManager
from Manager.Sound_manager import SoundManager
from Manager.Stage_manager import StageManager
from Utils.Enums import Action, EnemyType
from Utils.Paths import STAGES_PATH
from Views.Stage_view import StageView


class Stage:
    def __init__(self, stage_name):
        self.stage_name = stage_name
        self.event_manager = EventManager()
        self.sound_manager = SoundManager()
        self.enemy_manager = EnemiesManager()
        self._setup_event_manage()

        with open(STAGES_PATH + '/' + stage_name + '/stage_data.json') as f:
            self.stage_data = json.load(f)
        with open(STAGES_PATH + '/' + stage_name + '/wave_data.json') as f:
            self.wave_data = json.load(f)
        self.stage_view = StageView(self.stage_data)
        self.stage_manager = StageManager(self.stage_data, self.wave_data)

        # start stage
        self.stage_manager.start_stage(5)

    def _setup_event_manage(self):
        self.event_manager.on_stage_state_change = self.on_stage_state_change
        self.event_manager.on_action = self.on_action
        self.event_manager.enemy_action = self.on_enemy_action

    def on_stage_state_change(self, state, event):
        self.stage_view.set_stage_state(state, event)
        self.stage_manager.set_stage_state(state, event)

    def on_action(self, action, event):
        if action == Action.Tower_Placed:
            buy_data = self.stage_manager.buy_tower(event)
            if buy_data:
                self.sound_manager.play_drill_sound()
                self.stage_view.inject_action(action, buy_data)
            else:
                self.sound_manager.play_error_sound()

        if action == Action.Tower_Attack_Upgrade:
            buy_data = self.stage_manager.update_tower(event.data)
            if buy_data:
                self.sound_manager.play_coin_sound()
                self.stage_view.inject_action(action, buy_data)
            else:
                self.sound_manager.play_error_sound()

        if action == Action.Tower_Attack_Enemy:
            damage = event.data['tower'].damage
            enemy_index = event.data['enemy'].enemy.index
            self.sound_manager.play_explosion_sound()
            self.stage_view.add_explotion(enemy_index)
            self.enemy_manager.decrease_enemy_live(enemy_index, damage)

    def on_enemy_action(self, event, action):
        if action == Action.Add_Enemy:
            enemy_number = event.data['enemy']
            enemy = self.enemy_manager.add_enemies(EnemyType.convert_number_to_enemy(enemy_number))
            self.stage_view.add_enemy(enemy)
        if action == Action.Remove_Enemy:
            enemy = event.data['enemy']
            self.enemy_manager.remove_enemy(enemy.index)
            self.stage_view.remove_enemy(enemy.index)
            buy_data = self.stage_manager.enemy_has_remove(enemy)
            self.stage_view.inject_action(Action.Remove_Enemy, {'money': buy_data})
        if action == Action.Enemy_Update:
            enemy = event.data['enemy']
            self.stage_view.update_enemy(enemy)

    def update(self):
        self.stage_view.update()
        self.stage_manager.update()
        self.enemy_manager.update()

    def update_event(self, event):
        self.stage_view.update_event(event)

    def draw(self, surface):
        self.stage_view.draw(surface)
