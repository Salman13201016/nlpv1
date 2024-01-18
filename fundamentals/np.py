import numpy as np


sample = np.array([1,2,3,4,5])
sample2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i,j in enumerate(sample2.flat):
    pass 


sample3 = np.array([1,2,3,4,5])

res1 = sample / sample3

avg = np.mean(sample3) #mean #variance #root_variance 
std = np.std(sample3)

print(np.argmin(sample3))
print(np.argmax(sample3))
print(std)