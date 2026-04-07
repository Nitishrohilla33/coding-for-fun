import numpy as np
import matplotlib.pyplot as plt

# Random initial conditions generator
def random_initial_conditions(seed = 42):
    np.random.seed(seed)
    x = np.random.normal(0, 1)
    y = np.random.normal(0, 1)
    z = np.random.normal(0, 1)
    initial = [x, y, z]
    return initial

def derivative(s):
    x, y, z = s
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])

# constants
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# time steps
dt = 0.0025
steps = 20000

# Initial conditions
state1 = random_initial_conditions()
state2 = state1 + np.array([1e-3, 0, 0])  

# trajectories
x1_traj, y1_traj, z1_traj = [state1[0]], [state1[1]], [state1[2]]
x2_traj, y2_traj, z2_traj = [state2[0]], [state2[1]], [state2[2]]

print("Simulating Lorenz attractor...")

for i in range(steps):

    #RK4 method for state1
    k1 = derivative(state1)
    k2 = derivative(state1 + 0.5 * dt * k1)
    k3 = derivative(state1 + 0.5 * dt * k2)
    k4 = derivative(state1 + dt * k3)

    # Update state
    state1 += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    #RK4 method for state2
    k1 = derivative(state2)
    k2 = derivative(state2 + 0.5 * dt * k1)
    k3 = derivative(state2 + 0.5 * dt * k2)
    k4 = derivative(state2 + dt * k3)

    # Update state
    state2 += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    # append trajectories
    if i % 1 == 0:
        x1_traj.append(state1[0])
        y1_traj.append(state1[1])
        z1_traj.append(state1[2])
        x2_traj.append(state2[0])
        y2_traj.append(state2[1])
        z2_traj.append(state2[2])

    if i%max(steps//10, 1) == 0:
        print(f"Progress: {i/steps*100:.1f}%")    
print("Simulation complete. Plotting...")

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x1_traj, y1_traj, z1_traj, lw=0.6, label='Trajectory 1')
ax.plot(x2_traj, y2_traj, z2_traj, lw=0.6, label='Trajectory 2')

ax.scatter(x1_traj[0], y1_traj[0], z1_traj[0], s=40, label='Start 1')
ax.scatter(x2_traj[0], y2_traj[0], z2_traj[0], s=40, label='Start 2')

ax.set_title("Lorenz Attractor (Sensitivity to Initial Conditions)", fontsize=14)
ax.set_xlabel("X", fontsize=11)
ax.set_ylabel("Y", fontsize=11)
ax.set_zlabel("Z", fontsize=11)

ax.set_box_aspect([1,1,1])
ax.grid(True, linestyle='--', alpha=0.5)
ax.view_init(elev=25, azim=135)

ax.legend()

plt.tight_layout()
plt.show()