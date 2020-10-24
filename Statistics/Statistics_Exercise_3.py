#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
import math


# ## 1  
#  Create a Standard Normal Distribution Table using Python scipy.stats. 

# In[3]:


(mu, sigma) = (0, 1)
normDist = stats.norm(mu, sigma)


# In[64]:


z = np.round(np.linspace(0, 3, 310), 2) * -1


# In[65]:


z = list(z)


# In[84]:


for(ii) in range(310):
    a = np.round(normDist.cdf(z[ii]), 4)
    print(a, end = ' ')
    if ii % 10 == 0 and ii != 0:
        print('\n')


# ## 2
# The cycle time for trucks hauling concrete to a highway construction site is uniformly distributed over the interval 50 to 70 minutes. What is the probability that the cycle time exceeds 65 minutes  if it is known that the cycle time exceeds 55 minutes?

# In[85]:


(a, b) = (50, 70)


# In[86]:


unifDist = stats.uniform(50, 70)


# In[94]:


# P(X > 65 | X > 55)


# In[98]:


unifDist.cdf(65)


# In[99]:


unifDist.cdf(55)


# In[100]:


unifDist.cdf(55) / unifDist.cdf(65)


# ## 3.1
# The width of bolts of fabric is normally distributed with mean 950 mm (millimeters) and standard deviation 10 mm.
# What is the probability that a randomly chosen bolt has a width of between 947 and 958mm?

# In[102]:


(mu, sigma) = (950, 10)
normDist = stats.norm(mu, sigma)


# In[105]:


normDist.cdf(958) - normDist.cdf(947) 


# ## 3.2
# The width of bolts of fabric is normally distributed with mean 950 mm (millimeters) and standard deviation 10 mm.
# What is the appropriate value for C such that a randomly chosen bolt has a width less than C with probability .8531?

# In[109]:


normDist.ppf(0.8531)


# ## 4
# The school board administered an IQ test to 20 randomly selected teachers. They found that the average IQ score was 114 with a standard deviation of 10. Assume that the cumulative probability is 0.90. What population mean would have produced this sample result?

# In[113]:


# n = 20, df = 19, mu_sample = 114, std = 10


# In[114]:


stats.t.ppf(0.90, 19)


# In[116]:


114 - (stats.t.ppf(0.90, 19) * (10/math.sqrt(20)))   # = mu_population


# In[119]:


(114 - 111.03110946897203)/(10/math.sqrt(20))

