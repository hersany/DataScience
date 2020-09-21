#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df1 = pd.read_csv('df1', index_col = 0)
df2 = pd.read_csv('df2')


# In[3]:


df1.head()


# In[4]:


df2.head()


# In[5]:


sns.set(style = 'darkgrid')


# In[6]:


df1['A'].hist()


# In[4]:


df = pd.DataFrame({'sales': [3, 2, 3, 9, 10, 6], 'signups': [5, 5, 6, 12, 14, 13],
                   'visits': [20, 42, 28, 62, 81, 50]},
                  index=pd.date_range(start='2018/01/01', end='2018/07/01',
                                      freq='M'))


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


# area plot


# In[8]:


df.plot.area()      # = df.plot(kind = 'area')


# In[9]:


df.plot.area(stacked = False)  


# In[12]:


df.plot.area(figsize = (9, 5))


# In[17]:


# barplots


# In[16]:


speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant','rabbit', 'giraffe', 'coyote', 'horse']
df = pd.DataFrame({'speed': speed,'lifespan': lifespan}, index=index)
df.head()


# In[18]:


df.plot.bar()


# In[41]:


df.plot.bar(figsize = (9, 6), rot = 0)
plt.axhline(50, color = 'green', ls = '--')


# In[44]:


labels=['Snail', 'Pig', 'Elephant','Rabbit', 'Giraffe', 'Coyote', 'Horse']


# In[46]:


g = df.plot.bar(figsize = (9, 6), rot = 0)
g.set_xticklabels(labels)
for p in g.patches:
    g.annotate((p.get_height()), (p.get_x()+0.02, p.get_height()+0.5))


# In[47]:


income = [100, 80, 150, 48, 52, 69, 88]
expense = [30, 100, 100, 20, 75, 50, 28]
index = ['snail', 'pig', 'elephant','rabbit', 'giraffe', 'coyote', 'horse']
df = pd.DataFrame({'income': income,'expense': expense}, index=index)
df.head()


# In[48]:


df.plot.bar()


# In[49]:


df.plot.bar(stacked = True)


# In[50]:


df['profit_loss'] = df['income'] - df['expense']


# In[52]:


df.plot.bar(figsize = (8, 4))


# In[53]:


# histograms


# In[54]:


mpg = sns.load_dataset('mpg')


# In[55]:


mpg.head()


# In[56]:


mpg['horsepower'].plot.hist(bins = 20)


# In[57]:


mpg['horsepower'].plot(kind = 'hist', bins = 20)


# In[59]:


df1.head()


# In[61]:


df1['B'].plot()


# In[62]:


df1['B'].plot.line()


# In[63]:


df1.plot(y = 'B')


# In[66]:


mpg.groupby('model_year')['horsepower'].mean().plot()


# In[67]:


mpg.groupby('model_year')['horsepower'].mean().plot.line()


# In[68]:


mpg.groupby('model_year')['mpg'].mean().plot.line(ls = '--')


# In[ ]:




