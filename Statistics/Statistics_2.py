#!/usr/bin/env python
# coding: utf-8

# # Probability

# In[35]:


# Heads or Tails


# In[36]:


import random


# In[37]:


coin = ('H', 'T')


# In[38]:


random.choice(coin)


# In[39]:


for i in range(5):
    result = random.choice(coin)
    print(result)


# In[42]:


results = {'H' : 0, 'T' : 0}

for i in range(10):
    results[random.choice(list(results.keys()))] += 1
    
print('P(Heads):', results['H'] / sum(results.values()))
print('P(Tails):', results['T'] / sum(results.values()))


# In[41]:


results = {'H' : 0, 'T' : 0}

for i in range(100000):                                     # law of large estimates
    results[random.choice(list(results.keys()))] += 1
    
print('P(Heads):', results['H'] / sum(results.values()))
print('P(Tails):', results['T'] / sum(results.values()))


# In[43]:


# Rolling 2 Dice


# In[44]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[45]:


np.random.seed(51)


# In[46]:


d1 = np.array([1, 2, 3, 4, 5, 6])
d2 = np.array([1, 2, 3, 4, 5, 6])


# In[60]:


dice_1 = []
dice_2 = []

sums = []

for i in range(1000):
    dice_1.append(np.random.choice(d1))
    dice_2.append(np.random.choice(d2))
    sums.append(dice_1[i] + dice_2[i])

#print(dice_1)
#print(dice_2)
#print(sums)


# In[70]:


fig, (ax1, ax2) = plt.subplots(ncols = 2, sharey = True, figsize = (12, 4))
sns.countplot(dice_1, ax = ax1)
sns.countplot(dice_2, ax = ax2)


# In[68]:


sns.countplot(sums)


# # Combinatoric Generators

# In[72]:


# Product


# In[73]:


import itertools as it


# In[84]:


cp = list(it.product('HT', repeat = 3))      # possible outcomes of H or T (2 ** 3)


# In[85]:


len(cp)


# In[86]:


cp


# In[87]:


cp2 = list(it.product('123456', 'HT'))       # 2 x 6 = 12 possible outcomes


# In[88]:


cp2


# In[89]:


len(cp2)


# # Permutations

# In[1]:


import math


# In[2]:


math.factorial(4)


# In[3]:


def permutation(n, r):
    return math.factorial(n) / math.factorial(n - r)


# In[4]:


permutation(4, 2)


# In[5]:


permutation(8, 4)


# In[105]:


import itertools as it


# In[102]:


cp3 = list(it.permutations('GRYB', 2))       # pick 2 colors of 4 colors (order is important)


# In[103]:


len(cp3)


# In[104]:


cp3                                          # sequence is important


# # Combinations

# In[6]:


import itertools as it


# In[106]:


cp4 = list(it.combinations('GRYB', 2))           # pick 2 colors of 4 colors (order is not important)


# In[107]:


cp4


# In[108]:


len(cp4)


# In[7]:


def combination(n, r):
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


# In[8]:


combination(4, 2)


# In[9]:


combination(20, 11)


# In[119]:


cp5 = list(it.combinations_with_replacement('GRYB', 2))  


# In[120]:


cp5


# In[121]:


len(cp5)


# In[ ]:




