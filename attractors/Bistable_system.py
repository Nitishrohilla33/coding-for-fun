import numpy as np
import matplotlib.pyplot as plt

def x_dot(x):
    return x - x**3

# initial conditions
t0 = 0
x_array = np.arange(-2,2.5,0.5)
print(x_array)

# time steps
dt = 0.0001
steps = 20000

plt.figure(figsize=(10,6))
for x0 in x_array:
    # Trajectories
    x_traj = np.zeros(steps)
    t = np.zeros(steps)
    x = x0
    x_traj[0] = x
    
    for i in range(steps-1):
        x_traj[i+1] = x_traj[i] + x_dot(x)*dt
        t[i+1] = t[i] + dt
        x = x_traj[i+1]


    x_traj = np.array(x_traj)
    t = np.array(t)
    
    plt.plot(t,x_traj,label = f'x(0) = {x0}')
    plt.legend()
plt.title('Bistable System Trajectories')
plt.xlabel('Time')
plt.ylabel('x(t)')
plt.grid()
plt.show()
