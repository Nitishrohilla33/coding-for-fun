sigma = 10
rho = 28
beta = 8/3

dt = 0.01
t = np.arange(0,20,dt)
n = len(t)

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

x[0] = 0.1*np.random.randint(0,11)
y[0] = 0.1*np.random.randint(0,11)
z[0] = 0.1*np.random.randint(0,11)

for i in range(n-1):

    # k1
    k1x = sigma*(y[i]-x[i])
    k1y = x[i]*(rho-z[i]) - y[i]
    k1z = x[i]*y[i] - beta*z[i]

    # k2
    x_temp = x[i] + (2/3)*dt*k1x
    y_temp = y[i] + (2/3)*dt*k1y
    z_temp = z[i] + (2/3)*dt*k1z

    k2x = sigma*(y_temp-x_temp)
    k2y = x_temp*(rho-z_temp) - y_temp
    k2z = x_temp*y_temp - beta*z_temp

    # update
    x[i+1] = x[i] + dt*(0.25*k1x + 0.75*k2x)
    y[i+1] = y[i] + dt*(0.25*k1y + 0.75*k2y)
    z[i+1] = z[i] + dt*(0.25*k1z + 0.75*k2z)

plt.figure(dpi = 1500)
plt.plot(t,x)

plt.xlabel("t")
plt.ylabel("x")
plt.show()

plt.figure(dpi = 1500)
plt.plot(y,z, linewidth = 0.8)
plt.xlabel("y")
plt.ylabel("z")
plt.title("Lorenz Attractor Projection", font = 'times new roman')
plt.show()
plt.savefig()
