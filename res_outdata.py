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
    
def time(x,y):
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
            
    
    print(j_best)

name1 = input()
name2 = input()
    
data_1 = pd.read_csv(r'res_indata/'+name1+'.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_1.columns = ["id", "type", "xu", "yu", "zu", "vx", "vy", "vz"]

data_2 = pd.read_csv(r'res_indata/'+name2+'.txt', skiprows = lambda x: logic(x), sep = " ", header = None)
data_2.columns = ["id", "type", "xu", "yu", "zu", "vx", "vy", "vz"]

t = np.arange(1001)

r = np.array((np.power(data_1.xu - data_2.xu, 2) + np.power(data_1.yu - data_2.yu, 2) + np.power(data_1.zu - data_2.zu, 2)))
v = np.array(np.power(data_1.vx - data_2.vx, 2) + np.power(data_1.vy - data_2.vy, 2) + np.power(data_1.vy - data_2.vy, 2))

R = np.mean(r.reshape(1001,4000), 1)
V = np.mean(v.reshape(1001,4000), 1)

t = t[100:1000]
R = R[100:1000]
V = V[100:1000]

time(t,np.log(R))
time(t,np.log(V))

