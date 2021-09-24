import pandas as pd
import math
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

def logic(index):
    if (index % 4009 >= 0) and (index % 4009 < 9):
       return True
    return False
    
def graph(x, y, color, xlabel, ylabel, title, name):
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, '.', color=color)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
            
    plt.show()
    fig.savefig(name)

data_1 = pd.read_csv(r'res_indata/0.0001.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_1.columns = ["id", "type", "x", "y", "z", "vx", "vy", "vz"]

data_2 = pd.read_csv(r'res_indata/0.0005.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_2.columns = ["id", "type", "x", "y", "z", "vx", "vy", "vz"]

#print(data_1)
#print(data_2)

t = np.arange(1001)

#r = np.array(np.power((data_1.xu - data_2.xu, 2) + np.power(data_1.yu - data_2.yu, 2) + np.power(data_1.zu - data_2.zu, 2)))

r = np.array(np.power(data_1.x-data_2.x, 2)+np.power(data_1.y-data_2.y, 2)+np.power(data_1.z-data_2.z, 2))
v = np.array(np.power(np.power(data_1.vx - data_2.vx, 2) + np.power(data_1.vy - data_2.vy, 2) + np.power(data_1.vy - data_2.vy, 2), 0.5))

R = np.mean(r.reshape(1001,4000), 1)
V = np.mean(v.reshape(1001,4000), 1)

graph(t, R, "green", r"$\Delta t$", r"$\Delta(r^\prime-r^{\prime\prime})$", "Невязки координат", "res_1.png")
graph(t, V, "green", r"$\Delta t$", r"$\Delta(v^\prime-v^{\prime\prime})$", "Невязки скоростей", "res_2")

