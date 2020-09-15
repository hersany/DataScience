#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


df1 = pd.read_csv('df1', index_col = 0)


# In[24]:


df1.head()


# In[14]:


df2 = pd.read_csv('df2')


# In[15]:


df2.head()


# In[19]:


df1['A'].hist()


# In[20]:


df1['A'].hist(bins = 30)


# In[25]:


df1['A'].plot(kind = 'hist')


# In[26]:


df1['A'].plot(kind = 'hist', bins = 30)


# In[27]:


df1['A'].plot.hist()


# In[28]:


df1['A'].plot.hist(bins = 30)


# In[29]:


df2.head()


# In[30]:


df2.plot.area()


# In[32]:


df2.plot.area(figsize = (10, 7), alpha = 0.4)


# In[33]:


df2.plot.bar()


# In[36]:


df2.plot(kind = 'bar', figsize = (10, 7))


# In[37]:


df2


# In[38]:


df2.plot.bar(stacked = True)


# In[41]:


sns.set(style = 'darkgrid')
df1['A'].plot.hist(bins = 40)


# In[42]:


df1.head()


# In[56]:


df1.plot.line(y = 'B', figsize = (12, 3))


# In[55]:


df1.plot.line(y = 'B', figsize = (12, 3), lw = 1)


# In[57]:


df1.plot.scatter('A', 'B')


# In[58]:


df1.plot.scatter('A', 'B', c = 'C')


# In[60]:


df1.plot.scatter('A', 'B', c = 'C', cmap = 'coolwarm', figsize = (10, 7))


# In[62]:


df1.plot.scatter('A', 'B', s = df1['C']*100)


# In[64]:


df2.plot.box(figsize = (10, 7))


# In[65]:


df= pd.DataFrame(np.random.randn(1000, 2), columns = ['a', 'b'])


# In[67]:


df.head()


# In[70]:


df.plot.hexbin('a', 'b', figsize = (10, 7), gridsize = 25)


# In[71]:


df.plot.hexbin('a', 'b', figsize = (10, 7), gridsize = 25, cmap = 'coolwarm')


# In[72]:


df2['a']


# In[73]:


df2['a'].plot.kde()


# In[74]:


df2['a'].plot.density()


# In[75]:


df2.plot.density()


# In[ ]:




