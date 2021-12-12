from math import sqrt

import pygame

from Manager.Tower_sprite_manager import TowerSpriteManager
from Utils.Paths import EXPLOSION_IMAGES_PATH
from Views.Sprites.Enemy_sprite import EnemySprite
from Views.Sprites.Explosion_sprite import ExplosionSprite
from Views.Sprites.TD_sprite_controller import TDSpriteController
from Utils.Conts import stage_mapper, EXPLOSION_SIZE
from Utils.Enums import Map_State, Action
from Views.Grid_view import GridView
from Views.Sprites.BackgroundSprite import BackgroundSprite
from Views.Sprites.Tower_sprite import TowerSprint
from Views.Surface_view import SurfaceView
from Views.Tower_panel.Tower_panel_view import TowerPanelView
from random import randrange


class StageView(SurfaceView):

    def __init__(self, stage_data):
        self.stage_data = stage_data
        self.map_state = Map_State.Normal
        self.stage_name = stage_data[stage_mapper['map_name']]
        self.map_image_path = stage_data[stage_mapper['map_path']]
        self.wave_count = stage_data[stage_mapper['wave_count']]
        self.enemy_paths = self.stage_data[stage_mapper['paths']]

        # Sprites
        self.background_sprite = BackgroundSprite(self.map_image_path, use_full_path=True)
        self.spriteGroupController = TDSpriteController(self.background_sprite, [])
        self.background_view = pygame.sprite.Group(self.background_sprite)
        self.tower_panel_view = TowerPanelView(self.stage_data, self.background_sprite.rect.width,
                                               self.background_sprite.rect.y)
        self.towers_manager = TowerSpriteManager()
        self.enemies = []

        self.grid_view = GridView(stage_data[stage_mapper['board_matrix']])

    def add_enemy(self, enemy_data):
        path_rand = str(randrange(len(self.enemy_paths)))
        enemy = EnemySprite(enemy_data, self.enemy_paths[path_rand])
        self.enemies.append(enemy)
        self.spriteGroupController.add(enemy)

    def remove_enemy(self,enemy_index):
        enemy = next(filter(lambda x: x.enemy.index == enemy_index, self.enemies))
        self.enemies.remove(enemy)
        enemy.kill()

    def set_stage_state(self, state, event):
        self.map_state = Map_State.state_init(state)
        self._on_stage_state_change()

    def _on_stage_state_change(self):
        self.grid_view.is_show = self.map_state == Map_State.Tower_Selected

    def inject_action(self, action, event):
        self._on_action(action, event)

    def add_explotion(self, enemy_index):
        enemy = next(filter(lambda x: x.enemy.index == enemy_index, self.enemies))
        position = (enemy.rect.centerx - (EXPLOSION_SIZE[0]/2), enemy.rect.centery - (EXPLOSION_SIZE[1]/2))
        explosionSprint = ExplosionSprite(position,EXPLOSION_IMAGES_PATH)
        self.spriteGroupController.add(explosionSprint)

    def _on_action(self, action, event):
        if action == Action.Tower_Placed:
            tower_data = event['tower']
            self.tower_panel_view.stage_info.set_money(event['money'])
            tower_sprite = TowerSprint(tower_data)
            self.towers_manager.add_tower(tower_sprite)
            self.spriteGroupController.add(tower_sprite)

        if action == Action.Tower_Attack_Method_Change:
            self.towers_manager.set_tower_attack_method(event['index'], event['method'])

        if action == Action.Remove_Enemy:
            self.tower_panel_view.stage_info.set_money(event['money'])

    def update(self):
        for enemy in self.enemies:
            enemy.update()

        self.towers_manager.update(self.enemies)
        self.spriteGroupController.update()

    def update_event(self, event):
        self.towers_manager.update_event(event, map_state=self.map_state)
        self.tower_panel_view.update_event(event)
        self.grid_view.update_event(event)

    def draw(self, surface):
        self.spriteGroupController.draw(surface)
        self.grid_view.draw(surface)
        self.tower_panel_view.draw(surface)
        self.towers_manager.draw(surface)
