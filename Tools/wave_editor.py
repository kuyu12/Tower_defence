import json
import os
import sys

import PySimpleGUI as sg
from PIL import Image

from Utils.Conts import stage_mapper
from Utils.Enums import Difficulty, TowersType
from Utils.Paths import STAGES_PATH

def show_wave_entry_editor():
    event, values = sg.Window('Wave Editor',
                              [[sg.Text('Create wave')],
                               [sg.Text('Stage name'), sg.In(default_text='', key='stage_name')],
                               [sg.Open()]]).read(close=True)

    handel_entry_events(event,values)

def show_wave_editor(wave_count,location):
    layout = [[sg.Text('Create wave')]]
    for wave in range(wave_count):
        layout.append([sg.Text('Wave '+str(wave)),sg.In(default_text='', key='enemy_numbers_'+str(wave)),sg.In(default_text='', key='enemy_counts_'+str(wave))])
    layout.append([sg.Open()])
    event, values = sg.Window('Wave Editor',layout).read(close=True)
    handel_events(event, values,location,wave_count)

def handel_entry_events(event, values):
    stage_name = values['stage_name']
    location = STAGES_PATH + '/' + stage_name

    if not os.path.exists(location):
        print("STAGE NAME ISN'T EXISTS")
        return

    with open(location + '/stage_data.json') as f:
        stage_data = json.load(f)

    wave_count = stage_data[stage_mapper['wave_count']]
    show_wave_editor(wave_count,location)


def handel_events(event, values,location,wave_count):
    json_dict = {}
    for wave in range(wave_count):
        enemys_str = values['enemy_numbers_'+str(wave)]
        enemys_counts = values['enemy_counts_' + str(wave)]
        enemys = enemys_str.split(',')
        counts = enemys_counts.split(',')
        wave_json = {}
        if enemys_str == '':
            continue

        for index,enemy in enumerate(enemys):
            wave_json[enemy] = counts[index]
        json_dict[wave] = wave_json

    with open(location + '/wave_data.json', 'w') as f:
        json.dump(json_dict, f)

    sys.exit()

def _create_stage_json(map_location, map_name, difficulty, wave_count,start_health,start_money, tower_options):
    dict_json = {
        stage_mapper['map_path']: map_location,
        stage_mapper['map_name']: map_name,
        stage_mapper['stage_difficulty']: difficulty,
        stage_mapper['wave_count']: wave_count,
        stage_mapper['start_health']: start_health,
        stage_mapper['start_money']: start_money,
        stage_mapper['tower_sprits']: tower_options
    }

    return dict_json


if __name__ == '__main__':
    show_wave_entry_editor()