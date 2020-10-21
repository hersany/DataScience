#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# # Uniform Distribution

# In[2]:


(a, b) = (0, 30)


# In[4]:


unifDist = stats.uniform(0, 30)


# In[10]:


unifDist.args


# In[6]:


unifDist.pdf(10)


# In[14]:


unifDist.pdf(15)


# In[15]:


unifDist.cdf(15)


# In[12]:


unifDist.cdf(10)


# In[20]:


a = unifDist.rvs(1000)

b = []
for i in a:
    b.append(unifDist.pdf(i))


# In[23]:


plt.bar(a, b)


# In[24]:


mean, var = unifDist.stats()


# In[25]:


str(mean)


# In[26]:


str(var)


# In[27]:


unifDist.median()


# In[28]:


unifDist.std()


# # Normal Distribution

# In[30]:


(mu, sigma) = (0, 1)


# In[31]:


normDist = stats.norm(mu, sigma)


# In[33]:


normDist.args


# In[55]:


1 - normDist.cdf(2)            # P(Z>2)


# In[52]:


normDist.pdf(4)


# In[62]:


x = np.linspace(-5, 5, 1000)

y = normDist.pdf(x)


# In[63]:


plt.plot(x, y)


# In[64]:


mean, var, skew, kurt = normDist.stats(moments = 'mvsk')


# In[65]:


str(mean)


# In[66]:


str(var)


# In[67]:


str(skew)


# In[68]:


str(kurt)


# In[70]:


normDist.median()


# In[71]:


normDist.std()


# # t distribution

# In[72]:


stats.t.cdf(-0.7745966, df = 14)


# In[79]:


stats.t.cdf(0, df = 14)


# In[74]:


tDist = stats.t(df = 15)

x = np.linspace(-5, 5, 100)

y = tDist.pdf(x)


# In[75]:


plt.plot(x, y)


# In[ ]:




