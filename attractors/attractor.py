import numpy as np
import matplotlib.pyplot as plt

#parameters
a,b,c = 0.2,0.2,5.7

# RK4 method 
def rk4(f,t,y,h):
    k1 = f(t,y)
    k2 = f(t+h/2,y+k1*h/2)
    k3 = f(t+h/2,y+k2*h/2)
    k4 = f(t+h,y+k3*h)
    return y + h/6*(k1+2*(k2+k3)+k4)

# defining the functions
def f(t,state):
    x,y,z = state
    x_dot,y_dot,z_dot = -y-z,x+a*y,b+z*(x-c)
    return np.array([x_dot,y_dot,z_dot])

# time steps
t0,tf,h = 0,100,0.01
t = np.arange(t0,tf,h)

# initial conditions
state = np.array([1.0,0.0,0.0])

# trajectory
x_traj,y_traj,z_traj = [],[],[]


for i in range(len(t)):
    x_traj.append(state[0])
    y_traj.append(state[1])
    z_traj.append(state[2])
    state = rk4(f=f,t=t,y=state,h=h)

x,y,z = np.array(x_traj),np.array(y_traj),np.array(z_traj)

plt.figure()
plt.plot(x,y)
plt.show()
