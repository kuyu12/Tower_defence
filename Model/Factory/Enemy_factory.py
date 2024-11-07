
import uuid

from Model.Enemy_data import EnemyData
from Utils.Conts import ENEMY_DATA
from Utils.Enums import EnemyType


class EnemyFactory:
    @staticmethod
    def Enemy(enemy_type: EnemyType):
        enemy = ENEMY_DATA[enemy_type]
        return EnemyData(uuid.uuid4(),
                         enemy_type,
                         enemy['health'],
                         enemy['speed'],
                         enemy['image_url'],
                         enemy['worth_money']
                         )