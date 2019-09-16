#from matplotlib import pyplot
#import matplotlib
#fig=plt.figure()
'''
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
'''

import matplotlib as mpl
#print(mpl.rcsetup.all_backends)
mpl.use('TkAgg')
import matplotlib.pyplot as plt
print(mpl.get_backend())

squares=[i**2 for i in [1,2,3,4,5]]
plt.plot(squares)

plt.plot(squares,linewidth=5)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()
