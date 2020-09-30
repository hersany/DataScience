#!/usr/bin/env python
# coding: utf-8

# #### import the libraries

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #### load the tips dataset 

# In[12]:


tips = sns.load_dataset('tips')
tips.head()


# In[4]:


# instrutction: make a plot with seaborn that shows distribution of total bill. 


# ### 1-Distribution Plot

# ####  DISTPLOT

# In[8]:


sns.distplot(tips['total_bill'], kde = False, hist_kws = dict(edgecolor = 'k', lw = 2), bins = 15)


# In[13]:


sns.distplot(tips['total_bill'], kde = False)


# In[5]:





# show rug, kde, distplot in same figure but in different axes. 
# Explain the difference between matplotlib and seaborn in aspect of using axes.
# 
# (birinde ax.bar.... diye başlıyorduk, burada ax=axes[.. diye parantez içine yazıyoruz.)

# In[10]:


sns.set(style="darkgrid")
rs = np.random.RandomState(10)

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)

# Generate a random univariate dataset
# d = rs.normal(size=100)

# Plot a simple histogram with binsize determined automatically
sns.distplot(tips['total_bill'], kde=False, color="b", ax=axes[0, 0])

# Plot a kernel density estimate and rug plot
sns.distplot(tips['total_bill'], hist=False, rug=True, color="r", ax=axes[0, 1])

# Plot a filled kernel density estimate
sns.distplot(tips['total_bill'], hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

# Plot a histogram and kernel density estimate
sns.distplot(tips['total_bill'], color="m", ax=axes[1, 1])

# plt.setp(axes, yticks=[])
plt.tight_layout()


# In[16]:


sns.set(style="white")

# Set up the matplotlib figure


# Generate a random univariate dataset


# Plot a simple histogram with binsize determined automatically

# Plot a kernel density estimate and rug plot

# Plot a filled kernel density estimate

# Plot a histogram and kernel density estimate


# ### 2-Categorical Plot

# In[6]:


# ins: make a plot that shows avg total bills in both genders.


# In[9]:


sns.barplot('sex', 'total_bill', data = tips)


# In[17]:


sns.barplot('sex', 'total_bill', 'day', data = tips)
plt.legend(loc = 3)


# In[8]:


# ins: make a plot that shows avg total bills in both genders as well as the avg total bills in different days.
# what is the black bars on the graphs? (ci)


# In[ ]:





# In[6]:





# #### B) COUNTPLOT

# In[ ]:


# ins: count the people in the dataset in each day. And order them.


# In[30]:


tips.groupby('day').count()['size'].sort_values(ascending = False).index


# In[31]:


sns.countplot(tips['day'], order = tips.groupby('day').count()['size'].sort_values(ascending = False).index)


# In[27]:





# #### C) BOXPLOT

# In[ ]:


# Show the total bills range according to days as well as according to smokers/non smokers.


# In[32]:


sns.boxplot('day', 'total_bill', 'smoker', tips)


# In[8]:





# #### D) VIOLINPLOT

# In[ ]:


# make a violin plot of total bill separeted by days on x axis.


# In[33]:


sns.violinplot('day', 'total_bill', data = tips)


# In[17]:





# #### G) CATPLOT ( FORMER NAME: FACTOR PLOT)

# In[9]:


# try to make same plots using catplot instead of bar, violin, box plots.


# In[ ]:


sns.catplot()


# In[46]:



# kind options: bar, swarm, strip(default), box, violin, point and count. 


# #### H) POINTPLOT

# In[10]:


# make a pointplot that shows avg total bils both in lunch and dinner.


# In[20]:


sns.pointplot('time', 'total_bill', data = tips)


# In[21]:





# # 3- Matrix and Grid Plots

# In[11]:


# make a hit map to show corr matrix on tips dataset.


# In[35]:


sns.heatmap(tips.corr(), annot = True, cmap = 'coolwarm')


# In[28]:





# In[12]:


# make a pair plot of tips data set and make comments on it.


# In[45]:


sns.pairplot(tis);

