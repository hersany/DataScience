#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
import math


# ## EXERCISE 1. 
# The hourly wages in a particular industry are normally distributed with mean  $13.20  and  standard deviation $2.50. A company in this industry employs 40 workers, paying them an average of $12.20 per hour. Can this company be accused of paying substandard wages? Use an α = .01 level test.

# In[2]:


# H0: mu = 13.20
# Ha: mu < 13.20
# it is one tailed test


# In[3]:


mu = 13.20
mu_sample = 12.20
n = 40
std = 2.5
alpha = 0.01


# In[4]:


t_statistic = (mu_sample - mu)/(std/math.sqrt(n))


# In[5]:


t_statistic


# In[6]:


p_value = stats.norm.cdf(t_statistic)


# In[7]:


p_value


# In[8]:


if p_value < alpha:
    print('At {} level of significance, we can reject the null hypothesis in the favor of Ha.'.format(alpha))
else:
    print('At {} level of significance, we fail to reject the null hypothesis.'.format(alpha))


# ## EXERCISE 2.
# Shear strength measurements derived from unconfined compression tests for two types of soils gave the results shown in the following document (measurements in tons per square foot). Do the soils appear to differ with respect to average shear strength, at the 1% significance level?

# In[9]:


# H0: mu1 = mu2
# Ha: mu1 != mu2


# In[10]:


df = pd.read_csv('soil.csv')


# In[11]:


df.head()


# In[12]:


xbar1 = df['Soil1'].mean()
xbar2 = df['Soil2'].mean()

s1 = df['Soil1'].std()
s2 = df['Soil2'].std()

alpha = 0.01


# In[13]:


t_statistic = ((xbar1 - xbar2) - 0) / math.sqrt(((s1 ** 2) / df['Soil1'].notna().sum()) + ((s2 ** 2) / df['Soil2'].notna().sum()))


# In[14]:


t_statistic


# In[15]:


stats.norm.ppf(0.005)  # 0.01 / 2


# In[16]:


diff = xbar1 - xbar2
diff


# In[17]:


std_e = math.sqrt(((s1 ** 2) / df['Soil1'].notna().sum()) + ((s2 ** 2) / df['Soil2'].notna().sum()))
std_e


# In[18]:


diff - stats.norm.ppf(0.005) * std_e


# In[19]:


diff + stats.norm.ppf(0.005) * std_e


# In[20]:


# ci for xbar1 - xbar2 is 0.41 and 0.375 with %90 CL so we reject H0

