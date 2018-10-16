#!/usr/bin/python
print("Hello world!")

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 

Fs  =   1000
f   =   10
sample = 1024
t = np.arange(sample)


y = np.sin(2 * np.pi * f * t / Fs)
z = np.cos(2 * np.pi * f * t / Fs)

print(t)
print(y)
plt.subplot(2, 1, 1)
plt.plot(t,y)
plt.subplot(2, 1, 2)
plt.plot(t,z)
plt.show()
