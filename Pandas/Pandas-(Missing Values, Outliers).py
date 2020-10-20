#!/usr/bin/env python
# coding: utf-8

# # Missing Values & Outliers

# - # Handling with Missing Values

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'A':[1, 2, np.nan],
                  'B':[5, np.nan, np.nan],
                  'C':[1, 2, 3]})


# In[3]:


df


# In[4]:


df.dropna()


# In[5]:


df.dropna(axis = 1)


# In[6]:


df


# In[8]:


df.dropna(thresh = 1)


# In[9]:


df.fillna(value = "xxx")


# In[10]:


df['A']


# In[11]:


df['A'].mean()


# In[12]:


df["A"].fillna(value = df["A"].mean())


# In[ ]:


df


# In[13]:


V1 = np.array([2,3,5,np.NaN,7,1,np.NaN,10,14])
V2 = np.array([8,np.NaN,5,8,11,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,13,5,6,13,7,np.NaN,3,30])
df = pd.DataFrame(
        {"Var1" : V1,
         "Var2" : V2,
         "Var3" : V3}        
)

df


# In[14]:


df.isnull()


# In[16]:


df.notnull()


# In[15]:


df.isnull().sum()


# In[17]:


df.notnull().sum()


# In[18]:


df.isnull().sum().sum()


# In[19]:


df


# In[20]:


df['Var1'].isnull()


# In[21]:


df['Var1'][df['Var1'].isnull()]


# In[ ]:


df


# ### Missing Values Handling Methods

#  - #### Dropping

# In[22]:


df


# In[23]:


df.dropna()


# In[24]:


df.dropna(how = "all")


# In[26]:


df


# In[25]:


df.dropna(axis = 1)


# In[27]:


df


# In[28]:


df.dropna(axis = 1, how = "all")


# In[29]:


df["delete_me"] = np.nan


# In[30]:


df


# In[31]:


df.dropna(axis = 1, how = "all", inplace = True)


# In[32]:


df


#  - #### Filling

# In[33]:


df


#  - Filling with a specific value

# In[34]:


df["Var1"]


# In[35]:


df["Var1"].fillna(0)


# In[36]:


df.fillna(value = 0)


#  - Filling with any Proper Value

# In[37]:


df


# In[38]:


df["Var1"].mean()


# In[39]:


df["Var1"].fillna(value = df["Var1"].mean())


# In[40]:


df


# In[44]:


df['Var2'].mean()


# In[55]:


df.apply(lambda x : x.fillna(value = x.mean()))


# In[47]:


df.mean()


# In[46]:


df.fillna(df.mean())


# In[48]:


df


# In[49]:


df.fillna({"Var1" : 6, "Var2": 6.16})


# In[56]:


df["Var3"].fillna(df["Var3"].median())


#  - Filling with any Proper Value Regarding to Group of the Categorical Variables 

# In[57]:


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

df


# In[58]:


df.groupby("department")["salary"].mean()


# In[59]:


df.groupby("department")["salary"].transform(np.mean)


# In[60]:


df.groupby("department")["salary"].apply(np.mean)


# In[61]:


df["salary"].fillna(value = df.groupby("department")["salary"].transform(np.mean))


# In[62]:


df["salary"].fillna(value = df.groupby("department")["salary"].apply(np.mean))


# In[63]:


df.salary.fillna({0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9})


#  - Filling the Missing Values of Categorical Values

# In[64]:


V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V4 = np.array(["IT",np.nan,"HR","HR","HR","HR",np.nan,"IT","HR"], dtype=object)

df = pd.DataFrame(
        {"salary" : V1,
        "department" : V4}        
)

df


# In[65]:


df["department"].mode()[0]


# In[66]:


df["department"].fillna(df["department"].mode()[0])


# In[67]:


df


# In[68]:


df["department"].fillna(method = "bfill")


# In[69]:


df["department"].fillna(method = "ffill")


# In[70]:


df


# In[71]:


df.drop('department', axis = 1)


# In[72]:


df.drop(index = 1)


# In[ ]:


#df.farazi.fillna(method = "ffill", limit = 2)
#df.farazi.fillna(method = "bfill", limit = 2)


# In[ ]:


#df.fillna(value = "unique1", limit=10, inplace=True)
#df.fillna("unique2", limit=30, inplace=True)
#df.fillna("unique3", limit=25, inplace=True)
#df.fillna("unique4", limit=35, inplace=True)


# In[73]:


df = pd.DataFrame({"A":[None, 1, 2, 3, None, None],  
                   "B":[11, 5, None, None, None, 8], 
                   "C":[None, 5, 10, 11, None, 8]}) 


# In[74]:


df


# In[82]:


df.fillna(method = "ffill", limit = 2)


#  - # Handling with Outliers

# ## Catching and Detecting Outliers

# In[83]:


import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64']) 
df = df.dropna()
df.head()


# In[84]:


import matplotlib.pyplot as plt


# In[85]:


plt.figure(figsize=(20,15))
sns.boxplot(x = df['table'])


# In[86]:


df['table'].describe()


# In[87]:


df_table = df["table"]


# In[88]:


df_table.head()


# In[89]:


pd.DataFrame(df_table).info()


# In[90]:


len(df_table)


# ## Tukey's Fences | Tukey's Rule

# - First way of specifying ``Q1 & Q3`` is using the ``.quantile()`` method

# In[91]:


df_table.describe()


# In[178]:


df_table.quantile(0.25)


# In[93]:


Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3 - Q1


# In[94]:


Q1


# In[95]:


Q3


# In[96]:


IQR


# - Second way of specifying ``Q1 & Q3`` is using the ``.describe()`` method

# In[97]:


lower_lim = Q1 - 1.5 * IQR
upper_lim = Q3 + 1.5 * IQR


# In[98]:


lower_lim


# In[99]:


upper_lim


# In[100]:


(df_table < lower_lim)


# In[101]:


(df_table > upper_lim)


# In[102]:


outliers_15_low = (df_table < lower_lim)


# In[103]:


outliers_15_up = (df_table > upper_lim)


# In[104]:


df_table[outliers_15_low]


# In[105]:


len(df_table[outliers_15_low])


# In[106]:


df_table[outliers_15_up]


# In[107]:


len(df_table) - (len(df_table[outliers_15_low]) + len(df_table[outliers_15_up]))


# In[108]:


df_table[(outliers_15_low | outliers_15_up)]


# ***

# In[109]:


lower_lim = Q1 - 2.5 * IQR
upper_lim = Q3 + 2.5 * IQR


# In[110]:


lower_lim


# In[111]:


upper_lim


# In[112]:


(df_table < lower_lim) | (df_table > upper_lim)


# In[113]:


outliers_25 = (df_table < lower_lim) | (df_table > upper_lim)


# In[114]:


df_table[outliers_25]


# ### Removing the Outliers

# In[121]:


df_table[~(outliers_15_low | outliers_15_up)]


# In[117]:


df


# In[123]:


clean_df = df[~(outliers_15_low | outliers_15_up)]


# In[119]:


clean_df


# ### Limitation and Transformation of the Outliers

# - ### Limitation using ``.winsorize()`` method

# In[124]:


from scipy.stats.mstats import winsorize


# In[127]:


df


# In[128]:


df_table


# In[129]:


sns.boxplot(x = df_table)


# In[130]:


sns.distplot(df_table, bins = 15, kde = False)


# In[176]:


df_table.describe()


# In[125]:


df_table.quantile(0.01)


# In[126]:


df_table.quantile(0.98)


# In[131]:


df_table_win = winsorize(df_table, (0.01, 0.02))


# In[132]:


df_table_win


# In[133]:


sns.boxplot(x = df_table_win)


# In[134]:


sns.distplot(df_table_win, bins = 10, kde =False)


# In[135]:


pd.DataFrame(df_table_win)


# In[136]:


pd.DataFrame(df_table_win)[0]


# In[137]:


df_table_win = pd.DataFrame(df_table_win)[0]


# In[139]:


df_table_win.describe()


# In[138]:


df_table.describe()


# In[ ]:


df_table.quantile(0.01)


# In[140]:


df_table.quantile(0.98)


# In[ ]:


df_table_win.describe()


# In[141]:


df_table.sort_values().head(20)


# In[147]:


df_table_win.sort_values().head(50)


# In[143]:


df_table_win[df_table_win == 53]


# In[144]:


df_table[df_table == 53]


# In[145]:


df_table_win[df_table_win == 63]


# In[146]:


df_table[df_table == 63]


# In[149]:


Q1 = 56.0
Q3 = 59.0


# In[150]:


IQR = Q3 - Q1


# In[151]:


lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR


# In[152]:


lower


# In[153]:


upper


# In[154]:


outliers_15 = (df_table_win < lower) | (df_table_win > upper)


# In[155]:


df_table[outliers_15]


# In[156]:


df["table_win"] = df_table_win


# In[157]:


df.head()


# - ### ``log()`` Transformation

# In[158]:


df.info()


# In[159]:


df_carat = df["carat"]


# In[160]:


df_carat.shape


# In[161]:


df_carat.head()


# In[162]:


sns.boxplot(x = df_carat)


# In[163]:


sns.distplot(df_carat, bins = 15, kde = False)


# In[164]:


df_carat_log = np.log(df_carat)


# In[166]:


df_carat


# In[165]:


df_carat_log


# In[167]:


sns.boxplot(x = df_carat_log)


# In[174]:


sns.distplot(df_carat_log, bins = 11, kde = False)


# In[ ]:


df["carat_log"] = np.log(df["carat"])


# In[ ]:


df.head()

