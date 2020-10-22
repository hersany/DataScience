#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats


# ## 1  
# Create a binomial cumulative distribution table for n=10 using Python scipy.stats. 

# In[26]:


p = [0.01, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]


# In[4]:


k = list(range(10))


# In[5]:


n = 10


# In[25]:


print('n = 10')
print()
print('p', end = ' ')
for i in p:
    print('{:.2f}'.format(i), end = ' ')
print('\n')
print('k', end = '\n\n')
for(ii) in k:
    print(ii, end = ' ')
    for i in range(len(p)):
        a = '{:.2f}'.format(stats.binom.cdf(k[ii], n, p[i]))
        print(a, end = ' ')
        if i == 12:
            print('\n')


# ## 2.1
# A salesperson has found that the probability of a sale on a single contact is approximately .3. If the salesperson contacts 10 prospects, what is the approximate probability of making at least one sale?

# In[27]:


n = 10
p = 0.30


# In[28]:


binomDist = stats.binom(n, p)


# In[32]:


binomDist.pmf(0)         # probability of no sale


# In[33]:


1 - binomDist.pmf(0)      # probability of at least one sale


# ## 2.2
# Ten coins are tossed simultaneously. Find the probability of getting
# 
# (i) at least seven heads
# 
# (ii) exactly seven heads
# 
# (iii)at most seven heads

# In[35]:


n = 10
p = 0.5  # for heads


# In[36]:


binomDist = stats.binom(n, p)


# In[38]:


1 - binomDist.cdf(6)      # probability of at least seven heads


# In[39]:


binomDist.pmf(7)  + binomDist.pmf(8)  + binomDist.pmf(9)  + binomDist.pmf(10)


# In[43]:


binomDist.pmf(7)          # probability of seven heads


# In[41]:


binomDist.cdf(7)           # probability of at most seven heads


# ## 3.1
# A type of tree has seedlings dispersed in a large area with a mean density of five seedlings per square yard. What is the probability that none of ten randomly selected one-square yard regions have seedlings?

# In[49]:


avg = 50   # for 10 one-square yard
x = 0


# In[50]:


stats.poisson.pmf(x, avg)


# ## 3.2
# Let Y denote a random variable that has a Poisson distribution with mean λ = 2. Find
# (i) P(Y = 4)
# (ii) P(Y ≥ 4)
# (iii)P(Y < 4)
# (iv)P(Y ≥ 4 | Y ≥ 2 )

# In[53]:


avg = 2
x = 4


# In[55]:


stats.poisson.pmf(x, avg)          # x = 4


# In[56]:


1 - stats.poisson.cdf(3, avg)     # x >= 4


# In[57]:


stats.poisson.cdf(3, avg)         # x < 4


# In[59]:


(1 - stats.poisson.cdf(1, avg)) - (1 - stats.poisson.cdf(3, avg))   # P(x ≥ 4 | x ≥ 2 )


# ## 4
# Consider binomial experiment for n = 20, p = .05. 

# In[61]:


n = 20
p = 0.05


# In[62]:


binomDist = stats.binom(n, p)


# ## 4.1
# Calculate the binomial probabilities for Y = 0, 1, 2, 3, and 4.

# In[72]:


binomDist.pmf(0)


# In[68]:


binomDist.pmf(1)


# In[69]:


binomDist.pmf(2)


# In[70]:


binomDist.pmf(3)


# In[71]:


binomDist.pmf(4)


# ## 4.1
# Calculate the same probabilities by using the Poisson approximation with λ = np. Compare.

# In[73]:


avg = n*p   # avg = 1


# In[74]:


stats.poisson.pmf(0, avg)   


# In[75]:


stats.poisson.pmf(1, avg) 


# In[76]:


stats.poisson.pmf(2, avg) 


# In[77]:


stats.poisson.pmf(3, avg) 


# In[78]:


stats.poisson.pmf(4, avg) 


# In[ ]:




