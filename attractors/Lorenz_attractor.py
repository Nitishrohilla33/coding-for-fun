import numpy as np
import matplotlib.pyplot as plt

sigma = 10
rho = 28
beta = 8/3

dt = 0.01
t = np.arange(0,20,dt)
n = len(t)

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

np.random.seed(0)
x[0] = np.random.normal(0,1)
y[0] = np.random.normal(0,1)
z[0] = np.random.normal(0,1)

for i in range(n-1):

    # k1
    k1x = sigma*(y[i]-x[i])
    k1y = x[i]*(rho-z[i]) - y[i]
    k1z = x[i]*y[i] - beta*z[i]

    # k2
    x1 = x[i] + 0.5*dt*k1x
    y1 = y[i] + 0.5*dt*k1y
    z1 = z[i] + 0.5*dt*k1z

    k2x = sigma*(y1-x1)
    k2y = x1*(rho-z1) - y1
    k2z = x1*y1 - beta*z1

    # k3
    x2 = x[i] + 0.5*dt*k2x
    y2 = y[i] + 0.5*dt*k2y
    z2 = z[i] + 0.5*dt*k2z

    k3x = sigma*(y2-x2)
    k3y = x2*(rho-z2) - y2
    k3z = x2*y2 - beta*z2

    # k4
    x3 = x[i] + dt*k3x
    y3 = y[i] + dt*k3y
    z3 = z[i] + dt*k3z

    k4x = sigma*(y3-x3)
    k4y = x3*(rho-z3) - y3
    k4z = x3*y3 - beta*z3

    # update
    x[i+1] = x[i] + dt*(k1x + 2*k2x + 2*k3x + k4x)/6
    y[i+1] = y[i] + dt*(k1y + 2*k2y + 2*k3y + k4y)/6
    z[i+1] = z[i] + dt*(k1z + 2*k2z + 2*k3z + k4z)/6

# Plot results
plt.plot(t,x)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()    

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, linewidth = 0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()