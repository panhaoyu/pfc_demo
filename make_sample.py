# 这个模块用于生成单轴压缩所需要的模型

import numpy as np
import itasca
from vec import vec2
from itasca import wall, ball, contact
import settings


def make_domain():
    """设置计算区域的大小"""
    domian_min_x = - settings.DOMAIN_EXTEND_CM
    domian_min_y = -settings.DOMAIN_EXTEND_CM
    domain_max_x = settings.SPECIMEN_WIDTH_CM + settings.DOMAIN_EXTEND_CM
    domain_max_y = settings.SPECIMEN_HEIGHT_CM + settings.DOMAIN_EXTEND_CM
    domian_min_x /= 100
    domian_min_y /= 100
    domain_max_x /= 100
    domain_max_y /= 100
    domain_min = (domian_min_x, domian_min_y)
    domain_max = (domain_max_x, domain_max_y)
    itasca.set_domain_min(domain_min)
    itasca.set_domain_max(domain_max)


def make_walls():
    """设置上下、左右边界的墙"""
    width = settings.SPECIMEN_WIDTH_CM / 100
    height = settings.SPECIMEN_HEIGHT_CM / 100
    extend = settings.LOADING_PANEL_CM / 100
    wall_params = [
        # x1, y1, x2, y2
        (-extend, height, width + extend, height, 'top'),  # 上边界
        (-extend, 0, width + extend, 0, 'bottom'),  # 下边界
        (0, 0, 0, height, 'left'),
        (width, 0, width, height, 'right'),
    ]
    commands = [f'{x1}, {y1} {x2}, {y2}, name "{wall_id}"' for x1, y1, x2, y2, wall_id in wall_params]
    [itasca.command(f'wall create vertices {command}') for command in commands]


def set_random():
    """设置随机种子，对于某个随机种子，不同次运行间，其执行结果永远相同"""
    itasca.command('model random 10001')


def set_bound():
    """设置默认的连接模式，具体的含义暂时没看"""
    itasca.command('contact cmat default model linear method deform emod 1.0e9 kratio 0.0')
    itasca.command('contact cmat default property dp_nratio 0.5')


def make_balls():
    porosity = settings.BALL_POROSITY  # 如果调整孔隙度，应该可以进行应力路径的模拟
    radius_min = settings.BALL_RADIUS_MIN_MM / 1000
    radius_max = settings.BALL_RADIUS_MAX_MM / 1000
    x_min, y_min = 0, 0
    x_max, y_max = settings.SPECIMEN_WIDTH_CM / 100, settings.SPECIMEN_HEIGHT_CM / 100
    itasca.command(f'ball distribute '
                   f'porosity {porosity} '
                   f'radius {radius_min} {radius_max} '
                   f'box {x_min} {x_max} {y_min} {y_max}')
    itasca.command(f'ball attribute density 2500 damp 0.7')


def calm_balls():
    """将随机分布的球均布在整个区域内，消除其重叠的部分"""
    # 执行1000次循环，每10次循环进行一次能量清零
    # 这是用于首先将重合的球进行初步的大面积的应力释放
    itasca.command('model cycle 1000 calm 10')
    # 启用时间步长的缩放
    itasca.command('model mechanical timestep scale')
    # 根据各个激活的模块的平均收敛率的平均值判断结束条件
    # 这是用于进一步调整球的位置，将之前残存的能量释放掉
    # 如果只是用model cycle 1000 calm 10，则可能会有一部分地方还有大量的孔洞，收敛也很慢
    itasca.command('model solve ratio-average 1E-4')
    # 重设时间步长为automatic
    itasca.command('model mechanical timestep auto')
    # 清除模型中残存的能量
    itasca.command('model calm')


def delete_extra_walls():
    """删除侧边墙"""
    wall.find('left').delete()
    wall.find('right').delete()


def make_sample():
    make_domain()
    make_walls()
    set_random()
    set_bound()
    make_balls()
    calm_balls()
    delete_extra_walls()
