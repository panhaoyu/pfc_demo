import django_setup
import statistic.models
from django.db import models
from matplotlib import pyplot as plt


def plot_stress_porosity():
    project_list = statistic.models.Project.objects.filter(id__in=[
        2, 3, 4, 5, 6, 7, 8
    ])
    max_values = [statistic.models.Statistic.objects
                      .filter(project=project).aggregate(models.Max('stress'))['stress__max']
                  for project in project_list]
    porosity = [
        0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04
    ]
    plt.plot(porosity, max_values)
    plt.show()


if __name__ == '__main__':
    plot_stress_porosity()
