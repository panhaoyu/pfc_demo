import pandas
from django.db import models
from matplotlib import pyplot as plt
from statistic.models import Statistic, Project


def plot_temp():
    """
    用于绘制一些临时的图片
    :return:
    """
    project_list = [
        2, 3, 4, 5, 6, 7, 8
    ]
    project_list = [Project.objects.get(id=project) for project in project_list]
    porosity_list = [project.ball_porosity for project in project_list]
    stress_list = [Statistic.objects.filter(project=project).aggregate(models.Max('stress'))['stress__max']
                   for project in project_list]
    plt.plot(porosity_list, stress_list)
    data = {
        'porosity': porosity_list,
        'stress': stress_list,
    }
    df = pandas.DataFrame(data)
    df.plot()
