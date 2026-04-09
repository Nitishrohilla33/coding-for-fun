import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# heat equation
# initial conditions
t0,tf = 0,0.01
x0,xL = 0,1
alpha = 1

def f(x,sigma = 0.1):
    return np.exp(-(x-0.5)**2/(2*sigma**2))

# checking if the function is correct or not
#np.linspace(x0,xL,100)
#plt.plot(x,f(x))

x_array = np.linspace(x0,xL,200)
time = np.linspace(t0,tf,10000)

dx = x_array[1] - x_array[0]
dt = time[1] - time[0]

r = alpha * dt / dx**2
print('r =', r) # should be less then 0.5

T = np.zeros((len(x_array),len(time)))
T[0, :],T[-1, :] = 0,0
T[:, 0] = f(x_array)

for j in range(len(time)-1):
    for i in range(1,len(x_array)-1):
        T[i,j+1] = T[i,j] + r*(T[i+1,j]-2*T[i,j]+T[i-1,j]) 
plt.contour(x_array,time,T.T, 50) 
plt.title('contour map')
plt.xlabel('length of rod (x)')
plt.ylabel('Temprature(T)')
plt.show()

    
# Create meshgrid
X, Y = np.meshgrid(x_array, time)

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, T.T)
ax.set_xlabel('length of rod (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Temperature (T)')

plt.show()

plt.figure(figsize=(10,8))
for i in [0,100,200, 500 ,1000,1500,2000,5000,9999]:
    plt.plot(x_array,T[:,i],label = f'time = {i}')
plt.title('Heat transfer in a rod of unit lenght')  
plt.xlabel('length of rod (x)')
plt.ylabel('Temprature(T)')
plt.legend()
plt.show()
