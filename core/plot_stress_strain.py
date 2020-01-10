# 本模块用于绘制应力-应变曲线
import typing
from matplotlib import pyplot as plt
import statistic.models


def plot_stress_strain(project: statistic.models.Project):
    state_list: typing.List[statistic.models.Statistic] = statistic.models.Statistic.objects.filter(project=project)
    state_list = list(state_list)
    [state.update() for state in state_list if not (state.strain and state.stress)]
    value_list = [(state.strain, state.stress) for state in state_list]
    value_list.sort(key=lambda value: value[0])
    strain_list = [value[0] for value in value_list]
    stress_list = [value[1] for value in value_list]
    plt.plot(strain_list, stress_list)
