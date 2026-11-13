'''
Title: gradient.py
Author: Nathan Sajdak
Date: 11 November 2026
'''

import numpy as np
import matplotlib.pyplot as plt


saveStatus = False #Turns on plot saving

#Variables
sigma = 1 #m
T_0 = 100 #K
dx = 0.1
dy = 0.1


#Part A
x = np.arange(-3, 3 + dx, dx)
y = np.arange(-3, 3 + dy, dy)

X,Y = np.meshgrid(x, y)

temperature = T_0 * np.exp(-(X**2 + Y**2) / (sigma**2))

plt.figure()
plt.contourf(X, Y, temperature)
plt.xlabel('X Location (m)')
plt.ylabel('Y Location (m)')
plt.title('Heated Plate Tempature Gradient')
plt.colorbar(label='Tempature (K)')
if saveStatus == True:
    plt.savefig('t_plate.png')


#Part B
T = temperature

#Each individual derivative, simply measuring change over each slice.
#Using Central Differencing
dT_dx_CD = (T[1:-1, 2:] - T[1:-1, :-2]) / (2 * dx)
dT_dy_CD = (T[2:, 1:-1] - T[:-2, 1:-1]) / (2 * dy)


#Part C
#Numpy differentiation method
dT_dy_NP, dT_dx_NP = np.gradient(T, dy, dx)
dT_dx_NP = dT_dx_NP[1:-1, 1:-1] #Slices interior points for comparison
dT_dy_NP = dT_dy_NP[1:-1, 1:-1] #Slices interior points for comparison


#Part D
#Analytic differentiation method
dT_dx_AL = -2 * X / sigma**2 * T
dT_dy_AL = -2 * Y / sigma**2 * T
dT_dx_AL = dT_dx_AL[1:-1, 1:-1] #Slices interior points for comparison
dT_dy_AL = dT_dy_AL[1:-1, 1:-1] #Slices interior points for comparison

#Plot comparison along Y=0
y_index = np.argmin(np.abs(y)) - 1 #finds where y=0 in y
x = x[1:-1] #slices x from 61 to 59 objects to match the partial derivatives

plt.figure()
plt.plot(x, dT_dx_CD[y_index, :], 'ko', label='Central Differencing')
plt.plot(x, dT_dx_NP[y_index, :], 'ro', label='numpy.gradient')
plt.plot(x, dT_dx_AL[y_index, :], 'bo', label='Analytical')
plt.title('Comparison of Multiple Differentiation Methods')
plt.xlabel('X Axis at Y=0 (m)')
plt.ylabel('Rate of Temperature Change (K/m)')
plt.legend()
if saveStatus == True:
    plt.savefig('dtdx.png')


#Part D-i
NP_AL_difference = max(abs(dT_dx_NP[y_index, :] - dT_dx_CD[y_index, :]))
print('The maximum absolute difference is: ', NP_AL_difference)


#Part E
plt.figure()
plt.contourf(X, Y, temperature)
plt.colorbar(label='Tempature (K)')

step = 5 #sets arror step to 5
dT_dy_NP, dT_dx_NP = np.gradient(T, dy, dx) #unslices the boundary points

#Quiver plot
plt.quiver(
    X[::step, ::step], Y[::step, ::step],
    -dT_dx_NP[::step, ::step], -dT_dy_NP[::step, ::step],
    color='red', scale=2000, width=0.004
    )
plt.xlabel('X Location (m)')
plt.ylabel('Y Location (m)')
plt.title('Heat Flow Direction')
if saveStatus == True:
    plt.savefig('heat_flow.png')

