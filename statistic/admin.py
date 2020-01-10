from django.contrib import admin
from . import models


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Project

    list_display = [
        'id', 'name', 'specimen_width', 'specimen_height', 'ball_radius_min', 'ball_radius_max'
    ]


class StatisticAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Statistic

    list_display = [
        'project', 'cycle', 'stress', 'strain',
    ]


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Statistic, StatisticAdmin)
