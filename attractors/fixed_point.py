import numpy as np
import matplotlib.pyplot as plt

# fixed point attractor 

# RK4 method 
def rk4(x_dot,t,x,h):
    k1 = x_dot(t,x)
    k2 = x_dot(t+h/2,x+k1*h/2)
    k3 = x_dot(t+h/2,x+k2*h/2)
    k4 = x_dot(t+h,x+k3*h)
    return x + h/6(k1+k4+2*(k2+k3))

# differential equation
def x_dot(t,state):
    return np.array([-x])

# time steps 
t0,tf,h = 0,100,0.01
t = np.arange(t0,tf,h)

# intial conditions
state = np.array([5])

# trajectory
x_traj = []

for i in range(len(t)):
    x_traj.append(state[0])
    state = rk4(x_dot=x_dot,t=t,x=state,h=h)

x = np.array(x_traj)

plt.figure()
plt.plot(t,x)
plt.xlabel('t')
plt.ylabel('x')
plt.show()