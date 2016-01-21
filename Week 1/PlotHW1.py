import numpy as np
import matplotlib.pylab as plt
x = np.linspace(0, np.pi*6, 101)
sin_wave = plt.plot(x, np.sin(x), 'r-', label='Sin')
cos_wave = plt.plot(x, np.cos(x),'b--', label='Cos')
plt.xlabel('Length')
plt.ylabel('Height')
plt.axis('tight')
plt.legend([sin_wave, cos_wave], ['Sin', 'Cos'])
plt.show()

#Date 1/20/16
#Name Lateef Adetona
