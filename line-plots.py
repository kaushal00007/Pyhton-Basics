#import matplotlib
#print(matplotlib.__version__)
#import matplotlib.pyplot as plt
#import numpy as np
#xpoints = np.array([0,6])
#ypoints = np.array([0,256])
#plt.plot(xpoints, ypoints,'o')
#x = np.array([1,2,3,4,5])
#y = np.array([3,8,1,10,20])
#plt.plot(x,y,'o')
#plt.plot(x,y, marker = '*')
#plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(x, y)

plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.show()