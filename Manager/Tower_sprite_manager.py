import pygame

from Manager.Base_manager import BaseManager
from Utils.Colors import RED
from Utils.Enums import Map_State, Signals
from Utils.Sprite_utils import SpriteUtils
from Views.Tower_info_view import TowerInfoView


class TowerSpriteManager(BaseManager):

    def __init__(self):
        self.towers = []
        self.tower_info = None

    def add_tower(self, tower):
        self.towers.append(tower)

    def remove_tower(self, tower):
        self.towers.remove(tower)

    def set_tower_attack_method(self,tower_index,method):
        tower = next(x for x in self.towers if x.tower.index == tower_index)
        tower.tower.attack_method = method

    def update(self, enemies):
        if self.tower_info:
            self.tower_info.update()

        for tower in self.towers:
            closet_enemy = SpriteUtils.get_closet_enemy(tower.rect.centerx, tower.rect.centery, tower.range, enemies,
                                                        tower.tower.attack_method)
            if closet_enemy:
                tower.update((closet_enemy.rect.centerx, closet_enemy.rect.centery))
                shot_data = tower.shot_if_possible((closet_enemy.rect.centerx, closet_enemy.rect.centery), closet_enemy)
                if shot_data:
                    tower_data,enemy_data = shot_data
                    self.send_signal(Signals.Tower_Attack_Enemy,{'tower':tower_data,"enemy":enemy_data})

    def update_event(self, event, map_state):
        if map_state == Map_State.Normal:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                for tower in self.towers:
                    tower_collidepoint = tower.rect.collidepoint(mouse_pos)
                    tower.show_radius = tower_collidepoint
                    if tower_collidepoint:
                        self.tower_info = TowerInfoView(tower.tower, tower.rect)

                if self.tower_info is not None and self.tower_info.draw_rect.collidepoint(mouse_pos):
                    tower = list(filter(lambda x: x.tower.index == self.tower_info.tower.index, self.towers)).pop()
                    tower.show_radius = True

            if self.tower_info:
                self.tower_info.update_event(event)

    def draw(self, surface):
        for tower in self.towers:
            if tower.show_radius:
                pygame.draw.circle(surface, RED, (tower.rect.centerx, tower.rect.centery), tower.range, width=2)
                self.tower_info.draw(surface)
