#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# In[3]:


array=np.arange(10,51,2)
print(array)


# In[14]:


x=np.array([1,2,3,4,4,5,4,6])
print("original array:")
print(x)
y=np.bincount(x)
maximum=max(y)
for i in range (len(y)):
    if y[i]==maximum:
        print("the frequent value in the array is=")
print(i)


# In[4]:


import numpy as np
import time
mat_1 = np.random.rand(100, 100)
mat_2 = np.random.rand(100, 100)
start = time.time()
result_np = np.dot(mat_1, mat_2)
end = time.time()
print("Time taken by np.dot:", end - start)
result_loops = np.zeros((100, 100))
start = time.time()
for i in range(100):
    for j in range(100):
        for k in range(100):
            result_loops[i][j] += mat_1[i][k] * mat_2[k][j]
end = time.time()
print("Time taken by for-loops:", end - start)
print("Are the results equal? =", np.allclose(result_np, result_loops))


# In[12]:


import numpy as np 
arr=np.array([12,22,34,54,66,11])     #nearest value
print("array is:",arr)
x= 65
print("the value which is nearest to the =",x)
diff_array=np.absolute(arr-x)
print("the nearest element is=",arr[index])

