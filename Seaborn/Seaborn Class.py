#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# In[ ]:


# sns.set(style="darkgrid")   # it makes dark background, we can see grids.


# In[2]:


import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# In[3]:


diamonds=sns.load_dataset('diamonds')
exercise=sns.load_dataset('exercise')
flights=sns.load_dataset('flights')
geyser=sns.load_dataset('geyser')
iris=sns.load_dataset('iris')
penguins=sns.load_dataset('penguins')
planets=sns.load_dataset('planets')
mpg=sns.load_dataset('mpg')
tips = sns.load_dataset('tips')
titanic=sns.load_dataset('titanic')


# In[4]:


penguins.head()


# In[5]:


penguins.info()


# In[7]:


penguins.isnull().sum()


# In[8]:


penguins.dropna(inplace = True)


# In[9]:


penguins.isnull().sum()


# In[10]:


penguins.info()


# In[11]:


penguins.head()


# In[13]:


sns.distplot(penguins['body_mass_g'])


# In[27]:


sns.distplot(penguins['body_mass_g'], kde = False, hist_kws = dict(edgecolor = 'k', lw = 2))


# In[28]:


sns.distplot(penguins['body_mass_g'], kde = False, hist_kws = dict(edgecolor = 'k', lw = 2), bins = 20)


# In[29]:


sns.distplot(penguins['body_mass_g'], hist = False)


# In[30]:


sns.distplot(penguins['body_mass_g'], hist = False, rug = True)


# In[32]:


geyser.head()


# In[33]:


geyser.info()


# In[6]:


sns.set(style="darkgrid")


# In[7]:


sns.distplot(geyser['waiting'], kde = False)


# In[37]:


geyser['waiting'].mean()


# In[44]:


stats.mode(geyser['waiting'])[0][0]


# In[47]:


tips.head()


# In[48]:


tips.info()


# In[52]:


sns.jointplot(x = tips['total_bill'], y = tips['tip'], data = tips) 


# In[70]:


sns.scatterplot(x = 'total_bill', y = 'tip', data = tips) 


# In[71]:


# But adding 'hue' gives the error:
sns.scatterplot(x = 'total_bill', y = 'tip', hue = tips.time.tolist(), data = tips)


# In[72]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'reg')


# In[73]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')


# In[74]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'kde')


# In[75]:


mpg.head()


# In[76]:


mpg.info()


# In[77]:


mpg.drop('displacement', axis = 1, inplace = True)


# In[78]:


sns.pairplot(mpg)


# In[79]:


mpg.groupby('model_year')[['mpg']].mean()


# In[91]:


mpg.groupby('model_year')[['mpg']].mean().plot()


# In[100]:


mpg.groupby('model_year')[['mpg']].mean().plot.bar()


# In[101]:


mpg.groupby("model_year")["horsepower"].mean().plot()


# In[102]:


sns.pairplot(mpg, hue = 'cylinders')


# In[ ]:





# In[ ]:





# In[ ]:




