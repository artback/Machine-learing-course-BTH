import numpy as np
x1 = np.array([2.5, 3.6, 1.2, 0.8, 4.0, 3.4])
x2 = np.array([1.2, 1.0, 1.8, 0.9, 3.0, 2.2])
x3 = np.array([8.0, 15.0, 12.0, 6.0, 8.0, 10.0])
res1 = np.corrcoef(x1, x2)[1,0]
res3 = np.corrcoef(x1, x3)[1,0]
res2 = np.corrcoef(x2, x3)[1,0]
print(res1)
print(res3)
print(res2)



