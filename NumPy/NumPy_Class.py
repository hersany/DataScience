#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_list = [1, 2, 3]


# In[3]:


np.array(my_list)


# In[5]:


type(np.array(my_list))


# In[6]:


a = [1, 2, 3, 4]
b = [2, 3, 4, 5]


# In[8]:


np.array(a) * np.array(b)


# In[9]:


my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[10]:


type(my_matrix)


# In[11]:


np.array(my_matrix)


# In[12]:


type(np.array(my_matrix))


# In[13]:


np.arange(0, 10)


# In[16]:


np.arange(0, 11, 2)


# In[20]:


np.arange(10)


# In[21]:


np.zeros(2)


# In[37]:


np.zeros((4, 4), dtype = bool)


# In[43]:


np.zeros((4, 4), dtype = str)


# In[39]:


np.ones((2, 2), dtype = int)


# In[41]:


np.ones(3)


# In[44]:


np.ones((4, 4), dtype = bool)


# In[46]:


np.full((3, 5), 7)


# In[47]:


np.full((3, 5), '7')


# In[54]:


np.linspace(0, 10, 3)


# In[55]:


np.linspace(0, 10)


# In[56]:


len(np.linspace(0, 10))


# In[57]:


np.linspace(0, 10, dtype = int)


# In[58]:


set(np.linspace(0, 10, dtype = int))


# In[60]:


np.linspace(0, 10, dtype = int).reshape(10, 5)


# In[61]:


np.eye(4)


# In[62]:


np.random.rand(5)     # uniform distribution


# In[64]:


np.random.rand(3, 2)


# In[1]:


import matplotlib.pyplot as plt


# In[4]:


plt.hist(np.random.rand(5000))   # uniform distribution
plt.show()


# In[90]:


plt.hist(np.random.rand(50000), bins = 75) 
plt.show()


# In[80]:


np.random.randn(5)        # normal distribution


# In[88]:


np.random.randn(5, 5) 


# In[94]:


plt.hist(np.random.randn(50000))       # normal distribution
plt.show()


# In[99]:


np.random.randn(50000).mean()


# In[5]:


np.random.randn(50000).std()


# In[5]:


np.random.randint(1, 100)


# In[7]:


np.random.randint(100, size = 10)


# In[8]:


np.random.randint(1, 100, 10)


# In[15]:


np.random.randint(1, 100, (2, 2))


# In[7]:


np.random.randint(1, [3, 50, 100])


# In[9]:


np.random.randint(1, [3, 50, 100], (10, 3))


# In[22]:


np.random.randint([3, 50, 100], [5, 60, 120])


# In[10]:


np.random.randint([3, 50, 100], [5, 60, 120], (5, 3))


# In[23]:


arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)


# In[24]:


arr


# In[25]:


ranarr


# In[26]:


arr.reshape(5, 5)


# In[28]:


np.reshape(ranarr, (2, 5))


# In[31]:


ranarr.max()


# In[32]:


ranarr.argmax()


# In[33]:


np.max(ranarr)


# In[34]:


ranarr.min()


# In[35]:


ranarr.argmin()


# In[37]:


arr.ndim


# In[38]:


arr.shape


# In[41]:


arr.reshape(5, 5).shape


# In[39]:


arr.size


# In[40]:


arr.dtype


# In[11]:


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])


# In[13]:


np.concatenate([x, y])


# In[45]:


z = np.array([7, 8, 9])


# In[48]:


np.concatenate([x, y, z])


# In[50]:


a1 = np.concatenate([x, y]).reshape(2, 3)


# In[51]:


a1


# In[54]:


np.concatenate([a1, a1])


# In[55]:


np.concatenate([a1, a1], axis = 1)


# In[56]:


x = np.array([1, 2, 3, 99, 99, 3, 2, 1])


# In[63]:


np.split(x, [3, 5, 7])


# In[70]:


a, b, c, d = np.split(x, [3, 5, 7])


# In[71]:


a


# In[72]:


b


# In[73]:


c


# In[74]:


d


# In[75]:


np.split(x, 4)


# In[16]:


y = np.arange(20).reshape(5, 4)


# In[17]:


y


# In[18]:


np.split(y, 5)


# In[19]:


np.split(y, 4, axis = 1)


# In[20]:


np.vsplit(y, [2,4])


# In[21]:


np.vsplit(y, 5)


# In[22]:


np.split(y, [2, 4])


# In[25]:


np.split(y, [2, 4], axis = 1)


# In[118]:


y


# In[123]:


np.hsplit(y, [3])


# In[125]:


np.hsplit(y, 2)


# In[127]:


left, right = np.hsplit(y, 2)


# In[128]:


left


# In[129]:


right


# In[132]:


upper, lower = np.vsplit(y, [4])


# In[133]:


upper


# In[134]:


lower


# In[140]:


v = np.array([2, 1, 4, 3, 5])
v


# In[141]:


np.sort(v)     # we need to assign a new variable


# In[142]:


v


# In[143]:


v.sort()         # changes


# In[144]:


v


# In[148]:


v2 = np.random.randint(5, 100, (3, 3))


# In[149]:


v2


# In[150]:


np.sort(v2, axis = 0)


# In[151]:


np.sort(v2, axis = 1)


# In[156]:


np.sort(v2)


# In[157]:


arr = np.arange(0, 11)


# In[158]:


arr


# In[159]:


arr[2:4]


# In[160]:


arr[8]


# In[161]:


arr[-1]


# In[163]:


arr[::2]


# In[164]:


arr[0:5] = 100


# In[165]:


arr


# In[166]:


arr = np.arange(11)


# In[167]:


arr


# In[172]:


slice_of_arr = arr[0:6]


# In[173]:


slice_of_arr


# In[176]:


slice_of_arr[:] = 88


# In[177]:


arr


# In[178]:


slice_of_arr


# In[179]:


arr = np.arange(11)


# In[180]:


arr_2 = arr.copy()


# In[181]:


arr_2


# In[182]:


slice_of_arr = arr[0:6]


# In[183]:


slice_of_arr[:] = 77


# In[184]:


arr


# In[185]:


arr_2


# In[27]:


arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
arr_2d


# In[187]:


arr_2d[1]


# In[30]:


arr_2d[1, 0]


# In[192]:


arr_2d[1, 0:1]


# In[193]:


arr_2d[:, 2]


# In[194]:


arr_2d[:, 2:]


# In[195]:


arr_2d[:, 2] = 3


# In[196]:


arr_2d


# In[200]:


v = np.arange(0, 30, 3)


# In[201]:


v


# In[202]:


v[1]


# In[206]:


idx_list = [1, 3, 5]             # fancy indexing


# In[207]:


v[idx_list]                      # fancy indexing


# In[208]:


v[[1, 3, 5]]                     # fancy indexing


# In[210]:


arr_2d = np.zeros((10, 10), dtype = int)


# In[211]:


arr_2d


# In[212]:


arr_2d.shape


# In[213]:


arr_length = arr_2d.shape[1]


# In[215]:


arr_length


# In[216]:


arr_2d[0]


# In[217]:


arr_2d[3]


# In[218]:


for i in range(arr_length):
    arr_2d[i] = i


# In[219]:


arr_2d


# In[220]:


arr_2d[[2, 4, 6, 8]]


# In[221]:


arr_2d[[6, 4, 2, 7]]


# In[3]:


jj = np.arange(1, 17).reshape(4, 4)


# In[4]:


jj


# In[9]:


jj[[1, 3], [2, 3]]              # fancy indexing [axis-0], [axis-1]


# In[226]:


jj[[1, 2], [0, 3]]


# In[227]:


jj


# In[228]:


jj[1, [1, 3]]


# In[230]:


jj [[0, 3], 1]


# In[232]:


jj[0:, [1, 3]]


# In[233]:


arr = np.arange(1, 11)


# In[234]:


arr


# In[235]:


arr > 4


# In[236]:


arr[arr > 4]


# In[242]:


arr[(arr != 3) & (arr != 4)]


# In[250]:


arr[arr % 2 == 0]


# In[251]:


arr = np.arange(11)


# In[252]:


arr + arr


# In[253]:


arr - arr


# In[254]:


arr * arr


# In[255]:


arr ** 2


# In[256]:


arr // arr


# In[257]:


arr / 0


# In[258]:


arr / 1


# In[259]:


arr + 3


# In[260]:


np.exp(arr)


# In[261]:


np.sin(arr)


# In[263]:


np.sin(np.pi/2)


# In[264]:


np.tan(np.pi/4)


# In[ ]:




