import os
import settings
import itasca
from itasca import wall, ballfacetarray


def calculate_stress_mpa():
    """获取荷载板的正应力，单位为MPa"""
    width = settings.SPECIMEN_WIDTH_CM / 100
    top_position = wall.find('top').pos_y()
    bottom_position = wall.find('bottom').pos_y()
    top_position_array = abs(ballfacetarray.pos()[:, 1] - top_position) < 0.001
    bottom_position_array = abs(ballfacetarray.pos()[:, 1] - bottom_position) < 0.001
    top_normal_force = ballfacetarray.force_normal()[top_position_array]
    bottom_normal_force = ballfacetarray.force_normal()[bottom_position_array]
    normal_force_average = (sum(top_normal_force) + sum(bottom_normal_force)) / 2 / 1E6
    return normal_force_average / width


def calculate_strain():
    """获取试样的应变"""
    height = settings.SPECIMEN_HEIGHT_CM / 100
    top_position = wall.find('top').pos_y()
    bottom_position = wall.find('bottom').pos_y()
    strain = (height - (top_position - bottom_position)) / height
    return strain


def cycle(number: int):
    """
    前进给定的帧数
    :param number: 帧数
    :return:
    """
    itasca.command(f'model cycle {number}')


def save(name: str):
    """
    将当前状态保存为给定的名字，不支持子路径
    :param name: 存档文件的名字
    :return:
    """
    path = os.path.join(settings.SAV_PATH, f'{name}.sav')
    itasca.command(f'model save "{path}"')
