#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Distribution Plots


# In[4]:


import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# In[5]:


tips = sns.load_dataset('tips')


# In[6]:


tips.head()


# In[7]:


tips


# In[10]:


sns.distplot(tips['total_bill'])


# In[10]:


sns.distplot(tips['total_bill'], kde = False, bins = 20);


# In[11]:


sns.distplot(tips['total_bill'], kde = False, bins = 40);      # histogram, there is a hist = True arg.


# In[21]:


sns.jointplot(x = tips['total_bill'], y = tips['tip'], data = tips)       # scatter plot


# In[22]:


sns.jointplot(tips['total_bill'], tips['tip'], tips, kind = 'hex')  # default kind value is scatter


# In[23]:


sns.jointplot(tips['total_bill'], tips['tip'], tips, kind = 'reg')


# In[25]:


tips.head()


# In[24]:


sns.pairplot(tips)         # it is a collected form of jointplots of each numerical variables.scatter/strip


# In[26]:


sns.pairplot(tips, hue = 'sex')     # we can add categorical variable with hue argument


# In[27]:


sns.pairplot(tips, hue = 'sex', palette = 'coolwarm') 


# In[28]:


sns.rugplot(tips['total_bill'])   # it gives distribution without bins (unlike histogram)
                                  # dash mark for every points with uniform distribution


# In[32]:


sns.distplot(tips['total_bill'], kde = False)


# In[33]:


sns.distplot(tips['total_bill'])   # kde lin  e; kernel density estimation
                                   # normal distribution over each point and collected form of norm.dist.


# In[34]:


sns.kdeplot(tips['total_bill'])


# In[ ]:


# Categorical Plots


# In[5]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


tips = sns.load_dataset('tips')


# In[7]:


tips.head()


# In[17]:


import numpy as np


# In[16]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips)  # x = categorical, y = numeric
                                                       # it gives mean of total_bill


# In[18]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.sum)  # we can get sum by estimator arg.


# In[21]:


sns.barplot(tips['sex'], tips['total_bill'], estimator = np.std)


# In[20]:


sns.countplot(tips['sex'])            # it counts values


# In[23]:


sns.countplot('size', data = tips)  # it is barchart with numbers of values.


# In[46]:


sns.violinplot(tips['total_bill'])


# In[37]:


sns.boxplot(tips['total_bill'])


# In[24]:


sns.boxplot(tips['day'], tips['total_bill'])     # it gives total_bill boxplot per day


# In[26]:


sns.boxplot(tips['day'], tips['total_bill'], hue = tips['smoker'])   # we can add other status/info with hue.


# In[27]:


sns.violinplot(tips['day'], tips['total_bill'])    # points kde. violinplot related with boxplot. 


# In[29]:


sns.violinplot(tips['day'], tips['total_bill'], hue = tips['smoker'])


# In[51]:


sns.violinplot(tips['day'], tips['total_bill'], hue = tipss['smoker'], split = True)


# In[31]:


sns.stripplot(x = 'day', y = 'total_bill', data = tips)  # like scatter plot based one numeric one categorical
                                                         # scatter plot is about 2 numeric


# In[33]:


sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = False)


# In[49]:


sns.stripplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex', dodge = True)


# In[52]:


sns.stripplot(x = 'day', y = 'total_bill', data = tips)


# In[8]:


sns.swarmplot(x = 'day', y = 'total_bill', data = tips)   # combining stripplot and violinplot
                                                          # it is for small data sets


# In[64]:


tips['day'][tips['day'] == 'Fri'].value_counts()


# In[60]:


sns.violinplot(x = 'day', y = 'total_bill', data = tips)
sns.swarmplot(x = 'day', y = 'total_bill', data = tips, color = 'black')


# In[67]:


sns.barplot(x = 'day', y = 'total_bill', data = tips)


# In[72]:


sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'bar') # we can call all types with kind arg.


# In[9]:


# Matrix Plots
# we need matrix form for heatmap.


# In[53]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


tips = sns.load_dataset('tips')


# In[12]:


flights = sns.load_dataset('flights')


# In[13]:


flights.head()


# In[14]:


tips.head()


# In[15]:


tips.corr()


# In[22]:


sns.heatmap(tips.corr(), annot = True, cmap = 'coolwarm')


# In[37]:


flights.head()


# In[32]:


flights.corr()


# In[27]:


sns.heatmap(flights.corr(), annot = True)


# In[40]:


fp = flights.pivot_table(values = 'passengers', index = 'month', columns = 'year') 


# In[41]:


fp


# In[42]:


sns.heatmap(fp)


# In[52]:


sns.heatmap(fp, linecolor = 'white', linewidths = 1)


# In[56]:


plt.subplots(figsize=(10,5))
sns.heatmap(fp, cmap = 'coolwarm', linecolor = 'black', linewidths = 1)


# In[58]:


sns.clustermap(fp, cmap = 'coolwarm')              # it doesn't order. it makes clustersgroups.
                                                   #standard_scale = 1


# In[59]:


# Grids


# In[61]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[62]:


iris = sns.load_dataset('iris')


# In[63]:


iris.head()


# In[64]:


sns.pairplot(iris)


# In[65]:


sns.PairGrid(iris)


# In[70]:


g = sns.PairGrid(iris)
g.map(plt.scatter)


# In[71]:


g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[72]:


tips = sns.load_dataset('tips')


# In[73]:


tips.head()


# In[76]:


g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')


# In[81]:


g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')
g.map(sns.distplot, 'total_bill')


# In[83]:


g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')
g.map(plt.scatter, 'total_bill', 'tip')


# In[ ]:




