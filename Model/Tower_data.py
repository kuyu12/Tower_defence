import uuid

from Model.Figure_data import FigureData
from Utils.Conts import GRID_BLOCK_SIZE


class TowerData(FigureData):
    def __init__(self, index, name, damage, shot_speed, upgrade, price, upgrade_price, range, image_url, active,
                 pos=None):
        super(TowerData, self).__init__(index, name, image_url)
        self.damage = damage
        self.shot_speed = shot_speed
        self.upgrade = upgrade
        self.price = price
        self.upgrade_price = upgrade_price
        self.range = range
        self.active = active
        self.pos = pos
        self.pixel_pos = None if pos is None else (pos[0]*GRID_BLOCK_SIZE, pos[1]*GRID_BLOCK_SIZE)
        self.attack_method = min

    def copy_new_tower(self, pos):
        return TowerData(uuid.uuid1(),
                         self.name,
                         self.damage,
                         self.shot_speed,
                         self.upgrade,
                         self.price,
                         self.upgrade_price,
                         self.range,
                         self.image_url,
                         self.active,
                         pos)
