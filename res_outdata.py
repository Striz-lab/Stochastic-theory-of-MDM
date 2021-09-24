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
    
data_1 = pd.read_csv(r'res_indata/0.01.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_1.columns = ["id", "type", "xu", "yu", "zu", "vx", "vy", "vz"]

data_2 = pd.read_csv(r'res_indata/0.001.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_2.columns = ["id", "type", "xu", "yu", "zu", "vx", "vy", "vz"]

t = np.arange(1001)

r = np.array(np.power((np.power(data_1.xu - data_2.xu, 2) + np.power(data_1.yu - data_2.yu, 2) + np.power(data_1.zu - data_2.zu, 2)),0.5))
v = np.array(np.power(np.power(data_1.vx - data_2.vx, 2) + np.power(data_1.vy - data_2.vy, 2) + np.power(data_1.vy - data_2.vy, 2), 0.5))

R = np.mean(r.reshape(1001,4000), 1)
V = np.mean(v.reshape(1001,4000), 1)

