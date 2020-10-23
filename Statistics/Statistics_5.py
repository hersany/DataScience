#!/usr/bin/env python
# coding: utf-8

# # CENTRAL LIMIT THEOREM

# ## Sample Mean for a Uniform Distribution

# In[1]:


import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
random.seed(54312)


# In[10]:


sample_size = 30

sim_num = 10000


# In[11]:


mean_list = []

for i in range(sim_num):
    sample_list = []
    for i in range(sample_size):
        sample_list.append(random.randint(0, 100))
    sample_mean = sum(sample_list)/sample_size
    mean_list.append(sample_mean)


# In[12]:


mean_list


# In[13]:


sum(mean_list)/len(mean_list)


# In[19]:


plt.hist(mean_list, bins=100, density = True, color = 'r');
plt.grid()
mu = 50
sigma = math.sqrt((100**2)/12) / (math.sqrt(sample_size))
x = np.linspace(mu - 4* sigma, mu + 4 * sigma)
plt.plot(x, stats.norm.pdf(x, mu, sigma))


# ## Sample Mean for a Exponential Distribution

# In[32]:


sample_size = 30

sim_num = 10000


# In[33]:


mean_list = []

for i in range(sim_num):
    sample_list = []
    for i in range(sample_size):
        sample_list.append(np.random.exponential(1))
    sample_mean = sum(sample_list)/sample_size
    mean_list.append(sample_mean)


# In[34]:


plt.hist(mean_list, bins=100, density = True, color = 'r');
plt.grid()
mu = 1
sigma = 1 / (math.sqrt(sample_size))
x = np.linspace(mu - 4* sigma, mu + 4 * sigma)
plt.plot(x, stats.norm.pdf(x, mu, sigma))


# ## CONFIDENCE INTERVAL

# In[39]:


import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
random.seed(39809)


# In[40]:


sample_size = 30
sample_list = []

for i in range(30):
    sample_list.append(random.randint(0, 10))    


# In[41]:


sample_mean = np.mean(sample_list)


# In[42]:


sample_mean


# In[43]:


n = len(sample_list)


# In[44]:


cl = 0.95

std = 1


# In[51]:


critic_value = stats.norm.ppf(((1-0.95)/2) + 0.95)


# In[53]:


(((1-0.95)/2) + 0.95)   # z table ppf value for 0.95 at t table


# In[52]:


critic_value


# In[54]:


lower_limit = sample_mean - (critic_value * (std/math.sqrt(n)))


# In[56]:


upper_limit = sample_mean + (critic_value * (std/math.sqrt(n)))


# In[62]:


print(f'Your {cl} z confidence interval is ({lower_limit:.2f}, {upper_limit:.2f})')


# Exercise

# In[63]:


sample_list = [2, 3, 5, 6, 9]


# In[65]:


sample_mean = np.mean(sample_list)

sample_mean


# In[66]:


std = 2.5


# In[67]:


n = len(sample_list)


# In[68]:


cl = 0.95


# In[71]:


critic_value = stats.norm.ppf(((1 - cl)/2) + cl)


# In[72]:


critic_value


# In[73]:


lower_limit = sample_mean - (critic_value * (std/math.sqrt(n)))


# In[74]:


upper_limit = sample_mean + (critic_value * (std/math.sqrt(n)))


# In[75]:


print(f'Your {cl} z confidence interval is ({lower_limit:.2f}, {upper_limit:.2f})')


# In[84]:


stats.norm.interval(cl, loc = sample_mean, scale = std/math.sqrt(n))   # using scipy


# In[76]:


critic_value = stats.norm.ppf(((1 - 0.99)/2) + 0.99)  # interval gets larger beacuse CL gets higher


# In[77]:


lower_limit = sample_mean - (critic_value * (std/math.sqrt(n)))


# In[78]:


upper_limit = sample_mean + (critic_value * (std/math.sqrt(n)))


# In[79]:


print(f'Your {cl} z confidence interval is ({lower_limit:.2f}, {upper_limit:.2f})')   # interval gets larger


# In[85]:


stats.norm.interval(0.99, loc = sample_mean, scale = std/math.sqrt(n))


# ## USING SCIPY

# In[87]:


stats.norm.interval(cl, loc = sample_mean, scale = std/math.sqrt(n))   # using scipy

