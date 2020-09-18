#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[6]:


df.dropna(axis = 1)


# In[7]:


df.dropna(thresh = 2)


# In[8]:


df.fillna(value = 'milk')


# In[9]:


V1 = np.array([2,3,5,np.NaN,7,1,np.NaN,10,14])
V2 = np.array([8,np.NaN,5,8,11,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,13,5,6,13,7,np.NaN,3,30])
df = pd.DataFrame(
        {"Var1" : V1,
         "Var2" : V2,
         "Var3" : V3}
)
df


# In[10]:


df.isnull()


# In[11]:


df.notnull()


# In[12]:


df.isnull().sum()


# In[13]:


df.notnull().sum()


# In[14]:


df['Var1'].isnull()


# In[15]:


df[df['Var1'].isnull()]


# In[16]:


df.isnull()


# In[17]:


df


# In[18]:


df.isnull().any(axis=0)


# In[19]:


df.isnull().all(axis=1)


# In[20]:


df.isnull().any(axis=1)


# In[21]:


df[df.isnull().any(axis=1)]


# In[22]:


df[~df.isnull().any(axis=1)]    # ~ means against


# In[23]:


# handle with missing values


# In[24]:


df.dropna()


# In[25]:


df.dropna(how = 'all')


# In[26]:


df.dropna(how = 'any')


# In[27]:


df['Var1']


# In[28]:


df['Var1'].fillna(0)


# In[29]:


df['Var1'].fillna(df['Var1'].mean())


# In[30]:


df.apply(lambda x : x.fillna(x.mean()))


# In[31]:


df.mean()


# In[32]:


df.fillna(df.mean())


# In[33]:


df.fillna({'Var1' : 6, 'Var2' : 6.16})


# In[34]:


#where


# In[35]:


df.where(pd.notnull(df), df.mean(), axis = 1)


# In[36]:


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


# In[37]:


df


# In[38]:


df.groupby('department')['salary'].mean()


# In[39]:


df['salary'].fillna({0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9})


# In[40]:


df


# In[41]:


df.groupby('department')['salary'].transform('mean')


# In[42]:


df.salary.fillna(df.groupby('department')['salary'].transform('mean'))


# In[43]:


V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V4 = np.array(["IT",np.nan,"HR","HR","HR","HR",np.nan,"IT","HR"], dtype=object)
df = pd.DataFrame(
        {"salary" : V1,
        "department" : V4}
)
df


# In[44]:


df['department'].fillna(df['department'].mode()[0])         # fill missing values with mode of column


# In[45]:


df['department'].fillna(method = 'bfill')                  # back fill


# In[46]:


#df['department'].fillna(a, method = 'ffill', limit = 200)   
#df['department'].fillna(b, method = 'ffill', limit = 100)  
#df['department'].fillna(a, method = 'ffill', limit = 100)  
#df['department'].fillna(c, method = 'ffill', limit = 100)  
#df['department'].fillna(a, method = 'ffill', limit = 100) 
#df['department'].fillna(b, method = 'ffill', limit = 200)  
#df['department'].fillna(c, method = 'ffill', limit = 100)  
#df['department'].fillna(a, method = 'ffill', limit = 100)  


# In[47]:


df['department'].fillna(method = 'ffill')                    # forward fill


# In[48]:


# outliers


# In[49]:


import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64'])
df = df.dropna()
df.head()


# In[50]:


sns.boxplot(df['table'])


# In[51]:


df_table = df['table']


# In[52]:


df_table.head()


# In[53]:


pd.DataFrame(df_table).info()


# In[54]:


q1 = df_table.quantile(0.25)
q3 = df_table.quantile(0.75)
iqr = q3 - q1


# In[55]:


q3


# In[56]:


q1


# In[57]:


iqr


# In[58]:


df.describe()


# In[59]:


lower_lim = q1 - 1.5 * iqr
upper_lim = q3 + 1.5 * iqr


# In[60]:


lower_lim


# In[61]:


upper_lim


# In[62]:


outliers_15_low = df_table < lower_lim


# In[63]:


outliers_15_up = df_table > upper_lim


# In[64]:


df_table[outliers_15_low]


# In[65]:


df_table[outliers_15_up]


# In[66]:


df_table[outliers_15_low | outliers_15_up]


# In[67]:


lower_lim = q1 - 2.5 * iqr
upper_lim = q3 + 2.5 * iqr


# In[68]:


df_table[(df_table < lower_lim) | (df_table > upper_lim)]


# In[69]:


#removing the outliers


# In[70]:


df_table[~(outliers_15_low | outliers_15_up)]


# In[71]:


clean_df = df[~(outliers_15_low | outliers_15_up)]


# In[72]:


clean_df                             # without ouliers (1.5)


# In[73]:


# limitation winsorize() method


# In[74]:


from scipy.stats.mstats import winsorize


# In[75]:


df


# In[76]:


df_table


# In[77]:


sns.boxplot(df['table'])


# In[78]:


sns.distplot(df['table'], kde = False, bins = 15)


# In[79]:


df_table_win = winsorize(df_table, (0.01, 0.02))      # % 1 from bottom % 2 from top


# In[80]:


df_table_win


# In[81]:


sns.distplot(df_table_win, kde = False, bins = 10)


# In[82]:


sns.boxplot(df_table_win)


# In[83]:


df['table'].describe()


# In[86]:


df_table_win = pd.DataFrame(df_table_win)[0]


# In[87]:


df_table_win.describe()


# In[92]:


df['table'].sort_values().head(20)


# In[93]:


df_table_win.sort_values().head(20)    # scale values


# In[94]:


df_table_win[11368]


# In[95]:


df['table'][11368]


# In[96]:


df_table_win[24815]


# In[97]:


df['table'][24815]


# In[100]:


df_table_win[df_table_win == 53]


# In[99]:


df_table[df_table == 53]


# In[103]:


df_table_win[df_table_win == 63]           # 1180 - 563. because right skewed.
                                           # upper outliers are more than lower. 0.02 from uuper side.


# In[104]:


df_table[df_table == 63]


# In[107]:


q1


# In[106]:


q3


# In[108]:


iqr


# In[111]:


lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr


# In[112]:


lower


# In[113]:


upper


# In[114]:


outliers_15 = (df_table_win < lower) | (df_table_win > upper)


# In[116]:


df_table_win[outliers_15]


# In[117]:


df_table[(df_table < lower) | (df_table > upper)]


# In[131]:


df['table_win'] = df_table_win


# In[119]:


# log() transformation


# In[132]:


df.info()


# In[122]:


df_carat = df['carat']


# In[123]:


df_carat.head()


# In[124]:


sns.boxplot(df_carat)


# In[127]:


sns.distplot(df_carat, bins = 15, kde = False)


# In[128]:


df_carat_log = np.log(df_carat)


# In[129]:


sns.distplot(df_carat_log, bins = 15, kde = False)


# In[130]:


sns.boxplot(df_carat_log)


# In[133]:


df['carat_log'] = np.log(df['carat'])


# In[134]:


df.head()


# In[1]:


import pandas as pd


# In[2]:


df1 = pd.DataFrame({'lkey': ['x', 'y', 'z', 'c', 'z','x'],
                    'lvalue': [2, 3, 5, 7, 0, 99]})
df2 = pd.DataFrame({'rkey': ['x', 'x', 'z', 'z'],
                    'rvalue': [7, 8, 9, 10]})


# In[3]:


df1


# In[4]:


df2


# In[5]:


pd.merge(df1, df2, left_on = 'lkey', right_on = 'rkey', how = 'left')

