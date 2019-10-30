import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.cos(2*np.pi*x) * np.exp(-x)+0.8
plt.plot(x,y,'k',color='r',label="$exp-decay$",linewidth=3)
plt.axis([0,6,0,1.8])
ix = (x>0.8) & (x<3)
plt.fill_between(x, y ,0, where = ix, \
      facecolor='grey', alpha=0.25)
plt.text(0.5*(0.8+3), 0.2, r"$\int_a^b f(x)\mathrm{d}x$", \
      horizontalalignment='center')
plt.legend()
plt.show()
