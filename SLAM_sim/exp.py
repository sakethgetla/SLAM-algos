import math
import numpy as np
#from pdb import set_trace as bp

## 
#theta = 2*math.pi /100
tr = np.asarray([[2, 4, 5], [6, 3, 7], [0, 0, 1]])
matx = np.random.randint(10, size =(3))

##
print(matx)
#print(matx.T)
print(tr)
#b = np.matmul(matx, tr)
#b = tr*matx
print('')

##
#print((tr*a).T)
#print(tr*matx)
print(np.matmul(tr, matx.transpose()))
print(np.matmul(matx, tr))
## 
