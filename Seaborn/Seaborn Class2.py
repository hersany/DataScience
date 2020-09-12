#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# In[2]:


df = pd.read_csv('cleaned_autos.csv')


# In[3]:


df.info()


# In[4]:


pd.set_option('display.max_columns', 27)


# In[5]:


df.head()


# In[6]:


df['vehicleType'].unique()


# In[7]:


df.groupby('vehicleType')['price'].mean().plot.bar()


# In[8]:


# variation of the price range by vehicle types


# In[9]:


plt.subplots(figsize = (12, 6))
sns.boxplot('vehicleType', 'price', data = df)


# In[10]:


# demonstration of the mean prices by the vehicle type


# In[11]:


fig, ax = plt.subplots(figsize = (12, 6))
sns.set(style="darkgrid")
sns.pointplot('vehicleType', 'price', data = df)
ax.set_xticklabels(df['vehicleType'].unique(), rotation = 90);


# In[12]:


# total count of vehicles by type available on sale


# In[13]:


plt.subplots(figsize = (12, 6))
sns.countplot('vehicleType', data = df)

