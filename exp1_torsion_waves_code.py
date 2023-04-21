# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:41:39 2023

@author: User1
"""
import numpy as np # math functions
import scipy # scientific functions
import matplotlib.pyplot as plt # for plotting figures and setting their properties
import pandas as pd # handling data structures (loaded from files)
from scipy.stats import linregress # contains linregress (for linear regression)
from scipy.optimize import curve_fit as cfit # non-linear curve fitting
from sklearn.metrics import r2_score # import function that calculates R^2 score




m = 0.05 #[kg]
𝐹 = 0.49 #[𝑁] 
l = 0.45 #[m]
alpha = 0.11 #[rad/bar]
deltax=1.27e-2 #[m]
Lbar=0.45 #[m] wide bar
mbar=4.32e-2#[kg] wide bar
n = [1,2,3,4,5,6]
n_prob=[2,3,4,5,6]#stands for n "problematic"
L = 0.92#[m]
K=F*l/(2*alpha)
k=K*deltax**2
I=mbar*Lbar**2/12

v=np.sqrt(k/I)
def wl_held(n):
    wl=[]
    for i in range(len(n)):
        wl.append(L*2/n[i])
    return(wl)
f_held=v/wl_held(n)

f_held_measured=[0.352,0.605,0.858,1.189,1.434,1.680]

slope, intercept, r, p, se = linregress(n,f_held_measured)
linreg_f_held=np.zeros(len(n))
for i in range(len(n)):
    linreg_f_held[i]=(i+1)*slope+intercept
slope=round(slope,3)
intercept=round(intercept,3)
plt.figure()
plt.plot(n,f_held,label='Theoretical Data')
plt.plot(n,f_held_measured,'.',label='Measured Data')
plt.plot(n,linreg_f_held,label='Linear Regression')
plt.text(0.9,1.3,'R²=%a' %round(r**2,4))
plt.text(0.9, 1.2,'y=%a' %(str(slope)+"x+"+str(intercept)))
plt.legend()
plt.ylabel('f(n) [Hz]')
plt.xlabel('n')


def wl_piston(n):
    wl=[]
    for i in range(len(n)):
        wl.append(L*4/(n[i]*2-1))
    return(wl)

f_piston=v/wl_piston(n)

f_piston_measured=[0.427,0.656,0.903,1.206,1.426] #unsuccesful in measurment for n=1

slope, intercept, r, p, se = linregress(n_prob,f_piston_measured)
linreg_f_piston=np.zeros(len(n))
for i in range(len(n)):
    linreg_f_piston[i]=(i+1)*slope+intercept

slope=round(slope,3)
intercept=round(intercept,3)
plt.figure()
plt.plot(n,f_piston,label='Theoretical Data')
plt.plot(n_prob,f_piston_measured,'.',label='Measured Data')
plt.plot(n,linreg_f_piston,label='Linear Regression')
plt.text(0.9,1.05,'R²=%a' %round(r**2,4))
plt.text(0.9,0.95,'y=%a' %(str(slope)+"x+"+str(intercept)))
plt.ylabel('f(n) [Hz]')
plt.xlabel('n')
plt.legend()
