import numpy as np

zeros = np.zeros(5)
range_arr = np.arange(1, 10)
random_arr = np.random.rand(3)

print("Shape of zeros:", zeros.shape)           
print("Shape of range_arr:", range_arr.shape)    
print("Shape of random_arr:", random_arr.shape)  

# Reshape 9 elements into 3 rows and 3 columns
matrix_3x3 = range_arr.reshape(3, 3)
print("New Matrix:\n", matrix_3x3)
print("New Shape:", matrix_3x3.shape)  