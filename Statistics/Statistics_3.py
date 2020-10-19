#!/usr/bin/env python
# coding: utf-8

# # Binomial Distribution

# In[1]:


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# In[34]:


(n, p) = (2, 0.5)


# In[35]:


stats.binom(n, p)


# In[36]:


binomDist = stats.binom(n, p)


# In[37]:


binomDist.args


# In[38]:


binomDist.pmf(0)               # it gives P(x=0) in n = 2, p = 0.5


# In[39]:


dist = []

print('r\tp(r)')
for i in range(n + 1):
    dist.append(binomDist.pmf(i))
    print(str(i) + '\t' + str(binomDist.pmf(i)))


# In[12]:


binomDist.pmf(2) 


# In[13]:


binomDist.pmf(3)    # because n = 2


# In[21]:


# other example


# In[41]:


(n, p) = (10, 0.2)


# In[42]:


binomDist = stats.binom(n, p)


# In[43]:


binomDist.args


# In[44]:


dist = []

print('r\tp(r)')
for i in range(n + 1):
    dist.append(binomDist.pmf(i))
    print(str(i) + '\t' + str(binomDist.pmf(i)))


# In[45]:


binomDist.pmf(7) 


# In[46]:


binomDist.cdf(1)           # pmf(0) + pmf(1)


# In[47]:


plt.bar(list(range(n + 1)), dist)


# In[48]:


mean, var = binomDist.stats()


# In[49]:


print('mean = ' + str(mean))


# print('var = ' + str(var))

# In[53]:


binomDist.stats()      # mean and var


# In[54]:


binomDist.median()


# In[56]:


binomDist.std()


# In[72]:


binomDist.rvs(100)


# In[75]:


stats.binom.cdf(2, 10, 0.2)


# In[76]:


binomDist.cdf(2)


# ### Exercise
# There was a probability of 0.8 success in any attempt to make a call. 
# Calculate the probability of having 7 successes in 10 attempts.

# In[92]:


stats.binom.pmf(7, 10, 0.8)


# ### Exercise
# A (blindfolded) marksman finds that on the average he hits the target 4 times out of 5. If he fires 4 shots, what is the probability of
# (a) more than 2 hits?
# (b) at least 3 misses?

# In[ ]:





# # Poisson Distribution

# In[94]:


stats.poisson.pmf(5, 6)            # avg = 6, x = 5


# In[95]:


stats.poisson.cdf(5, 6)    


# ### Exercise
# A bank is interested in studying the number of people who use the ATM located outside its office late at night.
# On average, 1.6 customers walk up to the ATM during any 10 minute interval between 9pm and midnight.
# What is lambda λ for this problem?
# What is the probability of exactly 3 customers using th ATM during any 10 minute interval?
# What is the probability of 3 or fewer people?

# In[98]:


avg = 1.6
x = 3


# In[99]:


stats.poisson.pmf(3, 1.6)   


# In[100]:


stats.poisson.cdf(3, 1.6)   


# In[101]:


poissonDist = stats.poisson(avg)


# In[102]:


dist = []

print('r\tp(r)')
for i in range(10):
    dist.append(poissonDist.pmf(i))
    print(str(i) + '\t' + str(poissonDist.pmf(i)))


# ### Exercise
# The Indiana Department of Transportation is concerned about the number of deer being struck by cars between Martinsville and Bloomington. They note the number of deer carcasses and other deer-related accidents over a 1-month period in a 2-mile intervals.
# What is the probability of zero deer strike incidents during any 2-mile interval between Martinsville and Bloomington?
# 0.08 strikes per/day

# In[104]:


stats.poisson.pmf(0, 0.08*30)


# # Bernoulli Distribution

# In[116]:


p = 0.3


# In[117]:


bernDist = stats.bernoulli(p)


# In[118]:


bernDist.pmf(0)


# In[119]:


bernDist.pmf(1)


# In[120]:


bernDist.pmf(2)             # because single trial. there is no other option.


# In[121]:


dist = []

print('r\tp(r)')
for i in range(2):
    dist.append(bernDist.pmf(i))
    print(str(i) + '\t' + str(bernDist.pmf(i)))


# In[122]:


plt.bar(list(range(2)), dist)
plt.xticks(list(range(2)), ('0', '1'))
plt.show()


# In[123]:


mean, var = bernDist.stats()


# In[125]:


str(mean)


# In[126]:


str(var)


# In[127]:


bernDist.median()


# In[129]:


bernDist.std()


# In[ ]:




