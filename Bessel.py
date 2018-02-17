import numpy as np
import matplotlib.pyplot as plt
import scipy.special.cython_special
x=np.linspace(0,20,1000)
y0 = scipy.special.jn(0,x)
y1 = scipy.special.jn(1,x)
y2 = scipy.special.jn(2,x)
y3 = scipy.special.jn(3,x) 
y4 = scipy.special.jn(4,x)
fig,ax = plt.subplots()
ax.plot(x,y0,color='red',label='J0')
ax.plot(x,y1,color='green',label='J1')
ax.plot(x,y2,color='blue',label='J2')
ax.plot(x,y3,color='pink',label='J3')
ax.plot(x,y4,color='black',label='J4')
ax.legend(loc='upper right')
plt.show()
