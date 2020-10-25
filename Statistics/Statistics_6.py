#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
import math


# ## One Sample t Test

# #### Analyze if college students get 7.2 hours of sleep, on average, based on a sample of students, alpha = 0.05

# In[2]:


df = pd.read_csv('students.csv')


# In[3]:


df.head()


# In[4]:


# H0: mu = 7.2
# Ha: mu != 7.2
# it is two tailed test


# In[5]:


onesample = stats.ttest_1samp(df['Sleep'], 7.2)         # sample, pop_mean


# In[6]:


onesample.statistic


# In[7]:


onesample.pvalue           # fail to reject H0 because p_value is higher than alpha (significance level)


# In[8]:


alpha = 0.05
p_value = onesample.pvalue
if p_value<alpha:
    print('At {} level of significance, we can reject the null hypothesis in the favor of Ha.'.format(alpha))
else:
    print('At {} level of significance, we fail to reject the null hypothesis.'.format(alpha))


# #### The principal of the school thinks that the average hours of sleep is at most 7.2, alpha = 0.05

# In[9]:


# H0: mu = 7.2
# Ha: mu < 7.2
# it is one tailed test


# In[10]:


onesample = stats.ttest_1samp(df['Sleep'], 7.2)


# In[11]:


onesample.pvalue / 2       # reject H0 because p_value is lower than alpha (significance level)


# In[12]:


alpha = 0.05
p_value = onesample.pvalue/2
if p_value<alpha:
    print('At {} level of significance, we can reject the null hypothesis in the favor of Ha.'.format(alpha))
else:
    print('At {} level of significance, we fail to reject the null hypothesis.'.format(alpha))


# ## Independent Samples T Test (variances unknown and equal)

# In[13]:


# H0 : mu1 = mu2
# Ha : mu1 != mu2


# In[14]:


df = pd.read_csv('catalysts.csv')


# In[15]:


df


# In[16]:


xbar1 = df['Catalyst1'].mean()
xbar2 = df['Catalyst2'].mean()

s1 = df['Catalyst1'].std()
s2 = df['Catalyst2'].std()


# In[17]:


xbar1


# In[18]:


xbar2


# In[19]:


s1


# In[20]:


s2


# In[21]:


s_pooled = math.sqrt(((len(df['Catalyst1']) - 1) * (s1 ** 2) + (len(df['Catalyst2']) - 1) * (s2 ** 2)) / (len(df['Catalyst1']) - 1 + len(df['Catalyst2']) - 1))
print('spooled = {:.3f}'.format(s_pooled))


# In[22]:


t_statistic = (xbar1-xbar2)/(s_pooled*math.sqrt(1/len(df['Catalyst1']) + 1/len(df['Catalyst2'])))
print ('t_statistic = {:.3f}'.format(t_statistic))


# In[23]:


# degrees_of_freedom = n1 + n2 - 2


# In[24]:


p_value = 2 * stats.t.cdf(t_statistic, 14)


# In[25]:


p_value


# In[26]:


alpha = 0.05

if p_value<alpha:
    print('At {} level of significance, we can reject the null hypothesis in the favor of Ha.'.format(alpha))
else:
    print('At {} level of significance, we fail to reject the null hypothesis.'.format(alpha))


# ### scipy.stats.ttest for 2 groups

# In[27]:


ind_test_w_2gr = stats.ttest_ind(df['Catalyst1'], df['Catalyst2'], equal_var = True)


# In[28]:


ind_test_w_2gr.statistic


# In[29]:


ind_test_w_2gr.pvalue


# ### rp.ttest for 2 groups

# In[30]:


import researchpy as rp


# In[31]:


rp.ttest(df['Catalyst1'], df['Catalyst2'])


# ## Arsenic concentration in public drinking water supplies is a potential health risk. An article in the Arizona Republic (May 27, 2001) reported drinking water arsenic concentrations in parts per billion (ppb) for 10 metropolitan Phoenix communities and 10 communities in rural Arizona. You can find the data in CSV file.

# In[32]:


df = pd.read_csv('arsenic.csv')


# In[34]:


df


# In[36]:


# Independent Samples T Test (assumption that --> variances unknown and equal), small size


# In[37]:


ind_test_w_2gr = stats.ttest_ind(df['x1'], df['x2'], equal_var = True)


# In[38]:


ind_test_w_2gr.statistic


# In[39]:


p_value = ind_test_w_2gr.pvalue


# In[40]:


alpha = 0.05

if p_value<alpha:
    print('At {} level of significance, we can reject the null hypothesis in the favor of Ha.'.format(alpha))
else:
    print('At {} level of significance, we fail to reject the null hypothesis.'.format(alpha))


# Drinking water arsenic concentrations in ppb are different for rural Arizona and metropolitan Phoenix.

# ## Paired Sample Test

# In[41]:


df = pd.read_csv('prozac.csv')


# In[43]:


df


# In[46]:


paired_test = stats.ttest_rel(df['moodpre'], df['moodpost'])


# In[48]:


paired_test.pvalue        # it is for two side


# In[49]:


paired_test.pvalue / 2    # it is for one side


# In[52]:


rp.ttest(df['moodpre'], df['moodpost'], paired = True)           # with researchpy

