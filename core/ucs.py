from itasca import wall, ballarray, ballfacetarray
from . import utils
import statistic.models


class UCSLoading(object):
    """进行单轴压缩试验"""

    def __init__(self, project: statistic.models.Project):
        self.project = project

    def set_wall_velocity(self):
        """设置上下墙移动的速度"""
        wall.find('top').set_vel_y(-self.project.top_velocity)
        wall.find('bottom').set_vel_y(self.project.bottom_velocity)

    def set_damp(self):
        """设置加载时的能量耗散率"""
        ballarray.set_damp(ballarray.damp() * 0 + self.project.damp_when_loading)

    def run(self):
        """执行单轴加载过程"""
        self.set_wall_velocity()
        self.set_damp()
        stress_list = list()
        self.project.save_before_load()
        while True:
            utils.cycle(self.project, self.project.cycle_step)
            stress = utils.get_stress_mpa(self.project)
            stress_list.append(stress)
            if stress < max(stress_list) * 0.7:
                break

    @classmethod
    def start(cls, project: statistic.models.Project):
        """加载程序的入口点"""
        ucs_loading = cls(project)
        ucs_loading.run()


ucs = UCSLoading.start
