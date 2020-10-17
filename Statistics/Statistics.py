#!/usr/bin/env python
# coding: utf-8

# In[1]:


salary = [102, 33, 26, 27, 30, 25, 33, 33, 24]
import numpy as np
from scipy import stats


# In[2]:


mean_salary = np.mean(salary)
print('Mean :', mean_salary)


# In[6]:


median_salary = np.median(salary)
print('Median :', median_salary)


# In[4]:


stats.iqr(salary)


# In[7]:


mode_salary = stats.mode(salary)
print('Mode :', mode_salary)


# In[9]:


print('Range :', (np.max(salary) - (np.min(salary))))


# In[10]:


print('Variance :', (np.var(salary)))


# In[11]:


print('Std :', (np.std(salary)))


# In[12]:


a = [1, 10, 7, 12, 0, 30, 15, 22, 8, 2]
print(np.std(a))


# In[3]:


import numpy as np


# In[4]:


temp = [93, 84, 82, 78, 98, 70]
number_of_people = [13, 10, 11, 8, 15, 9]


# In[5]:


print('Coveriance :', np.cov(temp, number_of_people))


# In[6]:


print('Correlation :', np.corrcoef(temp, number_of_people))


# In[1]:


import numpy as np


# In[17]:


np.random.seed(101)
population = np.random.randint(0, 80, 100000)


# In[18]:


population


# In[19]:


len(population)


# In[20]:


np.random.seed(101)
sample = np.random.choice(population, 100)


# In[21]:


sample


# In[11]:


len(sample)


# In[25]:


population.mean()


# In[26]:


sample.mean()


# In[24]:


np.random.seed(101)
for i in range(10):
    sample = np.random.choice(population, 100)
    print(sample.mean())


# In[28]:


np.random.seed(101)
sample_means = []
for i in range(10):
    sample = np.random.choice(population, 100)
    sample_means.append(sample.mean())


# In[29]:


sample_means


# In[30]:


np.mean(sample_means)


# In[31]:


population.mean()


# In[32]:


from scipy.stats import kurtosis, skew


# In[33]:


pip install matplotlib


# In[1]:


import matplotlib.pyplot as plt


# In[43]:


np.random.seed(42)
x = np.random.normal(0, 2, 100000)


# In[44]:


plt.hist(x, bins = 100);


# In[45]:


kurtosis(x)


# In[46]:


skew(x)


# In[6]:


import numpy as np
from scipy import stats


# In[49]:


age = [20, 22, 25, 25, 27, 27, 29, 30, 31, 121]


# In[50]:


np.mean(age)


# In[51]:


np.median(age)


# In[13]:


stats.mode(age)


# In[15]:


stats.mode(age)[0]


# In[16]:


stats.mode(age)[0][0]


# In[24]:


age_2 = [20, 22, 25, 25, 27, 27, 29, 30, 31]


# In[25]:


np.mean(age_2)


# In[26]:


np.median(age_2)


# In[27]:


age_3 = [19, 20, 21, 22]


# In[28]:


stats.mode(age_3)   # it gives smallest element if no duplicate or more.


# In[29]:


type(age)


# In[30]:


# mean in arrays
age_new = np.array(age)


# In[31]:


age_new


# In[32]:


type(age_new)


# In[33]:


age_new.mean()


# In[35]:


a = np.array([[6, 8, 3, 0],
              [3, 2, 1, 7],
              [8, 1, 8, 4],
              [5, 3, 0, 5],
              [4, 7, 5, 9]])
stats.mode(a)


# In[38]:


stats.mode(a, axis = 1)


# In[52]:


# range, sd, variance
age = [20, 22, 25, 25, 27, 27, 27, 29, 30, 31, 121]


# In[73]:


range = np.max(age) - np.min(age)
print(range)


# In[74]:


np.ptp(age)   # it gives range Peak To Peak ptp


# In[54]:


np.std(age)


# In[55]:


np.var(age)


# In[56]:


age_2 = [20, 22, 25, 25, 27, 27, 27, 29, 30, 31]


# In[57]:


np.std(age_2)


# In[60]:


range = np.max(age_2) - np.min(age_2)


# In[61]:


print(range)


# In[62]:


# IQR - iqr


# In[63]:


x=[8, 10, 5, 24, 8, 3, 11, 3, 40, 7, 6, 12, 4]


# In[64]:


q75, q25 = np.percentile(x, [75, 25])


# In[65]:


q75


# In[66]:


q25


# In[67]:


sorted(x)


# In[68]:


iqr = q75-q25


# In[69]:


iqr


# In[70]:


stats.iqr(x)


# In[71]:


np.percentile(x, 75)


# In[72]:


np.percentile(x, 25)


# In[1]:


q = [62, 63, 64, 64, 70, 72, 76, 77, 81, 81]


# In[3]:


from scipy import stats
import numpy as np


# In[5]:


np.percentile(q, 25)


# In[6]:


np.percentile(q, 75)


# In[7]:


stats.iqr(q)


# In[8]:


np.median(q)


# In[9]:


np.mean(q)


# In[15]:


stats.mode(q)


# In[16]:


# scatter plot


# In[17]:


# method matplotlib


# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.linspace(0, 5, 11)


# In[3]:


x


# In[4]:


y = x ** 2


# In[5]:


y


# In[6]:


plt.plot(x, y);   # line plot


# In[7]:


plt.scatter(x, y);  #scatter plot


# In[16]:


np.cov(x, y)


# In[8]:


# method seaborn


# In[9]:


import seaborn as sns


# In[10]:


sns.scatterplot(x, y);


# In[14]:


sns.jointplot(x, y, kind = 'scatter');


# In[15]:


# method pandas


# In[11]:


import pandas as pd


# In[15]:


lst = zip(x, y)
print(list((lst)))
df = pd.DataFrame(lst, columns = ['x', 'y'])


# In[18]:


df.head()


# In[21]:


df.plot.scatter('x', 'y');


# In[22]:


# method changing linestyle in line plot


# In[23]:


plt.plot(x, y);


# In[24]:


plt.plot(x, y, marker = 'o', linestyle = ' ');


# In[28]:


# boxplot


# In[ ]:


# boxplot with matplotlib


# In[26]:


x


# In[27]:


plt.boxplot(x);


# In[30]:


arr1 = np.random.randint(100, 200, 100)


# In[31]:


arr1


# In[34]:


plt.boxplot(arr1);


# In[36]:


arr1=np.random.randint(100,200,100)
arr2=np.random.randint(1,50,5)
arr3=np.random.randint(300,350,5)
arr=np.append(arr1, arr2)
arr=np.append(arr, arr3)
plt.boxplot(arr);


# In[37]:


min(arr)


# In[38]:


max(arr)


# In[39]:


from scipy import stats


# In[40]:


stats.iqr(arr)


# In[41]:


np.percentile(arr, 25)


# In[42]:


np.percentile(arr, 75)


# In[43]:


np.median(arr)


# In[45]:


sns.boxplot(arr, orient = 'v');


# In[17]:


# corr and cov


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


temp=[93,84,82,78,98,70]
number_of_people=[13,10, 11, 8, 15, 9]


# In[3]:


np.cov(temp, number_of_people)[0, 1]


# In[4]:


np.corrcoef(temp, number_of_people)[0, 1]


# In[7]:


df = sns.load_dataset('tips')


# In[8]:


df.head()


# In[9]:


df.dtypes


# In[10]:


df.corr('pearson')


# In[11]:


df.corr()


# In[15]:


np.corrcoef(df['total_bill'], df['tip'])[0, 1]


# In[16]:


df['total_bill'].corr(df['tip'])


# In[21]:


sns.heatmap(tips.corr(), annot = True, cmap = 'RdYlGn');


# In[24]:


mpg = sns.load_dataset('mpg')


# In[25]:


sns.pairplot(mpg);

