import pandas as pd
import math
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from scipy.fft import fft, ifft

def logic(index):
    if (index % 4009 >= 0) and (index % 4009 < 9):
       return True
    return False
    
def graph(x, y, color, xlabel, ylabel, title, name):
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, '.', color=color)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    #ax.set_xlabel(xlabel)
    #ax.set_ylabel(ylabel)
    #ax.set_title(title)
    
    plt.show()
    fig.savefig(name)
    
name = input()

data = pd.read_csv(name+'.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data.columns = ["id", "type","fx", "fy", "fz"]

t = np.arange(1001)
#T = np.arange(500)
#x = np.exp(np.abs(T))*np.cos(T)
f = np.array(np.power(data.fx, 2) + np.power(data.fy, 2) + np.power(data.fz, 2))
f = np.mean(f.reshape(1001,4000), 1)

graph(t[10:1000], ifft(fft(f)[10:1000]), "green", r"$\Delta t$", r"<F>", "Флуктуация сил", "Sp2.png")
