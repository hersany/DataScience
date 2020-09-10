#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.zeros(10)


# In[3]:


np.ones(10)


# In[5]:


np.ones(10) * 5


# In[6]:


np.arange(10, 51)


# In[7]:


np.arange(10, 51, 2)


# In[8]:


np.arange(9).reshape(3, 3)


# In[9]:


np.eye(3)


# In[14]:


from numpy.random import rand
rand(1)


# In[15]:


from numpy.random import randn
randn(25)


# In[24]:


np.arange(1, 101).reshape(10, 10) / 100


# In[25]:


np.linspace(0, 1, 20)


# In[27]:


mat = np.arange(1, 26).reshape(5, 5)
mat


# In[28]:


mat[2:,1:]


# In[29]:


mat[3, 4]


# In[31]:


mat[:3,1:2]


# In[53]:


mat[4]


# In[34]:


mat[3:]


# In[36]:


np.sum(mat)


# In[38]:


np.std(mat)


# In[51]:


np.sum(mat, axis = 0)


# In[1]:


########LAB#########


# In[2]:


import numpy as np


# In[3]:


a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])


# In[4]:


a


# In[5]:


b


# In[28]:


np.linalg.multi_dot(b)


# In[9]:


x = np.arange(1, 11)


# In[10]:


x


# In[11]:


y = np.arange(-1, 1, 0.2)


# In[12]:


y


# In[13]:


np.linspace(0, 10, 25)


# In[20]:


np.logspace(0, 10, 10, base = 2)


# In[30]:


np.random.seed(0)
np.random.rand(5, 5)        # uniform distribution


# In[31]:


np.random.rand(5, 5)


# In[32]:


np.random.rand(5, 5)


# In[33]:


np.random.seed(0)
np.random.rand(5, 5)


# In[34]:


np.random.randn(3, 3)       # normal distribution


# In[36]:


np.diag([1, 2, 3, 4])      # diagonal matrix


# In[37]:


np.diag([1, 2, 3, 4], k = -1)    # default k = 0


# In[38]:


np.diag([1, 2, 3, 4], k = 1)


# In[41]:


np.eye(4, k = -1)


# In[42]:


np.eye(4)


# In[43]:


d = np.array([i for i in range(5)])


# In[44]:


d


# In[45]:


row_mask = np.array([True, False, True, False, False])   # np.arrays are homogeneous.


# In[46]:


d[row_mask]


# In[47]:


row1_mask = np.array([0, 0, 0, 1, 1], dtype = bool)


# In[49]:


d[row1_mask]


# In[54]:


x = np.arange(0, 10, 0.5)


# In[55]:


x


# In[56]:


mask = (5 < x) & (x < 7.5)


# In[59]:


mask


# In[57]:


x[mask]


# In[58]:


x[(5 < x) & (x < 7.5)]


# In[62]:


indices = np.where(mask)


# In[63]:


indices


# In[64]:


np.where(mask)


# In[65]:


x[indices]


# In[67]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]])


# In[68]:


a


# In[70]:


np.diag(a)


# In[71]:


np.diag(a, k = 1)


# In[75]:


np.diag(a, k = 3)


# In[76]:


arr = np.arange(-3, 3)


# In[77]:


arr


# In[78]:


arr[[1, 3, 5]]


# In[79]:


arr.take([1, 3, 5])


# In[85]:


np.choose([1, 3, 5], arr)


# In[ ]:




