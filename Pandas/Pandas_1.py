#!/usr/bin/env python
# coding: utf-8

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[3]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[4]:


sal.info()


# **What is the average BasePay ?**

# In[11]:


sal['BasePay'].mean()


# In[10]:





# ** What is the highest amount of OvertimePay in the dataset ? **

# In[23]:


sal['OvertimePay'].sort_values(ascending = False)[1]


# In[11]:





# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[16]:


sal['JobTitle'][sal['EmployeeName'] == 'JOSEPH DRISCOLL']


# In[12]:





# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[18]:


sal['TotalPayBenefits'][sal['EmployeeName'] == 'JOSEPH DRISCOLL']


# In[13]:





# ** What is the name of highest paid person (including benefits)?**

# In[33]:


sal.sort_values(by = 'TotalPayBenefits', ascending = False).iloc[[0]]


# In[14]:





# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[32]:


sal.sort_values(by = 'TotalPayBenefits').iloc[[0]]


# In[34]:





# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[40]:


sal['Year'].unique()


# In[39]:


sal.groupby('Year').mean()['BasePay']


# In[41]:





# ** How many unique job titles are there? **

# In[45]:


sal['JobTitle'].nunique()


# In[17]:





# ** What are the top 5 most common jobs? **

# In[48]:


sal['JobTitle'].value_counts()[:5]


# In[18]:





# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[65]:


sal[['Id', 'JobTitle']][sal['Year'] == 2013].nunique()


# In[19]:





# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[64]:


sal[sal['JobTitle'].str.contains('Chief')].nunique()


# In[21]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[71]:


title_len = sal['JobTitle'].apply(len)


# In[72]:


import numpy as np


# In[73]:


np.corrcoef(title_len, sal['TotalPayBenefits'])


# In[23]:





# # Great Job!
