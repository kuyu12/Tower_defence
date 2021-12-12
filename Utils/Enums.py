from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Difficulty(ExtendedEnum):
    Easy = 'Easy'
    Medium = 'Medium'
    Hard = 'Hard'


class Signals(ExtendedEnum):
    Tower_Deselected = 0
    Tower_Placed = 1
    Tower_Selected = 2
    Add_Enemy = 3
    Tower_Attack_Method_Change = 4
    Tower_Attack_Enemy = 5
    Remove_Enemy = 6


class Stage_State(ExtendedEnum):
    Normal = 0
    Tower_Selected = 1


class Action(ExtendedEnum):
    Tower_Placed = 0
    Tower_Attack_Method_Change = 1
    Tower_Attack_Enemy = 2
    Add_Enemy = 3
    Remove_Enemy = 4


class Map_State(ExtendedEnum):
    Normal = 0
    Tower_Selected = 1

    @staticmethod
    def state_init(stage_state):
        if stage_state == Stage_State.Normal:
            return Map_State.Normal
        if stage_state == Stage_State.Tower_Selected:
            return Map_State.Tower_Selected
        return None


class TowersType(ExtendedEnum):
    Vulcan = 'Vulcan'
    Howitzer = 'Howitzer'
    Anti_Tank = 'Anti_Tank'
    Beaufort = 'Beaufort'
    Mortar = 'Mortar'
    Laser = 'Laser'
    Armor_piercing = 'Armor_piercing'
    Garival = 'Garival'


class EnemyType(ExtendedEnum):
    Armored_vehicle_1 = 'Armored vehicle1'
    Armored_vehicle_2 = 'Armored vehicle2'
    Armored_vehicle_3 = 'Armored vehicle3'
    Basic_tank_1 = 'Basic tank1'
    Basic_tank_2 = 'Basic tank2'
    Basic_tank_3 = 'Basic tank3'
    Light_tank_1 = 'Light tank1'
    Light_tank_2 = 'Light tank2'
    Medium_tank = 'Medium tank'
    Heavy_tank_1 = 'Heavy tank1'
    Heavy_tank_2 = 'Heavy tank2'
    Heavy_tank_3 = 'Heavy tank3'

    @staticmethod
    def convert_number_to_enemy(number):
        number = int(number)
        if number == 1:
            return EnemyType.Armored_vehicle_1
        if number == 2:
            return EnemyType.Armored_vehicle_2
        if number == 3:
            return EnemyType.Armored_vehicle_3
        if number == 4:
            return EnemyType.Basic_tank_1
        if number == 5:
            return EnemyType.Basic_tank_2
        if number == 6:
            return EnemyType.Basic_tank_3
        if number == 7:
            return EnemyType.Light_tank_1
        if number == 8:
            return EnemyType.Light_tank_2
        return None
