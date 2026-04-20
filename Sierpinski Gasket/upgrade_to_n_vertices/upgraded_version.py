import numpy as np
import matplotlib.pyplot as plt

# number of experiments
N = 1000000
# number of verticies 
n = 5
x_vert, y_vert = [],[]
for i in range(n):
    angle = 2*np.pi*i/n
    vertx,verty = np.cos(angle),np.sin(angle)
    x_vert.append(vertx)
    y_vert.append(verty)
# plt.scatter(x_vert,y_vert)  
# plt.show()  
x,y = np.random.uniform(-1,1), np.random.uniform(-1,1)
point_x,point_y = [x],[y]
for i in range(N):
    idx = np.random.randint(0,n)
    x,y = 0.5*(x+x_vert[idx]),0.5*(y+y_vert[idx])
    point_x.append(x)
    point_y.append(y)

plt.plot(point_x,point_y,
        linestyle = ' ',
        marker = ',', 
        markersize = 0.8,
        color = 'k')
plt.axis('equal')
plt.axis('off')
plt.show()