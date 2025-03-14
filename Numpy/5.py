import numpy as np


row_1 = [1,2,3,4,5]
row_2 = [6,7,8,9,10]
row_3 = [11,12,13,14,15]
row_4 = [16,17,18,19,20]
row_5 = [21,22,23,24,25]

test_data = np.array([row_1,row_2,row_3,row_4,row_5])
print(test_data)

# Using Python Slices
print(test_data[:,2:4:1])
# negative index
print(test_data[:,-2:-4:-1])

# boolean 
greater_than_5 = test_data > 5
print(greater_than_5)
print(test_data[greater_than_5])

# where
drop_under_5_array = np.where(test_data > 5, test_data, 0)
print(drop_under_5_array)

#logical and
drop_under_5_and_over_20 = np.logical_and(test_data > 5, test_data < 20)
print(drop_under_5_and_over_20)

# https://www.youtube.com/watch?v=baLBPuR3Sd4&list=PLc_Ps3DdrcTuf3e-BBpDv8r9jbOB5Wdv-&index=9