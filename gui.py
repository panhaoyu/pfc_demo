import core.environ

core.environ.setup()

import functools
from PySide2 import QtWidgets, shiboken2
import itasca
import importlib
import ui_src.main
from core import make_sample
from core import parallel_bonded, ucs, plot_stress_strain, utils, plot_temp
import statistic.models

itasca.command('python-reset-state false')
dockWidget = itasca.dockWidget('Geo Numerical Demo', '', True)
dockWidget = shiboken2.wrapInstance(int(dockWidget), QtWidgets.QDockWidget)
widget = dockWidget.widget()
importlib.reload(ui_src.main)


def reload(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        importlib.reload(make_sample)
        importlib.reload(parallel_bonded)
        importlib.reload(ucs)
        importlib.reload(plot_stress_strain)
        importlib.reload(utils)
        importlib.reload(statistic.models)
        importlib.reload(plot_temp)
        return func(*args, **kwargs)

    return wrapper


class Window(ui_src.main.Ui_Form, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        self.setWindowTitle(self.tr('Demo GUI Title'))

    @property
    def project(self):
        return statistic.models.Project.objects.get(id=int(self.project_id.text()))

    @reload
    def make_sample(self):
        make_sample.make_sample(self.project)

    @staticmethod
    @reload
    def clear():
        utils.clear()

    @reload
    def parallel_bond(self):
        parallel_bonded.parallel_bonded(self.project)

    @reload
    def ucs(self):
        ucs.ucs(self.project)

    @reload
    def plot_stress_strain(self):
        plot_stress_strain.plot_stress_strain(self.project)

    @reload
    def cycle(self):
        """根据GUI中指定的帧数前进"""
        times = int(self.forward_times.text())
        number = int(self.forward_number.text())
        for i in range(times):
            utils.cycle(self.project, number)

    @reload
    def duplicate(self):
        project = statistic.models.Project.objects.get(id=self.project.id)
        project.pk = None
        project.save()

    @reload
    def go_to_start(self):
        self.project.load_specimen()

    @reload
    def plot_temp(self):
        plot_temp.plot_temp()


window = [Window()]
widget.layout().addWidget(window[0])

dockWidget.show()
dockWidget.raise_()
