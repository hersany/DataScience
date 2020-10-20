#!/usr/bin/env python
# coding: utf-8

# # Aggregation & Groupby
# 
# The ``groupby`` method allows you to group rows of data together and call aggregate functions

# ### Basic aggregation methods:
# 
# * ``count()``   Compute count of group
# * ``mean()``    Compute mean of groups
# * ``median()``  Compute median of groups
# * ``min()``     Compute min of group values
# * ``max()``     Compute max of group values
# * ``std()``     Standard deviation of groups
# * ``var()``     Compute variance of groups
# * ``sum()``     Compute sum of group values
# * ``describe()``Generates descriptive statistics

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df = sns.load_dataset("planets")


# In[3]:


df


# In[5]:


df.head(2)


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df['mass']


# In[9]:


df["mass"].mean()


# In[10]:


df["mass"].count()


# In[11]:


df["mass"].min()


# In[12]:


df["mass"].max()


# In[13]:


df["mass"].sum()


# In[14]:


df["mass"].std()


# In[15]:


df["mass"].var()


# In[16]:


df.describe()


# In[18]:


df.describe().T


# In[17]:


df.describe().transpose()


#  - # ``df.groupby()``

# In[19]:


df.head()


# In[20]:


df.info()


# In[21]:


df['method'].unique()


# In[22]:


df['method'].nunique()


# In[26]:


df['mass'].value_counts(dropna = False)


# In[24]:


df["method"].value_counts()


# In[27]:


df.groupby("method")


# In[28]:


df.groupby("method").max()


# In[29]:


df.groupby("method").mean()


# In[30]:


df.groupby("method").mean()['distance']


# In[31]:


df.groupby("method").mean()[['distance']]


# In[33]:


df.groupby("method").describe()['year']


# In[34]:


df


# In[35]:


df.groupby('year')['distance'].sum()


# In[36]:


data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
       'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
       'Sales':[200, 120, 340, 124, 243, 350]}


# In[37]:


df1 = pd.DataFrame(data)


# In[38]:


df1


# In[39]:


df1.groupby('Company')[['Sales']].mean()


# In[40]:


df1.groupby('Company').min()


# In[41]:


df1.groupby('Company').sum()


#  - # ``DataFrame`` Operations

# - ### Common Operations 👈

# There are lots of operations with pandas that will be really useful to you, but don't fall into any distinct category. Let's show **Common Operations** here in this lecture:

# - Quick review and refresh

# In[42]:


df2 = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df2.head()


# ### Info on Unique Values

# In[43]:


df2["col2"].unique()


# In[44]:


df2["col2"].nunique()


# In[45]:


df2["col2"].value_counts()


# In[46]:


df['mass'].value_counts(dropna = False)


# ### Selecting Data

# In[47]:


df2


# In[48]:


df2['col1'] > 2


# In[49]:


df2[df2['col1'] > 2]


# In[50]:


df2[(df2['col1'] > 2) & (df2['col2'] == 444)]


# In[51]:


df2[(df2['col1']>2) | (df2['col2']==444)]


# **Get column and index names:**

# In[52]:


df2


# In[53]:


df2.columns


# In[54]:


df.columns


# In[55]:


df2.shape


# In[56]:


df2.index


# In[ ]:





# In[58]:


df4 = df.groupby("method")["distance"].describe()


# In[59]:


df4


# In[60]:


df4.index


# **Sorting and Ordering a DataFrame:**

# In[61]:


df2


# In[62]:


df2.sort_values(by = 'col2')


# In[63]:


df2.sort_values(by = 'col2', ascending = False, inplace = True)


# In[64]:


df2


# - ### `.transform()`
# - ### `.apply()`

# ### ``.transform()``

# In[65]:


df4 = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'var1': [10,23,33,22,11,99],
                   'var2': [100,253,333,262,111,969]})
df4


# In[66]:


df4["var1"]*9


# In[67]:


df_numeric = df4.iloc[:, 1:3]


# In[68]:


df_numeric


# In[69]:


df_numeric.transform(lambda x : (x-x.mean()) / x.std())


# In[70]:


df_numeric.iloc[0,0]


# In[71]:


(df_numeric.iloc[0,0] - df_numeric['var1'].mean()) / df_numeric['var1'].std()


# In[72]:


df_numeric.transform(lambda x : np.log10(x))


# In[73]:


df_numeric.transform(np.log10)


# ### ``.apply()``

# In[74]:


df4 = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'var1': [10,23,33,22,11,99],
                   'var2': [100,253,333,262,111,969]})
df4


# In[82]:


df4.apply('mean')


# In[76]:


df4['var1'].sum()


# In[77]:


df4['groups'].sum()


# In[84]:


df_numeric


# In[85]:


df_numeric.apply(np.median)


# In[ ]:


df_numeric


# In[87]:


df_numeric.apply(np.mean, axis = 1)


# In[88]:


df4


# In[89]:


df4.groupby("groups").apply(np.mean)


# In[90]:


df4.groupby("groups").mean()


# In[91]:


df2 = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abcc','de','ghi','xyzzz']})

df2


# In[92]:


def times2(x):
    return x * 2


# In[93]:


df2["col1"].apply(times2)


# In[94]:


df2["col3"].apply(len)


# ### `df.transform() vs df.apply()`

# In[95]:


df2


# In[96]:


df2.transform(len)


# In[97]:


df2["col3"].transform(len)


# In[98]:


df2.apply(len)


# In[99]:


df1 = pd.DataFrame([["a", 9, 25]] * 4, columns=["grp", 'P', 'Q'])
df2 = pd.DataFrame([["b", 9, 25]] * 3, columns=["grp", 'P', 'Q'])
df3 = pd.concat([df1, df2], ignore_index=True)
df3


# In[100]:


df3.apply(lambda x : x + x)


# In[101]:


df3.transform(lambda y : y + y)


# In[102]:


df3


# In[103]:


df3.groupby("grp").apply(sum)


# In[106]:


df3.groupby("grp").transform(np.mean)


# In[107]:


df3.groupby("grp").sum()


# In[108]:


df3


# In[109]:


df3.groupby("grp").transform(len)


# In[110]:


df3.iloc[0:4]


# In[111]:


len(df3.iloc[0:4])


# In[112]:


df3.groupby("grp").apply(len)


# ### Pivot Tables

# In[113]:


titanic = sns.load_dataset("titanic")


# In[114]:


titanic.head()


# In[115]:


titanic.groupby("sex")[["survived"]].mean()


# In[116]:


titanic.groupby(["sex", "class"])[["survived"]].mean()


# In[117]:


titanic.groupby(["sex", "class"])[["survived"]].mean().T


# In[118]:


titanic.groupby(["sex", "class"])[["survived"]].mean().unstack()


# In[ ]:





# ### Using pivot table

# - Create a spreadsheet-style pivot table as a ``DataFrame``.

# In[120]:


titanic.pivot_table(values = "survived", index = "sex", columns = "class", aggfunc = 'sum')


# In[ ]:


titanic.head(2)


# In[ ]:


titanic.pivot_table("age", index = "sex", columns = "class")


# In[ ]:


titanic.pivot_table("age", index = "class", columns = "sex")


# In[121]:


data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
       'B':['one', 'one', 'two', 'two', 'one', 'one'],
       'C':['x', 'y', 'x', 'y', 'x', 'y'],
       'D':[1, 3, 2, 5, 4, 1]}

df5 = pd.DataFrame(data)

df5


# In[122]:


df5.pivot_table(values = "D", index = ["A", "B"], columns = "C")


# # The End of the Session
