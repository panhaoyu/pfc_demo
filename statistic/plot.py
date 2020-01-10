import typing
from . import models
from matplotlib import pyplot as plt


def stress_strain(project_id: int):
    """
    绘制应力-应变曲线
    :param project_id: 项目编号
    :return: 
    """
    obj_list: typing.List[models.Statistic] = models.Statistic.objects.filter(project_id=project_id).all()
    data = [(obj.strain, obj.stress) for obj in obj_list]
    plt.plot([datum[0] for datum in data], [datum[1] for datum in data])
