#!/usr/bin/env python
# coding: utf-8

# In[6]:


# missing values / outliers


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.DataFrame({'A':[1, 2, np.nan],
                  'B':[5, np.nan, np.nan],
                  'C':[1, 2, 3]})


# In[4]:


df


# In[5]:


df.dropna()


# In[7]:


df.dropna(axis = 1)


# In[8]:


df.dropna(thresh = 2)


# In[10]:


df.fillna(value = 'milk')


# In[11]:


V1 = np.array([2,3,5,np.NaN,7,1,np.NaN,10,14])
V2 = np.array([8,np.NaN,5,8,11,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,13,5,6,13,7,np.NaN,3,30])
df = pd.DataFrame(
        {"Var1" : V1,
         "Var2" : V2,
         "Var3" : V3}
)
df


# In[12]:


df.isnull()


# In[17]:


df.notnull()


# In[18]:


df.isnull().sum()


# In[19]:


df.notnull().sum()


# In[20]:


df['Var1'].isnull()


# In[21]:


df[df['Var1'].isnull()]


# In[31]:


df.isnull()


# In[41]:


df


# In[37]:


df.isnull().any(axis=0)


# In[39]:


df.isnull().all(axis=1)


# In[40]:


df.isnull().any(axis=1)


# In[42]:


df[df.isnull().any(axis=1)]


# In[43]:


df[~df.isnull().any(axis=1)]    # ~ means against


# In[44]:


# handle with missing values


# In[45]:


df.dropna()


# In[49]:


df.dropna(how = 'all')


# In[50]:


df.dropna(how = 'any')


# In[51]:


df['Var1']


# In[52]:


df['Var1'].fillna(0)


# In[53]:


df['Var1'].fillna(df['Var1'].mean())


# In[57]:


df.apply(lambda x : x.fillna(x.mean()))


# In[61]:


df.mean()


# In[62]:


df.fillna(df.mean())


# In[63]:


df.fillna({'Var1' : 6, 'Var2' : 6.16})


# In[65]:


#where


# In[66]:


df.where(pd.notnull(df), df.mean(), axis = 1)


# In[68]:


Var1 = np.array([1,3,6,np.NaN,7,1,9,np.NaN,15])
Var2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
Var3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
Var4 = np.array(["IT","IT","IT","HR","HR","HR","HR","IT","IT"])
df = pd.DataFrame(
        {"salary" : Var1,
         "Var2" : Var2,
         "Var3" : Var3,
         "department" : Var4}
)


# In[69]:


df


# In[71]:


df.groupby('department')['salary'].mean()


# In[72]:


df['salary'].fillna({0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9})


# In[73]:


df


# In[76]:


df.groupby('department')['salary'].transform('mean')


# In[75]:


df.salary.fillna(df.groupby('department')['salary'].transform('mean'))


# In[77]:


V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V4 = np.array(["IT",np.nan,"HR","HR","HR","HR",np.nan,"IT","HR"], dtype=object)
df = pd.DataFrame(
        {"salary" : V1,
        "department" : V4}
)
df


# In[78]:


df['department'].fillna(df['department'].mode()[0])         # fill missing values with mode of column


# In[80]:


df['department'].fillna(method = 'bfill')                  # back fill


# In[ ]:


#df['department'].fillna(a, method = 'ffill', limit = 200)   
#df['department'].fillna(b, method = 'ffill', limit = 100)  
#df['department'].fillna(a, method = 'ffill', limit = 100)  
#df['department'].fillna(c, method = 'ffill', limit = 100)  
#df['department'].fillna(a, method = 'ffill', limit = 100) 
#df['department'].fillna(b, method = 'ffill', limit = 200)  
#df['department'].fillna(c, method = 'ffill', limit = 100)  
#df['department'].fillna(a, method = 'ffill', limit = 100)  


# In[81]:


df['department'].fillna(method = 'ffill')                    # forward fill


# In[82]:


# outliers


# In[83]:


import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64'])
df = df.dropna()
df.head()


# In[84]:


sns.boxplot(df['table'])


# In[85]:


df_table = df['table']


# In[86]:


df_table.head()


# In[88]:


pd.DataFrame(df_table).info()


# In[96]:


q1 = df_table.quantile(0.25)
q3 = df_table.quantile(0.75)
iqr = q3 - q1


# In[97]:


q3


# In[98]:


q1


# In[99]:


iqr


# In[94]:


df.describe()


# In[128]:


lower_lim = q1 - 1.5 * iqr
upper_lim = q3 + 1.5 * iqr


# In[102]:


lower_lim


# In[103]:


upper_lim


# In[133]:


outliers_15_low = df_table < lower_lim


# In[134]:


outliers_15_up = df_table > upper_lim


# In[113]:


df_table[outliers_15_low]


# In[114]:


df_table[outliers_15_up]


# In[115]:


df_table[outliers_15_low | outliers_15_up]


# In[117]:


lower_lim = q1 - 2.5 * iqr
upper_lim = q3 + 2.5 * iqr


# In[118]:


df_table[(df_table < lower_lim) | (df_table > upper_lim)]


# In[119]:


#removing the outliers


# In[135]:


df_table[~(outliers_15_low | outliers_15_up)]


# In[138]:


clean_df = df[~(outliers_15_low | outliers_15_up)]


# In[139]:


clean_df                             # without ouliers (1.5)


# In[140]:


# limitation winsorize() method


# In[141]:


from scipy.stats.mstats import winsorize


# In[142]:


df


# In[144]:


df_table


# In[145]:


sns.boxplot(df['table'])


# In[146]:


sns.distplot(df['table'], kde = False, bins = 15)


# In[161]:


df_table_win = winsorize(df_table, (0.01, 0.02))      # % 1 from bottom % 2 from top


# In[158]:


df_table_win


# In[159]:


sns.distplot(df_table_win, kde = False, bins = 10)


# In[160]:


sns.boxplot(df_table_win)


# In[163]:


df['table'].describe()


# In[ ]:


df_table_win

