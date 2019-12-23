import functools
from PySide2 import QtWidgets, shiboken2
import itasca
import importlib
import ui_src.main
import settings
from core import make_sample
from core import parallel_bonded, ucs, plot_stress_strain, utils

itasca.command('python-reset-state false')
dockWidget = itasca.dockWidget('Geo Numerical Demo', '', True)
dockWidget = shiboken2.wrapInstance(int(dockWidget), QtWidgets.QDockWidget)
widget = dockWidget.widget()
importlib.reload(ui_src.main)


def reload(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        importlib.reload(settings)
        importlib.reload(make_sample)
        importlib.reload(parallel_bonded)
        importlib.reload(ucs)
        importlib.reload(plot_stress_strain)
        importlib.reload(utils)
        return func(*args, **kwargs)

    return wrapper


class Window(ui_src.main.Ui_Form, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        self.setWindowTitle(self.tr('Demo GUI Title'))

    @staticmethod
    @reload
    def make_sample():
        make_sample.make_sample()

    @staticmethod
    @reload
    def clear():
        itasca.command('model new')

    @reload
    def save(self):
        name = self.status_name.text()
        utils.save(name)

    @reload
    def parallel_bond(self):
        parallel_bonded.parallel_bonded()

    @reload
    def ucs(self):
        ucs.ucs(self.auto_name.text())

    @reload
    def plot_stress_strain(self):
        plot_stress_strain.plot_stress_strain()

    @reload
    def cycle(self):
        number = int(self.forward_number.text())
        utils.cycle(number)


window = [Window()]
widget.layout().addWidget(window[0])

dockWidget.show()
dockWidget.raise_()
