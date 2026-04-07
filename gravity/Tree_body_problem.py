# importing required libraries
import numpy as np
import matplotlib.pyplot as plt


# Random Intial condition generator
def random_initial_conditions(seed = 42):
    np.random.seed(seed)
    # random masses
    m1,m2,m3 = 1,np.random.uniform(0.5,1.5),np.random.uniform(0.5,1.5)
  
    # initial position
    x1,y1 = np.random.uniform(0,1),np.random.uniform(0,1)
    x2,y2 = np.random.uniform(0,1),np.random.uniform(0,1)
    x3,y3 = np.random.uniform(0,1),np.random.uniform(0,1)
    
    # intiial velocities
    v1x,v1y = np.random.uniform(0,1),np.random.uniform(0,1)
    v2x,v2y = np.random.uniform(0,1),np.random.uniform(0,1)
    
    v3x,v3y = -(m1*v1x + m2*v2x)/m3,-(m1*v1y + m2*v2y)/m3
    
    
    
    # print Initial conditions
    initial = [x1, y1, x2, y2, x3, y3,
               v1x, v1y, v2x, v2y, v3x, v3y]

    return m1,m2,m3,initial

# constants
G = 1
eps = 1e-5
seed = 42


# initial conditions
m1,m2,m3,state = random_initial_conditions(seed = seed)

# time and steps 
t = 0
steps = 1460000
dt = 9.49e-06

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
    

    r12 = (dx12**2 + dy12**2 + eps**2)**0.5
    r23 = (dx23**2 + dy23**2 + eps**2)**0.5
    r31 = (dx31**2 + dy31**2 + eps**2)**0.5
    

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

    return [v1x, v1y, v2x, v2y, v3x, v3y,
            a1x, a1y, a2x, a2y, a3x, a3y]

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
    r12 = (dx12**2 + dy12**2 + eps**2)**0.5
    r23 = (dx23**2 + dy23**2 + eps**2)**0.5
    r31 = (dx31**2 + dy31**2 + eps**2)**0.5
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
    if i%100 == 0:
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
# ploting the trajactories in lab frame of reference
plt.figure()
plt.plot(x1_traj,y1_traj, label = 'Star 1')
plt.plot(x2_traj,y2_traj, label = 'Star 2')
plt.plot(x3_traj,y3_traj, label = 'Star 3')
plt.plot(xcom_traj,ycom_traj, label = 'center of mass')
plt.scatter(x = x1_traj[0] ,y = y1_traj[0], label = 'Star 1 intial position')
plt.scatter(x = x2_traj[0] ,y = y2_traj[0], label = 'Star 2 intial position')
plt.scatter(x = x3_traj[0] ,y = y3_traj[0], label = 'Star 3 intial position')
plt.title('3-body problem in lab frame', font = 'times new roman')
plt.xlabel('x',fontsize = 20, font = 'times new roman')
plt.ylabel('y',fontsize = 20, font = 'times new roman')
plt.tight_layout()
plt.legend()
#plt.savefig('3-body_problem_in_lab_frame.png', dpi = 1500)
plt.show()

# ploting the trajactory in their center of mass reference
x1com = np.array(x1_traj) - np.array(xcom_traj)
y1com = np.array(y1_traj) - np.array(ycom_traj)
x2com = np.array(x2_traj) - np.array(xcom_traj)
y2com = np.array(y2_traj) - np.array(ycom_traj)
x3com = np.array(x3_traj) - np.array(xcom_traj)
y3com = np.array(y3_traj) - np.array(ycom_traj)
plt.figure()
plt.plot(x1com, y1com, label = 'star 1')
plt.plot(x2com, y2com, label = 'star 2')
plt.plot(x3com, y3com, label = 'star 3')
plt.scatter(x = x1com[0] ,y = y1com[0], label = 'Star 1 intial position')
plt.scatter(x = x2com[0] ,y = y2com[0], label = 'Star 2 intial position')
plt.scatter(x = x3com[0] ,y = y3com[0], label = 'Star 3 intial position')
plt.title('3-body problem in center of mass frame',font = 'times new roman')
plt.xlabel('x',fontsize = 20, font = 'times new roman')
plt.ylabel('y',fontsize = 20, font = 'times new roman')
plt.tight_layout()
plt.legend()
#plt.savefig('3-body_problem_in_center_of_mass_frame.png', dpi = 1500)
plt.show()

# ploting energy of the system vs time
plt.figure()
plt.plot(time, E)
E0 = E[0]
error = [(e - E0)/E0 for e in E]
plt.plot(time, error)
plt.xlabel('Time',fontsize = 20, font = 'times new roman')
plt.ylabel('Total energy of the system',fontsize = 20, font = 'times new roman')
plt.tight_layout()
#plt.savefig('energy_time_graph.png', dpi = 1500)
plt.show()
