import numpy as np
import matplotlib.pyplot as plt
# Random Intial condition generator
def rendom_initial_conditions()

  # initial position
  x1 = 0.1*np.random.randint(0,11)
  y1 = 0.1*np.random.randint(0,11)
  x2 = 0.1*np.random.randint(0,11)
  y2 = 0.1*np.random.randint(0,11)
  x3 = 0.1*np.random.randint(0,11)
  y3 = 0.1*np.random.randint(0,11)
  
  # intiial velocities
  v1x = 0.1*np.random.randint(0,11)
  v1y = 0.1*np.random.randint(0,11)
  v2x = 0.1*np.random.randint(0,11)
  v2y = 0.1*np.random.randint(0,11)
  v3x = 0.1*np.random.randint(0,11)
  v3y = 0.1*np.random.randint(0,11)
  
  
  
  # print Initial conditions
  initial = [x1, y1, x2, y2, x3, y3,
             v1x, v1y, v2x, v2y, v3x, v3y]

return initial

# constants
G = 1

# Masses
m1 = 1
m2 = 0.3375170104670978
m3 = 0.5634863023824473

# state = [x1, y1, x2, y2, x3, y3, v1x, v1y, v2x, v2y, v3x, v3y]
state = initial

# time and steps 
t = 0
steps = 1460000
dt = 9.5e-06

# trajectories
x1_traj, y1_traj = [], []
x2_traj, y2_traj = [], []
x3_traj, y3_traj = [], []
xcom_traj, ycom_traj = [], []
E, time = [], []

def derivatives(s):
    x1, y1, x2, y2, x3, y3, v1x, v1y, v2x, v2y, v3x, v3y = s

    dx12 = x2 - x1
    dx23 = x3 - x2
    dx31 = x1 - x3
    dy12 = y2 - y1
    dy23 = y3 - y2
    dy31 = y1 - y3
    
    r12 = (dx12**2 + dy12**2)**0.5
    r23 = (dx23**2 + dy23**2)**0.5
    r31 = (dx31**2 + dy31**2)**0.5
    

    # forces
    Fx1 = G*m1*m2*dx12/(r12**3) - G*m3*m1*dx31/(r31**3)
    Fy1 = G*m1*m2*dy12/(r12**3) - G*m3*m1*dy31/(r31**3)
    Fx2 = - G*m1*m2*dx12/(r12**3) + G*m2*m3*dx23/(r23**3)
    Fy2 = - G*m1*m2*dy12/(r12**3) + G*m2*m3*dy23/(r23**3)
    Fx3 = G*m3*m1*dx31/(r31**3) - G*m2*m3*dx23/(r23**3)
    Fy3 = G*m3*m1*dy31/(r31**3) - G*m2*m3*dy23/(r23**3)
    

    # acceleration
    a1x = Fx1/m1
    a1y = Fy1/m1
    a2x = Fx2/m2
    a2y = Fy2/m2
    a3x = Fx3/m3
    a3y = Fy3/m3

    return [v1x, v1y, v2x, v2y, v3x, v3y, a1x, a1y, a2x, a2y, a3x, a3y]

print('Starting simulation....\nLoading...')
for i in range(steps):

    # RK4 steps
    k1 = derivatives(state)

    k2 = derivatives([s + dt/2 * k for s, k in zip(state, k1)])

    k3 = derivatives([s + dt/2 * k for s, k in zip(state, k2)])

    k4 = derivatives([s + dt * k for s, k in zip(state, k3)])

    # update state
    state = [s + dt/6 * (k1_i + 2*k2_i + 2*k3_i + k4_i)
        for s, k1_i, k2_i, k3_i, k4_i in zip(state, k1, k2, k3, k4)]

    x1, y1, x2, y2, x3, y3, v1x, v1y, v2x, v2y, v3x, v3y = state

    
    # time and energy
    
    dx12 = x2 - x1
    dx23 = x3 - x2
    dx31 = x1 - x3
    dy12 = y2 - y1
    dy23 = y3 - y2
    dy31 = y1 - y3
    r12 = (dx12**2 + dy12**2)**0.5
    r23 = (dx23**2 + dy23**2)**0.5
    r31 = (dx31**2 + dy31**2)**0.5
    # velocity squared
    v1_sqre = v1x**2 + v1y**2
    v2_sqre = v2x**2 + v2y**2
    v3_sqre = v3x**2 + v3y**2
    
    t += dt
    energy = -G*(m1*m2/r12 + m1*m3/r31 + m2*m3/r23) + 0.5*(m1*v1_sqre + m2*v2_sqre + m3*v3_sqre)


    # center of mass
    xcom = (m1*x1 + m2*x2 + m3*x3)/(m1 + m2 + m3)
    ycom = (m1*y1 + m2*y2 + m3*y3)/(m1 + m2 + m3)

  
    # append trajectories
    x1_traj.append(x1)
    y1_traj.append(y1)
    x2_traj.append(x2)
    y2_traj.append(y2)
    x3_traj.append(x3)
    y3_traj.append(y3)
    xcom_traj.append(xcom)
    ycom_traj.append(ycom)
    # total mechanical energy
    E.append(energy)
    time.append(t)
    if i%max(1,steps//10)==0:
        print('.',end = '')
print('\nSimulation is ready to plot.')
