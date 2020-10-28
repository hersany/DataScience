#!/usr/bin/env python
# coding: utf-8

# # Finding the Confidence Interval of Polling Figures

# You are running a political campaign and decide to run 30 focus groups with about 10 people in each group. You get the results and want to report to your candidate the number of people who would vote for them in a typical 10-person group. Since there is some variability in each focus group, you decide that the most accurate way is to give a 95% z-confidence interval. You assume from past experience that the standard deviation is 2.89.

# 1.Import the random Python package and set the seed to 39809. This will ensure that we get the same results every time we run the program:

# In[1]:


import random
import math
import numpy as np
from scipy import stats
random.seed(39809)


# 2.Initialize our sample list and collect our samples from our focus groups. Use random.randint

# In[2]:


sample_size = 30
sample_list = []

for i in range(30):
    sample_list.append(random.randint(0, 10))
sample_mean = np.mean(sample_list)


# 3.Calculate 95% z-confidence interval.

# In[3]:


sample_mean
n = 30
std = 2.89
cl = 0.95


# In[4]:


std_e = std/math.sqrt(n)


# In[5]:


ci = stats.norm.interval(cl, sample_mean, std_e)


# In[6]:


ci


# In[7]:


print('Your {} z confidence interval is {}.'.format(cl, ci))


# 4.If you did everything correctly, then the following should be printed when you run your notebook:

#     Your 0.95 z confidence interval is (3.965845784931483, 6.034154215068517)

# # Hypothesis Testing

# Your boss asks you to conduct a hypothesis test about the mean dwell time of a new type of UAV.  Before you arrived, an experiment was conducted on n=5 UAVs (all of the new type) resulting in a sample mean dwell time of 10.4 hours.  The goal is to conclusively demonstrate, if possible, that the data supports the manufacturer’s claim that the mean dwell time is greater than 10 hours.  Given that it is reasonable to assume the dwell times are normally distributed, the sample standard deviation is s = 0.5 hours, and using a significance level of α = 0.01:

# 1.Write out the null and alternative hypotheses

# In[8]:


# H0 : mu = 10
# Ha : mu > 10


# 2.Calculate the test statistic

# In[9]:


mu_sample = 10.4
mu = 10
s = 0.5
n = 5
alpha = 0.01


# In[10]:


t_statistic = (mu_sample-mu)/(s/math.sqrt(n))


# In[11]:


t_statistic


# 3.Find the p-value and state the outcome

# In[12]:


df = n - 1


# In[13]:


p_value = 1 - stats.t.cdf(t_statistic, df)


# In[14]:


p_value


# In[15]:


if p_value<alpha:
    print('At {} level of significance, we can reject the null hypothesis in the favor of Ha.'.format(alpha))
else:
    print('At {} level of significance, we fail to reject the null hypothesis.'.format(alpha))

