# 本模块用于绘制应力-应变曲线
import re
import os
import glob
import itasca
from . import utils
from matplotlib import pyplot as plt


def plot_stress_strain():
    files = glob.glob('sav/ucs_*.sav')
    print(files)
    regex = r'sav\\ucs_(\d+)\.sav'
    regex = re.compile(regex)
    index_list = [regex.match(file).group(1) for file in files]
    index_list = [int(index) for index in index_list]
    index_list.sort()
    strain_list = list()
    stress_list = list()
    for index in index_list:
        itasca.command(f'model restore "sav/ucs_{index}.sav"')
        strain_list.append(utils.calculate_strain())
        stress_list.append(utils.calculate_stress_mpa())
    plt.plot(strain_list, stress_list)
