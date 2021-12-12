import os

import PySimpleGUI as sg
from PIL import Image

from Utils.Conts import stage_mapper
from Utils.Enums import Difficulty, TowersType
from Utils.Paths import STAGES_PATH


class MapInfoPage:

    def __init__(self):
        pass

    def show_map_info_editor(self, on_finish):
        event, values = sg.Window('Map Editor',
                                  [[sg.Text('Create new Map')],
                                   [sg.Text('Map name'), sg.In(default_text='', key='map_name')],
                                   [sg.Text('Difficulty'),
                                    sg.Combo(Difficulty.list(), default_value='Easy', key='difficulty')],
                                   [sg.Text('Wave count'), sg.In(default_text=10, key='wave_count')],
                                   [sg.Text('Start Health'), sg.In(default_text=10, key='start_health')],
                                   [sg.Text('Start Money'), sg.In(default_text=10, key='start_money')],
                                   [sg.Text('Tower options'), sg.Listbox(
                                       values=TowersType.list(),
                                       select_mode='extended', key='tower_options', size=(30, 6))],

                                   [sg.FileBrowse("Select Map", key='file'), sg.In()],
                                   [sg.Open(), sg.Cancel()]]).read(close=True)

        self._handel_view_events(event,values,on_finish)

    def _handel_view_events(self,event, values,on_finish):
        map_name = values['map_name']
        location = STAGES_PATH + '/' + map_name
        map_location = self._create_folder_and_save_image(location,values['file'])
        dict_json = self._create_stage_json(map_location,
                                           map_name,
                                           values['difficulty'],
                                           int(values['wave_count']),
                                           int(values['start_health']),
                                           int(values['start_money']),
                                           values['tower_options'])

        on_finish(location, map_location, dict_json)

    def _create_folder_and_save_image(self,folder_location,image_path):
        map_location = folder_location + '/map_image.png'
        image = Image.open(image_path)

        if not os.path.exists(folder_location):
            os.mkdir(folder_location)

        image.save(map_location)

        return map_location

    def _create_stage_json(self,map_location, map_name, difficulty, wave_count,start_health,start_money, tower_options):
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
