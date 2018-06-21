import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig4, ax = plt.subplots()
x = np.arange(0,2*np.pi,.1)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    
def init():
    line.set_ydata(np.sin(x))
    
ani = animation.FuncAnimation(fig=fig4,func=animate,frames=1000,init_func=init,interval=5,blit=False)
plt.show()
