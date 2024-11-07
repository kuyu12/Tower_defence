from Utils.Enums import TowersType, EnemyType
from Utils.Paths import TOWER_IMAGES_PATH, ENEMY_IMAGES_PATH

MAP_SIZE = (1200, 650)
PANEL_SIZE = (200, 650)
SCREEN_SIZE = (1400, 650)
TOWER_BUTTON_SIZE = (64,64)
GRID_BLOCK_SIZE = int(MAP_SIZE[0] / 20)
ENEMY_SIZE = (45,45)
ENEMY_MIN_WAVE_TIME = 300
ENEMY_MAX_WAVE_TIME = 1000
TOWER_INFO_SIZE = (300,200)
EXPLOSION_SIZE = (100,100)
HEALTH_BAR_SIZE = (50,8)

# Stage
stage_mapper = {
    'map_path': 'map_location',
    'map_name': 'name',
    'stage_difficulty': 'difficulty',
    'wave_count': 'wave_count',
    'wave_data' : 'wave_data',
    'tower_sprits': 'tower_options',
    'start_health': 'start_health',
    'start_money': 'start_money',
    'board_matrix' : 'board_matrix',
    'paths':'paths'
}

TOWERS_DATA = {
    TowersType.Vulcan.name: {
        'damage': 7,
        'shot_speed': 60,
        'upgrade': 2,
        'upgrade_price': 20,
        'range': 150,
        'price': 50,
        'image_url': TOWER_IMAGES_PATH + '/Vulcan.png'
    },
    TowersType.Howitzer.name: {
        'damage': 10,
        'shot_speed': 55,
        'upgrade': 1,
        'upgrade_price': 30,
        'range': 150,
        'price': 70,
        'image_url': TOWER_IMAGES_PATH + '/Howitzer.png'
    },
    TowersType.Anti_Tank.name: {
        'damage': 12,
        'shot_speed': 110,
        'upgrade': 6,
        'upgrade_price': 70,
        'range': 160,
        'price': 150,
        'image_url': TOWER_IMAGES_PATH + '/Anti_Tank.png'
    },
    TowersType.Beaufort.name: {
        'damage': 12,
        'shot_speed': 55,
        'upgrade': 10,
        'upgrade_price': 50,
        'range': 150,
        'price': 120,
        'image_url': TOWER_IMAGES_PATH + '/Beaufort.png'
    },
    TowersType.Mortar.name: {
        'damage': 15,
        'shot_speed': 50,
        'upgrade': 13,
        'upgrade_price': 100,
        'range': 180,
        'price': 180,
        'image_url': TOWER_IMAGES_PATH + '/Mortar.png'
    },
    TowersType.Laser.name: {
        'damage': 17,
        'shot_speed': 60,
        'upgrade': 10,
        'upgrade_price': 130,
        'range': 150,
        'price': 220,
        'image_url': TOWER_IMAGES_PATH + '/Laser.png'
    },
    TowersType.Armor_piercing.name: {
        'damage': 50,
        'shot_speed': 160,
        'upgrade': 8,
        'upgrade_price': 150,
        'range': 200,
        'price': 250,
        'image_url': TOWER_IMAGES_PATH + '/Armor_piercing.png'
    },
    TowersType.Garival.name: {
        'damage': 60,
        'shot_speed': 80,
        'upgrade': 10,
        'upgrade_price': 200,
        'range': 100,
        'price': 300,
        'image_url': TOWER_IMAGES_PATH + '/Garival.png'
    },
}

ENEMY_DATA = {
    EnemyType.Armored_vehicle_1.name: {
        'health': 40,
        'speed': 15,
        'image_url': ENEMY_IMAGES_PATH + '/Armored_vehicle_1.png',
        'worth_money': 7
    },
    EnemyType.Armored_vehicle_2.name: {
        'health': 70,
        'speed': 15,
        'image_url': ENEMY_IMAGES_PATH + '/Armored_vehicle_2.png',
        'worth_money': 7
    },
    EnemyType.Armored_vehicle_3.name: {
        'health': 40,
        'speed': 4,
        'image_url': ENEMY_IMAGES_PATH + '/Armored_vehicle_3.png',
        'worth_money': 10
    },
    EnemyType.Basic_tank_1.name: {
        'health': 100,
        'speed': 12,
        'image_url': ENEMY_IMAGES_PATH + '/Basic_tank_1.png',
        'worth_money': 13
    },
    EnemyType.Basic_tank_2.name: {
        'health': 120,
        'speed': 10,
        'image_url': ENEMY_IMAGES_PATH + '/Basic_tank_2.png',
        'worth_money': 15
    },
    EnemyType.Basic_tank_3.name: {
        'health': 150,
        'speed': 10,
        'image_url': ENEMY_IMAGES_PATH + '/Basic_tank_3.png',
        'worth_money': 20
    },
    EnemyType.Light_tank_1.name: {
        'health': 170,
        'speed': 7,
        'image_url': ENEMY_IMAGES_PATH + '/Light_tank_1.png',
        'worth_money': 25
    },
    EnemyType.Light_tank_2.name: {
        'health': 200,
        'speed': 6,
        'image_url': ENEMY_IMAGES_PATH + '/Light_tank_2.png',
        'worth_money': 30
    },
    EnemyType.Medium_tank.name: {
        'health': 220,
        'speed': 58,
        'image_url': ENEMY_IMAGES_PATH + '/Medium_tank.png',
        'worth_money': 40
    },
    EnemyType.Heavy_tank_1.name: {
        'health': 250,
        'speed': 4,
        'image_url': ENEMY_IMAGES_PATH + '/Heavy_tank_1.png',
        'worth_money': 40
    },
    EnemyType.Heavy_tank_2.name: {
        'health': 750,
        'speed': 18,
        'image_url': ENEMY_IMAGES_PATH + '/Heavy_tank_2.png',
        'worth_money': 80
    },
    EnemyType.Heavy_tank_3.name: {
        'health': 300,
        'speed': 6,
        'image_url': ENEMY_IMAGES_PATH + '/Heavy_tank_3.png',
        'worth_money': 100
    }
}
