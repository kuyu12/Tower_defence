from Model.Tower_data import TowerData
from Utils.Conts import TOWERS_DATA
from Utils.Enums import TowersType
import uuid


class TowerFactory:
    @staticmethod
    def Tower(tower_type: TowersType, active=True):
        tower = TOWERS_DATA[tower_type]
        return TowerData(uuid.uuid1(),
                         tower_type,
                         tower['damage'],
                         tower['shot_speed'],
                         tower['upgrade'],
                         tower['price'],
                         tower['upgrade_price'],
                         tower['range'],
                         tower['image_url'],
                         active
                         )

    @staticmethod
    def GetAllTowers(active_towers):
        towers = []
        for tower_enum in TowersType.list():
            is_active = tower_enum in active_towers
            towers.append(TowerFactory.Tower(tower_enum,is_active))
        return towers
