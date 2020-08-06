# long arrays can be stored in csv files far more efficiently
import numpy as np
import csv

loss = np.zeros((50,3),dtype=np.float)
# epoch = np.zeros(3,50)
# valid = np.zeros(50)
# # uploading arrays in a csv file
for i in range(0,50):
    loss[i,0] = i
    loss[i,1] = i/2
    loss[i,2] = i/4 

# # you can write('w') or append('a')
# with open('first.dat', 'a') as hi_append:
#     np.savetxt(hi_append, np.asarray([epoch]), delimiter='  ')
#     np.savetxt(hi_append, np.asarray([loss]), delimiter='   ')


# result = np.concatenate((epoch, loss, valid))
# print("\nAfter concatenate:")
# print(result)
np.savetxt('losses.dat', loss, delimiter='  ')

print(loss)
# print(epoch)
# print(valid)