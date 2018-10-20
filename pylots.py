import numpy as np
import matplotlib.pyplot as plt

length = 1000
periods = 5
time = np.arange(0,length,1)

#add noise

r = 1 # I just chose any numbers
w = 10
m = 2
t = 0.1
a = np.sqrt(m/(t*w*w*2))*np.exp(-r)

amplitude = a*a-np.sinh(r)**2

std_z = np.sqrt(np.exp(-2*r)/(4*w*w*a*a)+w*w*t*t/(m*m)*a*a*np.exp(2*r))

signal = np.zeros(shape= length)

for i in range(length):
    signal[i] = amplitude*np.cos(2.*np.pi*i*periods/length) + np.random.normal(0,std_z,1) # add noise

f, (ax1, ax2,ax3,ax4) = plt.subplots(1, 4)

ax1.plot(time,signal,'ro')
ax1.set_title("optimal alpha, m=2")

a = a*10
std_z = np.sqrt(np.exp(-2*r)/(4*w*w*a*a)+w*w*t*t/(m*m)*a*a*np.exp(2*r))

for i in range(length):
    signal[i] = amplitude*np.cos(2.*np.pi*i*periods/length) + np.random.normal(0,std_z,1) # add noise


ax2.plot(time,signal,'ro')
ax2.set_title("not optimal alpha, m=2")

m = 20
a = np.sqrt(m/(t*w*w*2))*np.exp(-r)
std_z = np.sqrt(np.exp(-2*r)/(4*w*w*a*a)+w*w*t*t/(m*m)*a*a*np.exp(2*r))

for i in range(length):
    signal[i] = amplitude*np.cos(2.*np.pi*i*periods/length) + np.random.normal(0,std_z,1) # add noise

ax3.plot(time,signal,'ro')
ax3.set_title("optimal alpha, m=20")

a = a*10
std_z = np.sqrt(np.exp(-2*r)/(4*w*w*a*a)+w*w*t*t/(m*m)*a*a*np.exp(2*r))

for i in range(length):
    signal[i] = amplitude*np.cos(2.*np.pi*i*periods/length) + np.random.normal(0,std_z,1) # add noise

ax4.plot(time,signal,'ro')
ax4.set_title("not optimal alpha, m=20")

plt.show()