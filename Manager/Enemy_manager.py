from pydispatch import dispatcher

from Model.Enemy_data import EnemyData
from Model.Factory.Enemy_factory import EnemyFactory
from Model.Signal_data import SignalData
from Utils.Enums import EnemyType, Signals


class EnemiesManager:
    def __init__(self):
        self.enemies = []

    def add_enemies(self, enemy_type: EnemyType):
        enemy_data = EnemyFactory.Enemy(enemy_type.name)
        self.enemies.append(enemy_data)
        return enemy_data

    def remove_enemy(self,enemy_index):
        self.enemies = list(filter(lambda x: x.index != enemy_index, self.enemies))

    def decrease_enemy_live(self,enemy_index,damage):
        print(enemy_index)
        enemy = next(filter(lambda x: x.index == enemy_index, self.enemies))
        enemy.health -= damage

    def update(self):
        for enemy in self.enemies:
            if enemy.health <= 0:
                signal_data = SignalData(sender=self.__class__.__name__, signal=Signals.Remove_Enemy,
                                         data={'enemy': enemy})
                dispatcher.send(signal=Signals.Remove_Enemy,event=signal_data)