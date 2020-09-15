#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


titanic = sns.load_dataset('titanic')


# In[3]:


titanic.head()


# In[4]:


titanic.info()


# In[60]:


sns.set(style = "whitegrid")
sns.jointplot('fare', 'age', data = titanic, xlim = (-100, 600))
plt.show()


# In[59]:


sns.distplot(titanic['fare'], kde = False, color = 'red', bins = 30)
plt.xlim(0)
plt.show()


# In[57]:


sns.boxplot('class', 'age', data = titanic, palette = 'rainbow')
plt.show()


# In[61]:


sns.swarmplot('class', 'age', data = titanic, palette = 'Set2')
plt.show()


# In[22]:


sns.countplot('sex', data = titanic)
plt.show()


# In[66]:


plt.figure(figsize = (8, 5))
sns.heatmap(titanic.corr(), cmap = 'coolwarm', vmin = -0.8, vmax = 0.8)
plt.title('titanic.corr()')
plt.show()


# In[64]:


g = sns.FacetGrid(titanic, col = 'sex', aspect = 1, height = 5)
g.map(sns.distplot, 'age', kde = False, bins = 10)
plt.xlim(0)
plt.tight_layout()


# In[63]:


g = sns.FacetGrid(titanic, col = 'sex', aspect = 1, height = 5)
g.map(plt.hist, 'age', bins = 10)
plt.xlim(0)
plt.tight_layout()

