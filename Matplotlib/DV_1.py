#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # 1. Set darkgrid style from seaborn

# In[3]:


sns.set(style = 'darkgrid')


# In[ ]:


## areaplot


# In[2]:


df = pd.DataFrame({'buy': [1, 2, 4, 9, 11, 5], 'register': [4, 6, 5, 11, 13, 15],
                   'view': [25, 45, 24, 58, 75, 55]}, 
                  index=pd.date_range(start='2018/01/01', end='2018/07/01',
                                      freq='M'))
df.head()


# In[ ]:


df.shape


# In[7]:


df.plot()


# In[6]:


df.plot.area()


# # 2. Make a bar plot

# In[ ]:


## barplots


# In[9]:


income = [100, 80, 150, 48, 52, 69, 88]
expense = [30, 100, 100, 20, 75, 50, 28]
index = ['A', 'B', 'C','D', 'E', 'F', 'G']
df = pd.DataFrame({'income': income,'expense': expense}, index=index)
df.head()


# # 3. Make a bar plot

# In[10]:


df.plot.bar()


# In[10]:


df.plot(kind = 'bar')


# In[ ]:





# # 3. Stack the bars

# In[16]:


df.plot.bar(stacked = True)


# In[ ]:





# # 3. Rotate the labels and set figsize

# In[17]:


games = ['Game-1', 'Game-2', 'Game-3', 'Game-4', 'Game-5', 'Game-6', 'Game-7']


# In[12]:


df.plot.bar(stacked = True, figsize = (9, 6))
plt.xticks(rotation = 0)
plt.show()


# In[ ]:





# # 4. Replace the labels by "Game-1", "Game-2", "Game-3", "Game-4", "Game-5", "Game-6", "Game-7"
# # 5. Unstuck the bars, annotate the hight of the bars on top of them

# In[27]:


games = ['Game-1', 'Game-2', 'Game-3', 'Game-4', 'Game-5', 'Game-6', 'Game-7']


# In[17]:


g = df.plot.bar(figsize = (9, 6))
plt.xticks(rotation = 0)
for p in g.patches:
    g.annotate((p.get_height()), (p.get_x()+ 0.01, p.get_height()+0.6), size = 10)
plt.show()


# In[40]:


g = df.plot.bar(figsize = (9, 6))
plt.xticks(rotation = 0)
g.set_xticklabels(games)
for p in g.patches:
    g.annotate((p.get_height()), (p.get_x()+ 0.01, p.get_height()+0.6), size = 10)
plt.show()


# In[ ]:





# In[ ]:


## histograms


# In[18]:


tips=sns.load_dataset("tips")


# In[19]:


tips.head()


# # 6. Histogram of the total_bill column

# In[52]:


sns.distplot(tips['total_bill'], kde = False)


# In[50]:


tips['total_bill'].hist()


# In[ ]:





# In[ ]:


## lineplots


# In[ ]:


tips.head()


# # 7. Plot the avg tip by size  (lineplot)

# In[63]:


tips.groupby('size')['tip'].mean().plot()


# In[ ]:





# # 8.Set the linestyle as "--"

# In[66]:


tips.groupby('size')['tip'].mean().plot(ls = '--')


# In[ ]:





# In[ ]:


## Scatter Plots


# In[ ]:


tips.head()


# # 9. Make a scatter plot between tip and total_bill

# In[69]:


tips.plot.scatter('tip', 'total_bill')


# In[ ]:





# # 10. Set an additional dimension using size column

# In[72]:


tips.head()


# In[21]:


tips.plot.scatter('tip', 'total_bill', c = 'size', cmap = 'coolwarm')


# In[ ]:





# In[ ]:


## boxplots


# In[ ]:


tips.head()


# # 11. Make a box plot of total_bill column

# In[75]:


sns.boxplot(tips['total_bill'])


# In[77]:


tips.boxplot('total_bill')


# In[ ]:





# # 12. Seperate the the boxplot above using size columns

# In[82]:


tips.boxplot('total_bill', 'size')
plt.tight_layout()


# In[ ]:





# # 13. Make the same plot using seaborn

# In[83]:


sns.boxplot('size', 'total_bill', data = tips)


# In[ ]:





# # 14. Make a violinplot instead of boxplot and discuss the difference between boxplot and violinplot

# In[84]:


sns.violinplot('size', 'total_bill', data = tips)


# In[23]:


sns.violinplot('size', 'total_bill', data = tips)
sns.swarmplot('size', 'total_bill', data = tips, color = 'black')


# In[ ]:





# In[ ]:




