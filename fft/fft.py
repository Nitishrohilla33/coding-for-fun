import numpy as np
import matplotlib.pyplot as plt

# fft
def fft_(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    if N == 1:
        return x
    
    even = fft_(x[::2])
    odd = fft_(x[1::2])

    factor = np.exp(-2j*np.pi*np.arange(N)/N)

    first_half = even + factor[:N//2]*odd
    second_half = even - factor[:N//2]*odd

    return np.concatenate([first_half,second_half])

# samples 
N = 256

# Frequencies 
f1,f2 = 5,20
a = 1
noise = np.random.normal(0,a,N)


# Time and steps 

t = 0 
tf = 1
dt = tf/N
time = np.arange(t,tf,dt)

# signal
y = np.sin(2*np.pi*f1*time)+0.5*np.sin(2*np.pi*f2*time)   
plt.plot(time,y,label = 'Signal without noise')
y_noise = y + noise
plt.plot(time,y_noise,label = 'Signal with noise')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.legend()
plt.show()

signal = fft_(y_noise)
mag = np.abs(signal)/N

# time to frequency 
fs = 256
freq = np.arange(N)*fs/N - N/2
freq = np.fft.fftshift(freq)
plt.figure()
plt.plot(freq,mag)
plt.title('Fourier space with noise.')
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.show()