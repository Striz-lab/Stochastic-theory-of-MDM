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
    
    #coefs = np.polyfit(x[1:700],y[1:700],1)
    #y_linear = x * coefs[0] + coefs[1]
    
    num_points = len(x)

    min_fit_length = 3

    chi = 0

    chi_min = 24

    j_best = 0
    
    
    for j in range(min_fit_length, len(x)):

        coefs = np.polyfit(x[0:j],y[0:j],1)
        y_linear = x * coefs[0] + coefs[1]
        chi = 0
        for k in range(j):
            chi += (y_linear[k] - y[k])**2
                
        if (chi < chi_min) and (chi > 23):
                
            j_best = j
            chi_min = chi
            #print(chi_min)
            
    coefs = np.polyfit(x[1:j_best],y[1:j_best],1)
    x_linear = x[0:j_best]
    y_linear = x[0:j_best] * coefs[0] + coefs[1]
    
    print(j_best)
    ax.plot(x, y, '.', color=color)
    ax.plot(x_linear, y_linear, '.', color="blue")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    
    plt.show()
    fig.savefig(name)

name1 = input()
name2 = input()


data_1 = pd.read_csv(r'res_indata/'+name1+'.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_1.columns = ["id", "type", "x", "y", "z", "vx", "vy", "vz"]

data_2 = pd.read_csv(r'res_indata/'+name2+'.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_2.columns = ["id", "type", "x", "y", "z", "vx", "vy", "vz"]

t = np.arange(2000)/0.0001

r = np.array(np.power(data_1.x-data_2.x, 2)+np.power(data_1.y-data_2.y, 2)+np.power(data_1.z-data_2.z, 2))
v = np.array(np.power(data_1.vx - data_2.vx, 2) + np.power(data_1.vy - data_2.vy, 2) + np.power(data_1.vz - data_2.vz, 2))

R = np.mean(r.reshape(1001,4000), 1)
V = np.mean(v.reshape(1001,4000), 1)

t = t[100:1000]
R = R[100:1000]
V = V[100:1000]

graph(t, np.log(R), "green", r"$\Delta t$", r"$\ln\Delta(r^\prime-r^{\prime\prime})$", "Невязки координат", "res_1.png")
graph(t, np.log(V), "green", r"$\Delta t$", r"$\ln\Delta(v^\prime-v^{\prime\prime})$", "Невязки скоростей", "res_2")

