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


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[23]:


sal['OvertimePay'].sort_values(ascending = False)[1]


# In[75]:


sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[16]:


sal['JobTitle'][sal['EmployeeName'] == 'JOSEPH DRISCOLL']


# In[76]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[18]:


sal['TotalPayBenefits'][sal['EmployeeName'] == 'JOSEPH DRISCOLL']


# In[77]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[82]:


sal.sort_values(by = 'TotalPayBenefits', ascending = False).iloc[[0]]


# In[80]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]


# In[86]:


sal.loc[[sal['TotalPayBenefits'].idxmax()]]   # idxmax() is similar numpy argmax()


# In[87]:


sal.iloc[[sal['TotalPayBenefits'].argmax()]]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[32]:


sal.sort_values(by = 'TotalPayBenefits').iloc[[0]]


# In[89]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]


# In[93]:


sal.loc[[sal['TotalPayBenefits'].idxmin()]]


# In[95]:


sal.iloc[[sal['TotalPayBenefits'].argmin()]]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[40]:


sal['Year'].unique()


# In[113]:


sal.groupby('Year').mean()['BasePay']


# In[116]:


sal.groupby('Year').mean()['BasePay'][[2011, 2013]]


# ** How many unique job titles are there? **

# In[45]:


sal['JobTitle'].nunique()


# In[117]:


len(sal['JobTitle'].unique())


# ** What are the top 5 most common jobs? **

# In[48]:


sal['JobTitle'].value_counts()[:5]


# In[119]:


sal['JobTitle'].value_counts().head(5)


# In[120]:


type(sal['JobTitle'].value_counts())


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[126]:


sal[['JobTitle']][sal['Year'] == 2013].nunique()


# In[128]:


sal[['JobTitle']][sal['Year'] == 2013].value_counts() == 1


# In[129]:


sum(sal[['JobTitle']][sal['Year'] == 2013].value_counts() == 1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[151]:


sum(sal['JobTitle'].apply(str.lower).str.contains('chief'))


# In[159]:


sal['JobTitle'][sal['JobTitle'].apply(str.lower).str.contains('chief')].value_counts().index


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[71]:


title_len = sal['JobTitle'].apply(len)


# In[72]:


import numpy as np


# In[73]:


np.corrcoef(title_len, sal['TotalPayBenefits'])


# In[152]:


sal['title_len'] = sal['JobTitle'].apply(len)


# In[161]:


sal[['TotalPayBenefits', 'title_len']].corr('pearson')


# # Great Job!
