import itasca
from itasca import wall, ballfacetarray
import statistic.models


def get_stress_mpa(project: statistic.models.Project):
    """获取荷载板的正应力，单位为MPa"""
    width = project.specimen_width / 1000
    top_position = wall.find('top').pos_y()
    bottom_position = wall.find('bottom').pos_y()
    top_position_array = abs(ballfacetarray.pos()[:, 1] - top_position) < 0.001
    bottom_position_array = abs(ballfacetarray.pos()[:, 1] - bottom_position) < 0.001
    top_normal_force = ballfacetarray.force_normal()[top_position_array]
    bottom_normal_force = ballfacetarray.force_normal()[bottom_position_array]
    normal_force_average = (sum(top_normal_force) + sum(bottom_normal_force)) / 2 / 1E6
    stress = normal_force_average / width
    cycle = itasca.cycle()
    if statistic.models.Statistic.objects.filter(project=project, cycle=cycle).count():
        state = statistic.models.Statistic.objects.get(project=project, cycle=itasca.cycle())
        state.stress = stress
        state.save()
    else:
        statistic.models.Statistic.objects.create(project=project, cycle=cycle, stress=stress)
    return stress


def get_strain(project: statistic.models.Project):
    """获取试样的应变"""
    height = project.specimen_height / 1000
    top_position = wall.find('top').pos_y()
    bottom_position = wall.find('bottom').pos_y()
    strain = (height - (top_position - bottom_position)) / height
    cycle = itasca.cycle()
    if statistic.models.Statistic.objects.filter(project=project, cycle=cycle).count():
        state = statistic.models.Statistic.objects.get(project=project, cycle=itasca.cycle())
        state.strain = strain
        state.save()
    else:
        statistic.models.Statistic.objects.create(project=project, cycle=cycle, strain=strain)

    return strain


def cycle(project: statistic.models.Project, number):
    """
    前进给定的帧数
    :param project:
    :param number: 帧数
    :return:
    """
    itasca.command(f'model cycle {number}')
    state, created = statistic.models.Statistic.objects.get_or_create(project=project, cycle=itasca.cycle())
    state.save_state()


def save(path: str):
    """
    将当前状态保存为给定的路径
    :param name: 存档文件的名字
    :return:
    """
    itasca.command(f'model save "{path}"')


def restore(path: str):
    """
    从给定的路径中恢复状态
    :param path: sav文件的路径
    :return:
    """
    itasca.command(f'model restore "{path}"')


def clear():
    """清空模型"""
    itasca.command('model new')
