#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
from scipy import stats


# ## 1
# 
# Suppose scores on exams in statistics are normally distributed with an unknown population mean and a population standard deviation of 3 points. A random sample of 36 scores is taken and gives a sample mean (sample  mean score) of 68. Find a confidence interval estimate for the population mean exam score (the mean score on all exams).
# 
# Find a 90% confidence interval for the true (population) mean of statistics exam scores.

# In[3]:


sample_mean = 68
n = 36
std = 3
cl = 0.90


# In[4]:


std_e = std/math.sqrt(n)


# In[6]:


ci = stats.norm.interval(cl, sample_mean, std_e)


# In[10]:


print('Your {} z confidence interval is {}.'.format(cl, ci))


# ## 2
# 
# What is the normal body temperature for healthy humans? A random sample of 130 healthy human body temperatures provided by Allen Shoemaker7 yielded 98.25 degrees and standard deviation 0.73 degrees. 
# 
# Give a 99% confidence interval for the average body temperature of healthy people.

# In[13]:


sample_mean = 98.25
n = 130
std = 0.73
cl = 0.99


# In[14]:


std_e = std/math.sqrt(n)


# In[15]:


ci = stats.norm.interval(cl, sample_mean, std_e)


# In[16]:


print('Your {} z confidence interval is {}.'.format(cl, ci))


# ## 3
# 
# The administrators for a hospital wished to estimate the average number of days required for inpatient treatment of patients between the ages of 25 and 34. A random sample of 500 hospital patients between these ages produced a mean and standard deviation equal to 5.4 and 3.1 days, respectively.
# Construct a 95% confidence interval for the mean length of stay for the population of patients from which the sample was drawn.

# In[18]:


sample_mean = 5.4
n = 500
std = 3.1
cl = 0.95


# In[19]:


std_e = std/math.sqrt(n)


# In[20]:


ci = stats.norm.interval(cl, sample_mean, std_e)


# In[21]:


print('Your {} z confidence interval is {}.'.format(cl, ci))

