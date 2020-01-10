import os
from django.conf import settings
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='项目名', default='无名称')
    specimen_height = models.FloatField(verbose_name='试样高，单位mm', default=150)
    specimen_width = models.FloatField(verbose_name='试样宽，单位mm', default=75)
    domain_extend = models.FloatField(verbose_name='计算区域扩展，单位mm', default=2)
    panel_extend = models.FloatField(verbose_name='荷载板扩展长度，单位mm', default=2)
    ball_radius_min = models.FloatField(verbose_name='最小直径，单位mm', default=3)
    ball_radius_max = models.FloatField(verbose_name='最大直径，单位mm', default=4)
    ball_porosity = models.FloatField(verbose_name='孔隙度', default=0.1)
    ball_count = models.IntegerField(verbose_name='颗粒数，只读', default=0)
    cycle_step = models.IntegerField(verbose_name='加载时的步长', default=1000)
    top_velocity = models.FloatField(verbose_name='上墙下移速度，恒正，单位m/s', default=0.1)
    bottom_velocity = models.FloatField(verbose_name='下墙上移速度，恒正，单位m/s', default=0.1)
    damp_when_loading = models.FloatField(verbose_name='加载时的能量耗散率', default=0.1)
    random_seed = models.IntegerField(verbose_name='随机种子', default=10001)

    @property
    def specimen_path(self):
        return os.path.join(settings.BASE_DIR, 'sav', f'specimen_{self.id}')

    def save_specimen(self):
        from core import utils
        utils.save(self.specimen_path)

    def save_before_load(self):
        from core import utils
        path = os.path.join(settings.BASE_DIR, 'sav', f'before_load_{self.id}')
        utils.save(path)

    def load_specimen(self):
        from core import utils
        utils.restore(self.specimen_path)

    def __str__(self):
        return f'{self.name}-{self.specimen_width}x{self.specimen_height}-{self.ball_radius_min}/{self.ball_radius_max}mm'


class Statistic(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, verbose_name='项目', default=1)
    cycle = models.IntegerField(verbose_name='总循环次数', default=0)
    strain = models.FloatField(verbose_name='总应变', default=0)
    stress = models.FloatField(verbose_name='总应力', default=0)

    @property
    def state_path(self):
        return os.path.join(settings.BASE_DIR, 'sav', f'state_{self.project.id}_{self.cycle}')

    def save_state(self):
        """保存文件到指定的路径"""
        from core import utils
        utils.save(self.state_path)

    def load_state(self):
        from core import utils
        utils.restore(self.state_path)

    def update(self):
        from core import utils
        self.load_state()
        self.strain = utils.get_strain(self.project)
        self.stress = utils.get_stress_mpa(self.project)
        self.save()

    def __str__(self):
        return f'{self.project.name}-{self.cycle}'
