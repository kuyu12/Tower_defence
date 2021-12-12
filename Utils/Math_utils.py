import math


def get_degrees(pos1, pos2):
    deltaX = pos2[0] - pos1[0]
    deltaY = pos2[1] - pos1[1]
    degrees_temp = math.atan2(deltaX, deltaY) / math.pi * 180
    if degrees_temp < 0:
        degrees_final = 360 + degrees_temp
    else:
        degrees_final = degrees_temp

    return degrees_final


def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
