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
dt = 0.001
t = 0.0
steps = 100000

# Initial conditions
state = random_initial_conditions()

# trajectories
x_traj, y_traj, z_traj = [state[0]], [state[1]], [state[2]]

print("Simulating Lorenz attractor...")

for i in range(steps):

    #RK4 method
    k1 = derivative(state)
    k2 = derivative(state + 0.5 * dt * k1)
    k3 = derivative(state + 0.5 * dt * k2)
    k4 = derivative(state + dt * k3)

    # Update state
    state += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    # append trajectories
    if i % 1 == 0:
        x_traj.append(state[0])
        y_traj.append(state[1])
        z_traj.append(state[2])

    if i%max(steps//10, 1) == 0:
        print(f"Progress: {i/steps*100:.1f}%")    
print("Simulation complete. Plotting...")

# Plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_traj, y_traj, z_traj, color='black', lw=0.5)
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()