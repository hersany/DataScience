#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('movies_metadata.csv', error_bad_lines=False)


# In[4]:


df = pd.read_csv('movies_metadata.csv', error_bad_lines=False, encoding = 'latin-1')


# In[9]:


df.info()


# In[10]:


df.head()


# In[13]:


df.loc[2]


# In[14]:


df.shape


# In[16]:


df.columns


# In[18]:


df[['title', 'genres']]


# In[15]:


df[df['original_title'] == 'Grumpier Old Men']


# In[5]:


df.iloc[4]


# In[20]:


df.info()


# In[21]:


df2 = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]


# In[22]:


df2.head(2)


# In[24]:


df.head(10)


# In[25]:


df.sort_values(by = 'release_date')


# In[34]:


df['release_date'].dtype


# In[37]:


df[df['release_date'] > '1995-01-01']


# In[38]:


df.columns


# In[39]:


df.sort_values('runtime', ascending = False)


# In[40]:


df.info()


# In[44]:


df['budget'].value_counts()


# In[70]:


df[(df['revenue'] >= 2000000) & (df['budget'] <= 1000000)]


# In[50]:


df['runtime'].max()


# In[51]:


df['runtime'].min()


# In[52]:


df.info()


# In[53]:


df['vote_count'].value_counts()


# In[54]:


df.describe()


# In[6]:


df['vote_count'].quantile(0.70)


# In[8]:


df[(df['runtime'] >= 30) & (df['runtime'] <= 360)]['title']


# In[73]:


df.info()


# In[74]:


df[['title', 'vote_count']]

