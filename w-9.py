#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
array=np.empty([4,2],dtype=np.uint16)
print("printing an array=",array)
print("printing the attributes of the array=")
print("1.shape",array.shape)
print("2.dimension=",array.ndim)
print("3.size=",array.itemsize)


# # np.empty([4,2],dtype=np.uint16) 

# In[2]:


import numpy as np
n = 3
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(M)
flattened_M = M.flatten()
print("Converted matrix into a 1-dimensional array")
print(flattened_M)
mean_M = np.mean(flattened_M)
std_M = np.std(flattened_M)
z = (flattened_M - mean_M) / std_M
mean_z = np.mean(z)
std_z = np.std(z)
print("Mean of M: ", mean_M)
print("Mean of z: ", mean_z)
print("Standard deviation of M: ", std_M)
print("Standard deviation of z: ", std_z)


# # # Print max from axis 0 and min from axis 1 from the 2-D array.

# In[24]:


import numpy as np
arr1=np.array([[1,2,3],[44,65,32],[65,12,7]])
print(arr1)
min1=np.amin(arr1,1)
print(min1)
max1=np.amax(arr1,0)
print(max1)


# ## Create a function which creates an n×n array with (i,j) - entry equal to i+j. 

# In[28]:


import numpy as np
def create_array(n):
    return [[i + j for j in range(n)] for i in range(n)]
print(create_array(3))

