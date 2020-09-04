#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt


# In[10]:


age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]
salary = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


# In[11]:


# Functional


# In[12]:


plt.plot(age, salary);   # ; = plt.show()


# In[8]:


plt.plot(age, salary)
plt.xlabel('age')
plt.ylabel('salary')
plt.title('Salary by Age');


# In[14]:


salary_2 = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


# In[10]:


plt.plot(age, salary)
plt.plot(age, salary_2)
plt.xlabel('age')
plt.ylabel('salary')
plt.title('Salary by Age');


# In[13]:


plt.plot(age, salary, label = 'Turkey')
plt.plot(age, salary_2, label = 'Europe')
plt.xlabel('age')
plt.ylabel('salary')
plt.title('Salary by Age')
plt.legend();


# In[23]:


plt.subplot(2, 1, 1)
plt.plot(age, salary, 'r')

plt.subplot(2, 1, 2)
plt.plot(age, salary_2, 'b')

plt.tight_layout()


# In[15]:


import pandas as pd
df = pd.DataFrame(list(zip(age, salary, salary_2)), columns =['age', 'salary', 'salary_2'])
df.head()


# In[26]:


df['salary']


# In[25]:


plt.plot(df['salary']);        # index and salary


# In[17]:


plt.plot(df['age'], df['salary']);         # age and salary


# In[28]:


# OOP


# In[20]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 0.8, 0.8])


# In[32]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(age, salary, 'r')
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
ax.set_title('Salary by Age');


# In[34]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0, 0.8, 0.8])

ax1.plot(age, salary, 'r')
ax1.set_xlabel('Age')
ax1.set_ylabel('Salary')
ax1.set_title('Salary by Age')

ax2 = fig.add_axes([1, 0.1, 0.4, 0.4])

ax2.plot(age, salary_2, 'b')
ax2.set_xlabel('Age')
ax2.set_ylabel('Salary2')
ax2.set_title('Salary2 by Age');


# In[46]:


ax1


# In[47]:


ax2


# In[48]:


fig


# In[49]:


fig, ax = plt.subplots()


# In[56]:


fig, ax = plt.subplots()         # default 1 row 1 column

ax.plot(age, salary, 'r')
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
ax.set_title('Salary by Age')
plt.tight_layout()


# In[37]:


fig, ax = plt.subplots(2, 1)         

ax[0].plot(age, salary, 'r')
ax[0].set_xlabel('Age')
ax[0].set_ylabel('Salary')
ax[0].set_title('Salary by Age')

ax[1].plot(age, salary_2, 'b')
ax[1].set_xlabel('Age')
ax[1].set_ylabel('Salary2')
ax[1].set_title('Salary2 by Age')
plt.tight_layout()


# In[74]:


fig, ax = plt.subplots(2, 2)
plt.tight_layout()


# In[73]:


ax


# In[75]:


fig


# In[79]:


fig, ax = plt.subplots(1, 2)

ax[0].plot(age, salary)
ax[0].set_title('First Plot')
ax[0].set_xlabel('Age')
ax[0].set_ylabel('Salaries')

ax[1].plot(age, salary_2)
ax[1].set_title('Second Plot')
ax[1].set_xlabel('Age')

plt.tight_layout()


# In[84]:


fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(age, salary)
ax[0, 0].set_title('First Plot')
ax[0, 0].set_xlabel('Age')
ax[0, 0].set_ylabel('Salaries')

ax[0, 1].plot(age, salary)
ax[0, 1].set_title('Second Plot')
ax[0, 1].set_xlabel('Age')
ax[0, 1].set_ylabel('Salaries')

ax[1, 0].plot(age, salary_2)
ax[1, 0].set_title('Third Plot')
ax[1, 0].set_xlabel('Age')
ax[1, 0].set_ylabel('Salaries')

ax[1, 1].plot(age, salary_2)
ax[1, 1].set_title('Fourth Plot')
ax[1, 1].set_xlabel('Age')
ax[1, 1].set_ylabel('Salaries')

plt.tight_layout()


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]
salary = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
salary_2 = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


# In[7]:


import pandas as pd
df = pd.DataFrame(list(zip(age, salary, salary_2)), columns =['age', 'salary', 'salary_2'])


# In[9]:


df.head()


# In[10]:


fig = plt.figure(figsize = (8, 4))


# In[11]:


fig, ax = plt.subplots(figsize = (8, 4))


# In[13]:


fig, ax = plt.subplots(figsize = (6, 3))
ax.plot(age, salary, 'r')
ax.set_xlabel('age')
ax.set_ylabel('salary')
ax.set_title('title');


# In[39]:


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(6,3))
ax[0].plot(age, salary)
ax[0].set_xlabel('age')
ax[1].plot(age, salary_2)
ax[0].set_title('First')
ax[1].set_title('Second')
ax[1].set_xlabel('age')
plt.tight_layout()


# In[15]:


fig.savefig('myplot')


# In[ ]:


# legend, label, title


# In[40]:


fig, ax = plt.subplots(figsize=(6,3))
ax.plot(age, salary, label = 'salary_1')
ax.set_xlabel('Age')
ax.plot(age, salary_2, label = 'salary_2')
ax.set_title('Title')
ax.set_ylabel('Salaries')
ax.legend(loc = 0)
plt.tight_layout()


# In[41]:


# setting colors, linewidths, linetypes, marker


# In[61]:


fig, ax = plt.subplots(figsize=(6,3))
ax.plot(age, salary, 'y', lw = 2, ls = ':', marker = '*', ms = 10, mfc = 'b', alpha = 0.3);


# In[62]:


# plot range (xlim - ylim)


# In[80]:


fig, ax = plt.subplots(figsize=(6,3))
ax.plot(age, salary)
ax.set_xlim([30, 40])
ax.set_ylim([45000, 60000]);


# In[66]:


# adding vertical-horizontal lines


# In[56]:


fig, ax = plt.subplots(figsize=(6,3))
ax.plot(age, salary)
ax.set_xlim([30, 40])
ax.set_ylim([45000, 60000])
ax.axvline(35)
ax.axhline(50000, color = 'red');


# In[60]:


import numpy as np
np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
p =  plt.plot(x, y, "o")
plt.vlines(70,100,250)
plt.hlines(100, 0, 100)


# In[82]:


# Plot types


# In[83]:


# Bar chart


# In[84]:


country = ['UK', 'USA', 'FRA', 'GER', 'NOR']
pci = [40000, 50000, 38000, 55000, 80000]


# In[85]:


fig, ax = plt.subplots()
ax.bar(country, pci)


# In[86]:


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]


# In[89]:


fig, ax = plt.subplots()
ax.bar(labels, men_means)


# In[94]:


fig, ax = plt.subplots()
ax.bar(labels, women_means, color = 'orange');


# In[95]:


x = np.arange(len(labels))
width = 0.35


# In[96]:


fig, ax = plt.subplots()
ax.bar(x - width/2, men_means, width, label='Men')
ax.bar(x + width/2, women_means, width, label='Women')


# In[98]:


fig, ax = plt.subplots()
ax.bar(x - width/2, men_means, width, label='Men')
ax.bar(x + width/2, women_means, width, label='Women')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


# In[105]:


age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]


fig, ax = plt.subplots(figsize = (8, 4))

ax.plot(age, salary)
ax.set_xticks([25, 30, 35, 40, 45]);


# In[107]:


import pandas as pd
df = pd.DataFrame(list(zip(labels, men_means, women_means)), columns =["labels", "men_means", "women_means"])
df.head()


# In[110]:


df.plot.bar(stacked = True)

