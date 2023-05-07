# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:01:31 2023

@author: Lab3
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#%% first experiment
theta1 =np.deg2rad(np.array([0,15,30,45,60,75]))
voltage1 = np.array([0.305, 0.291, 0.249,0.186, 0.069,0.003])
cosTheta1 = (np.cos(theta1))**2

# the error rate is 0.001V for the voltage or 5%
            
plt.plot(cosTheta1, voltage1, '*')
plt.show()

#%% second experiment
theta2 =np.deg2rad(np.array([30,45,60,75, 90]))
voltage2 = np.array([ 0.040, 0.119, 0.218, 0.286, 0.304])
cosTheta2 = (np.cos(theta2))**4

plt.plot(cosTheta2, voltage2, '*')
plt.show()

#%% Third Experiment
plateDist90 =np.array([0.045, 0.04, 0.035, 0.03, 0.025, 0.02, 0.0175, 0.015, 0.0125, 0.01])
voltage3 = np.array([0.470, 0.4442, 0.424, 0.416, 0.365, 0.351, 0.307, 0.285, 0.266, 0.235])

plt.plot(plateDist90, voltage3, '*')
plt.show()

#%% 4th Experiment
recieveAngle =np.deg2rad(np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180]))
voltage4 = np.array([0.406, 0.397, 0.327, 0.201, 0.038,0, 0.129, 0.287, 0.374, 0.414 ])

plt.polar(recieveAngle, voltage4, '*')
plt.show()


#%% 5th Expteriment
plateDist0 = np.array([0.01, 0.015, 0.02, 0.025, 0.0225, 0.0175, 0.0125 ])
voltage5 = np.array([0, 0.285,0.448, 0.483, 0.491, 0.421, 0 ])

plt.plot(plateDist0, voltage5, '*')
plt.show()

#%% 6th experiment
#with the plastic divider
distance = np.array([0.015, 0.02, 0.025, 0.0225, 0.0175])
maxDiff = np.array([0.025, 0.019, 0.016, 0.017, 0.021])


divDistance = (1/(2*distance))**2
divMaxDiff = (1/(maxDiff**2))

yReg = linregress(divDistance, divMaxDiff)
print(yReg)
plt.plot(divDistance, divMaxDiff, '*')
plt.show()

#%% 7th experiment 
lamda = 0.028 #[m]
L = 0.16 #[m]
lamdaG = 1/(1/lamda - 3/(4*L))
expectedD = 0.5*np.sqrt((1/lamda**2) - (1/lamdaG**2))

#%% 8th Experiment michelson
distanceMin = np.array([0.68, 0.691, 0.704, 0.719])
voltMin = np.array([0.119, 0.097, 0.086, 0.086])

distanceMax = np.array([0.731, 0.717,0.7, 0.687, 0.672 ])
voltMax = np.array([0.265, 0.261,0.259, 0.261, 0.266 ])

allTogether = np.append(distanceMin, distanceMax)
voltAllTogether = np.append(voltMin, voltMax)
# the error: is millimiter for the distance measurment and 0.001 for volt
plt.plot(allTogether, voltAllTogether, "*")



#%%  Fabri Pro experiment
d1 = 0.038 #voltage at d1 is 0.38
d2Volt = 0.380
minDistance = np.array([0.047, 0.059, 0.073,0.088, 0.101, 0.116,0.130, 0.143,0.158 ])
minVolt = np.array([0.278, 0.278,0.276, 0.277, 0.271, 0.268,0.261, 0.256, 0.258 ])
d2 = 0.167
d2Voltage = 0.392

theory = (d2-d1)/5 
print(theory)

#Second try 
secondD1 = 0.056
secondD1Volt = 0.326
secondMinDistance = np.array([0.063, 0.076, 0.092,0.106, 0.115, 0.131,0.142, 0.160, 0.175 ])
secondMinVoltage = np.array([0.216, 0.216, 0.226, 0.225,0.215,0.218,0.213,0.220, 0.208 ])
secondD2 = 0.183
secondD2Voltage = 0.318
secondTheory = (secondD2-secondD1)/5
print(secondTheory)

#%%Loyd infrometer
d1 = 0.413
h1 = 0.092
h1Voltage = 0.186
aroundH1 = np.array([0.088, 0.085, 0.078, 0.097, 0.106, 0.119])
aroundH1Voltage = np.array([0.193, 0.219, 0.248, 0.194, 0.225, 0.243])
plt.plot(aroundH1, aroundH1Voltage, "*")
plt.show()
h2 = 0.136
h2Voltage = 0.214
aroundH2 = np.array([0.12, 0.126, 0.116, 0.152, 0.146,0.143 ])
aroundH2Voltage = np.array([0.237, 0.224, 0.245, 0.234, 0.229, 0.227])
plt.plot(aroundH2, aroundH2Voltage, "*")
plt.show()

AB1 = np.sqrt(d1**2 +h1**2 )
AB2 = np.sqrt(d1**2 +h2**2 )
lamda = AB2-AB1
print(AB1)
print(AB2)
print(lamda)

#%%Circullar polarization galbo (got linear)
Angle =np.deg2rad(np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]))
voltage = np.array([0.156, 0.049, 0.001, 0.002, 0.032, 0.085, 0.143,0.183, 0.228, 0.237, 0.226, 0.201, 0.133 ])

plt.polar(Angle, voltage, '*')
plt.show()

#%%Circullar polarization galbo 
Angle =np.deg2rad(np.array([0,15, 0]))
voltage = np.array([0,0])

plt.polar(Angle, voltage, '*')
plt.show()


#%%
n=3
lam = 0.028
L =0.15

d = 0.25* np.sqrt(1/((1/2.8**2)-(1/4.83**2)))
print(d)
