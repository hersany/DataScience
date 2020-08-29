#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip show numpy


# In[2]:


pip install numpy


# In[3]:


my_list = [1, 2, 3]


# In[4]:


import numpy as np


# In[5]:


arr = np.array(my_list)


# In[6]:


arr


# In[7]:


my_math = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[8]:


np.array(my_math)


# In[9]:


np.arange(11)       # it is similar range() func. in python. (start,stop,step)


# In[10]:


np.arange(1, 11, 2)


# In[11]:


np.zeros(3)


# In[12]:


np.zeros((2, 5))        # 2 rows, 5 columns


# In[13]:


np.ones(4)              # output has 1 bracket it is 1-D array


# In[14]:


np.ones((3, 2))         # output has 2 brackets it is 2-D array


# In[15]:


np.linspace(2, 3, 5)    # (start, stop, number, some extra parameters...)


# In[16]:


np.linspace(0, 5, 10)


# In[17]:


np.linspace(0, 5, 10, retstep = True)


# In[18]:


np.eye(4)


# In[19]:


np.random.rand(5)       # random between 0 and 1, uniform distribution


# In[20]:


np.random.rand(5, 5)


# In[21]:


np.random.randn(5)       # random around 0, normal distribution


# In[22]:


np.random.randn(4, 4)


# In[23]:


np.random.randint(1,100)      # 1 is inclusive, 100 is exclusive


# In[24]:


np.random.randint(1, 100, 10)


# In[25]:


arr = np.arange(25)
print(arr)


# In[26]:


np.reshape(arr, (5, 5))


# In[27]:


ranarr = np.random.randint(0, 50, 10)
print(ranarr)


# In[28]:


arr.reshape(5, 10)


# In[ ]:


arr.reshape(5, 5)   # we changed it as a 2-D with reshape method


# In[29]:


ranarr


# In[30]:


ranarr.max()


# In[31]:


ranarr.min()


# In[32]:


ranarr.argmax()    # indexing max value in array


# In[33]:


ranarr.argmin()


# In[34]:


arr.shape     # 1-D


# In[35]:


arr


# In[36]:


arr = arr.reshape(5, 5)


# In[37]:


arr.shape       # 2-D


# In[38]:


arr


# In[39]:


arr.dtype          # it gives actual data type 


# In[40]:


from numpy.random import randint


# In[41]:


randint(2, 10)


# In[42]:


# NumPy Indexing and Selection


# In[43]:


import numpy as np


# In[44]:


arr = np.arange(11)


# In[45]:


arr


# In[46]:


arr[8]


# In[47]:


arr[1:5]


# In[48]:


arr[0:5]


# In[49]:


arr[:]


# In[50]:


arr[:6]


# In[51]:


arr[::-1]


# In[52]:


arr[::2]


# In[53]:


arr[0:5] = 100         # broadcast


# In[54]:


arr


# In[55]:


arr = np.arange(11)


# In[56]:


arr


# In[57]:


slice_of_arr = arr[0:6]        # original array does not copied


# In[58]:


slice_of_arr


# In[59]:


slice_of_arr[:] = 99


# In[60]:


slice_of_arr


# In[61]:


arr                         # it changes too


# In[62]:


arr_copy = arr.copy()       # we copied it now the origibal doesnt change


# In[63]:


arr


# In[64]:


arr_copy[:] = 100


# In[65]:


arr_copy


# In[66]:


arr


# In[67]:


arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])


# In[68]:


arr_2d


# In[69]:


arr_2d[0, 0]


# In[70]:


arr_2d[0, 1]


# In[71]:


arr_2d[1, 2]


# In[72]:


arr_2d[0]


# In[73]:


arr_2d[1]


# In[74]:


arr_2d[:2]


# In[75]:


arr_2d[::2]


# In[76]:


arr_2d[:2,1:]


# In[77]:


arr_2d[1:,:2]


# In[78]:


arr = np.arange(1, 11)


# In[79]:


arr


# In[80]:


bool_arr = arr > 5


# In[81]:


bool_arr


# In[82]:


arr[bool_arr]


# In[83]:


arr[arr > 5]


# In[84]:


arr[arr <= 3]


# In[85]:


arr_2d = np.arange(50).reshape(5, 10)


# In[86]:


arr_2d


# In[87]:


arr_2d[1:3,3:5]


# In[88]:


# NumPy Operations


# In[89]:


import numpy as np


# In[90]:


arr = np.arange(11)


# In[91]:


arr


# In[92]:


arr + arr


# In[93]:


arr - arr


# In[94]:


arr * arr


# In[95]:


arr + 100


# In[96]:


arr * 2


# In[97]:


arr ** 2


# In[98]:


arr % 2


# In[99]:


arr / arr           # 0 / 0 gives error normally. numpy just give a warning and gives a nan value


# In[100]:


1 / arr


# In[101]:


np.sqrt(arr)


# In[102]:


np.exp(arr)


# In[103]:


np.max(arr)


# In[104]:


arr.max()


# In[105]:


np.sin(arr)


# In[106]:


arr


# In[107]:


np.log(arr)


# In[108]:


import numpy as np


# In[109]:


arr = np.arange(10)
arr


# In[110]:


print(arr)


# In[111]:


print(type(arr))


# In[112]:


print(type(arr[0]))


# In[113]:


np.full((3, 2), 1)


# In[114]:


np.empty(2, dtype = int)


# In[115]:


np.empty((2, 2))


# In[116]:


np.random.seed(101)
np.random.randint(10, size = 6)


# In[117]:


from skimage import io
photo = io.imread('Sea.jpg')
type(photo)


# In[118]:


photo.shape


# In[119]:


import matplotlib.pyplot as plt
print(plt.imshow(photo))


# In[120]:


plt.imshow(photo[::-1])


# In[121]:


plt.imshow(photo[:, ::-1])


# In[122]:


plt.imshow(photo[:300,:600])


# In[123]:


plt.imshow(photo[::2, ::2])         # resize image /2


# In[124]:


print(np.sum(photo))


# In[125]:


print(np.mean(photo))
print(np.std(photo))
print(np.var(photo))


# In[126]:


a = np.array([9, 5, 1, 7, 3])


# In[127]:


a


# In[128]:


np.sort(a)


# In[129]:


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim)


# In[130]:


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


# In[131]:


arr = np.array([1, 2, 3, 4])

print(type(arr))
print(arr.dtype)


# In[132]:


arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype),
print(type(arr[0]))


# In[133]:


# data types in NumPy
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )


# In[134]:


arr = np.array([1, 2, 3, 4], dtype='U')

print(arr)
print(arr.dtype)
print(type(arr[0]))


# In[135]:


arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

