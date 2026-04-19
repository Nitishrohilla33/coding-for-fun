import numpy as np
import matplotlib.pyplot as plt


a,b = np.array([0.0,0.0]),np.array([1.0,0.0])
c = np.array([1/2,np.sqrt(3/4)])

# Defining the initial points
y_initial = np.random.uniform(0.0,np.sqrt(3/4))
cot = y_initial/np.tan(np.pi/3)
x_initial = np.random.uniform(0.0 + cot,1.0 - cot)

# time steps 
steps = 100000
x_points,y_points = [x_initial],[y_initial]
for i in range(steps):
    choosing_point = np.random.randint(3)
    if choosing_point == 0:
        x,y = a
    elif choosing_point == 1:
        x,y = b
    else:
        x,y = c
    x_initial,y_initial = (x+x_initial)*0.5,(y+y_initial)*0.5    
    x_points.append(x_initial)
    y_points.append(y_initial)
    
plt.scatter(x_points,y_points,s = 0.01,color = 'k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sierpinski Gasket')
plt.axis('equal')
plt.savefig('Sierpinski',dpi = 1000)
