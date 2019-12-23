from matplotlib import pyplot as plt
import itasca
from itasca import wall, ballarray, ballfacetarray
import settings
from . import utils


def wall_velocity():
    """设置按位移加载的速度"""
    wall.find('top').set_vel_y(-0.1)
    wall.find('bottom').set_vel_y(0.1)
    ballarray.set_damp(ballarray.damp() * 0 + 0.1)


def run(auto_name):
    """
    启动计算
    :param auto_name: 自动保存文件名
    :return:
    """
    stress_list = list()
    index = 1
    while True:
        stress = utils.calculate_stress_mpa()
        stress_list.append(stress)
        if stress < 0.7 * max(stress_list):
            break

        utils.cycle(1000)
        utils.save(auto_name.replace('{{index}}', str(index)))
        index += 1
    return stress_list


def ucs(auto_name='{{index}}'):
    wall_velocity()
    stress_list = run(auto_name)
    plt.plot(stress_list)
