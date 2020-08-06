import numpy as np 
from matplotlib import pyplot as plt 

# # x = np.arange(1,11) 
# # y = 2 * x + 5 

# y = np.zeros(3)
# #print ("Array with all zeroes:\n",y)

x = np.arange(1,5)
y = np.arange(1,5)
z = np.arange(1,5)

# y[0] = 3
# y[1] = 4
# y[2] = 5
# y[3] = 6

for t in range (0,4):
    y[t] = t+3

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,label = "plot1")
plt.plot(x,z,label = "plot2")
plt.legend() 
plt.show()
