import numpy as np

seq_a = [1,2,3]
seq_b = [4,5,6]
seq_c = [7,8,9]
seq_d = [10,11,12]

array_abc = np.array([seq_a, seq_b, seq_c, seq_d])
print(array_abc.shape) # 3 rows, 3 columns

# challenge

array_d = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])

print(array_d)
