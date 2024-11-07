import json
import sys

import pygame

from Tower_defence.Tools.New_Map_Editor.map_info_page import MapInfoPage
from Tower_defence.Tools.New_Map_Editor.map_path_page import MapPathPage
from Tower_defence.Tools.New_Map_Editor.map_selection_page import MapSelectionAreaPage


def save_json(stage_location, dict_json):
    with open(stage_location + '/stage_data.json', 'w') as f:
        json.dump(dict_json, f)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    map_info_page = MapInfoPage()
    map_selection_editor = MapSelectionAreaPage()
    map_path_editor = MapPathPage()

    map_info_page.show_map_info_editor(
        lambda location, map_location, dict_json:
        map_selection_editor.show_map_selection_editor(location, map_location, dict_json,
                                                       lambda location, map_location, dict_json:
                                                       map_path_editor.show_map_path_editor(location, map_location,
                                                                                            dict_json,
                                                                                            lambda stage_location,
                                                                                                   dict_json:
                                                                                            save_json(stage_location,
                                                                                                      dict_json)
                                                                                            )
                                                       )
    )
