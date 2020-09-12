#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# In[ ]:


# sns.set(style="darkgrid")   # it makes dark background, we can see grids.


# In[2]:


import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# In[4]:


diamonds=sns.load_dataset('diamonds')
exercise=sns.load_dataset('exercise')
flights=sns.load_dataset('flights')
geyser=sns.load_dataset('geyser')
iris=sns.load_dataset('iris')
penguins=sns.load_dataset('penguins')
planets=sns.load_dataset('planets')
mpg=sns.load_dataset('mpg')
tips = sns.load_dataset('tips')
titanic=sns.load_dataset('titanic')


# In[4]:


penguins.head()


# In[5]:


penguins.info()


# In[7]:


penguins.isnull().sum()


# In[8]:


penguins.dropna(inplace = True)


# In[9]:


penguins.isnull().sum()


# In[10]:


penguins.info()


# In[11]:


penguins.head()


# In[13]:


sns.distplot(penguins['body_mass_g'])


# In[27]:


sns.distplot(penguins['body_mass_g'], kde = False, hist_kws = dict(edgecolor = 'k', lw = 2))


# In[28]:


sns.distplot(penguins['body_mass_g'], kde = False, hist_kws = dict(edgecolor = 'k', lw = 2), bins = 20)


# In[29]:


sns.distplot(penguins['body_mass_g'], hist = False)


# In[30]:


sns.distplot(penguins['body_mass_g'], hist = False, rug = True)


# In[32]:


geyser.head()


# In[33]:


geyser.info()


# In[6]:


sns.set(style="darkgrid")


# In[7]:


sns.distplot(geyser['waiting'], kde = False)


# In[37]:


geyser['waiting'].mean()


# In[44]:


stats.mode(geyser['waiting'])[0][0]


# In[47]:


tips.head()


# In[48]:


tips.info()


# In[52]:


sns.jointplot(x = tips['total_bill'], y = tips['tip'], data = tips) 


# In[70]:


sns.scatterplot(x = 'total_bill', y = 'tip', data = tips) 


# In[71]:


# But adding 'hue' gives the error:
sns.scatterplot(x = 'total_bill', y = 'tip', hue = tips.time.tolist(), data = tips)


# In[72]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'reg')


# In[73]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')


# In[74]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'kde')


# In[75]:


mpg.head()


# In[76]:


mpg.info()


# In[77]:


mpg.drop('displacement', axis = 1, inplace = True)


# In[78]:


sns.pairplot(mpg)


# In[79]:


mpg.groupby('model_year')[['mpg']].mean()


# In[91]:


mpg.groupby('model_year')[['mpg']].mean().plot()


# In[100]:


mpg.groupby('model_year')[['mpg']].mean().plot.bar()


# In[101]:


mpg.groupby("model_year")["horsepower"].mean().plot()


# In[102]:


sns.pairplot(mpg, hue = 'cylinders')


# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# In[2]:


iris=sns.load_dataset('iris')
mpg=sns.load_dataset('mpg')
tips = sns.load_dataset('tips')
titanic=sns.load_dataset('titanic')


# In[3]:


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
df = pd.DataFrame(list(zip(labels, men_means, women_means)), columns =["labels", "men_means", "women_means"])
df.head()


# In[ ]:


#barplot


# In[4]:


sns.barplot(df['labels'], df['men_means'])


# In[5]:


plt.bar(df['labels'], df['men_means'])   # matplotlib version.


# In[7]:


sns.barplot('labels', 'men_means', data = df)


# In[9]:


# order method
sns.barplot('labels', 'men_means', order = ['G1', 'G5', 'G3', 'G2', 'G4'], data = df) 


# In[10]:


#auto-order method
sns.barplot('labels', 'men_means', order = df.sort_values('men_means')['labels'], data = df) 


# In[11]:


y=[59219,
 55466,
 47544,
 36443,
 35917,
 31991,
 27097,
 23030,
 20524,
 18523,
 18017,
 7920,
 7331,
 7201,
 5833]


# In[12]:


x= ['JavaScript',
 'HTML/CSS',
 'SQL',
 'Python',
 'Java',
 'Bash/Shel/PS',
 'C#',
 'PHP',
 'C++',
 'TypeScript',
 'C',
 'Other(s):',
 'Ruby',
 'Go',
 'Assembly']


# In[13]:


fig, ax = plt.subplots(figsize=(15, 7))
ax.bar(x, y)
ax.set_title("Most Popular Languages")
ax.set_ylabel('Number of People Who Use')
ax.set_xticklabels(x, rotation=45);


# In[14]:


fig, ax = plt.subplots(figsize=(15, 7))
sns.barplot(x, y)                         # sns.barplot(x, y, ax = ax)
ax.set_title("Most Popular Languages")
ax.set_ylabel('Number of People Who Use')
ax.set_xticklabels(x, rotation=45);


# In[15]:


tips.head()


# In[22]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips)   # if there is a statistical count there is a tab. (ci)
                                                        # default value is mean


# In[29]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips, ci = None)


# In[26]:


y=tips.groupby("sex").total_bill.mean()               # matplotlib version (mean)
x=tips.groupby("sex").total_bill.mean().index
fig, ax = plt.subplots()
ax.bar(x, y)


# In[31]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips, hue = 'smoker')


# In[34]:


tips.head()


# In[38]:


sns.barplot('day', 'tip', 'sex', tips, estimator=sum)


# In[39]:


sns.barplot('day', 'tip', 'sex', tips)      # default estimator value is mean


# In[40]:


mpg.head()


# In[42]:


sns.barplot('cylinders', 'horsepower', data = mpg)


# In[43]:


titanic.head()


# In[44]:


sns.barplot('class', 'age', 'sex', data = titanic)


# In[ ]:


# countplot


# In[45]:


tips.head()


# In[49]:


sns.set(style="darkgrid")
sns.countplot(x = 'sex', data = tips)   # = tips['sex'].value_counts()


# In[51]:


tips['sex'].value_counts().plot.bar()


# In[52]:


mpg.head()


# In[55]:


sns.countplot('model_year', data = mpg)


# In[68]:


#boxplot


# In[56]:


sns.boxplot('total_bill', data = tips)


# In[58]:


sns.boxplot('total_bill', data = tips, orient = 'v')


# In[59]:


sns.boxplot('day', 'total_bill', data = tips)


# In[69]:


#violinplot


# In[70]:


sns.violinplot('day', 'total_bill', data = tips)


# In[71]:


#stripplot


# In[72]:


sns.stripplot('day', 'total_bill', data = tips)


# In[73]:


# swarmplot


# In[74]:


sns.swarmplot('day', 'total_bill', data = tips)


# In[75]:


titanic.head()


# In[83]:


sns.swarmplot('class', 'age', 'survived', data = titanic)


# In[84]:


sns.swarmplot('origin', 'horsepower', 'cylinders', data = mpg)


# In[85]:


#catplot


# In[86]:


sns.catplot('sex', 'total_bill', data = tips, kind = 'bar')   # all in one


# In[87]:


sns.catplot('sex', 'total_bill', data = tips, kind = 'violin') 


# In[88]:


sns.catplot('sex', 'total_bill', data = tips, kind = 'strip') 


# In[89]:


sns.catplot('sex', 'total_bill', data = tips, kind = 'hist') 


# In[90]:


#pointplot


# In[91]:


sns.pointplot('sex', 'total_bill', data= tips)


# In[3]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# In[9]:


# heatmap


# In[4]:


flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
mpg=sns.load_dataset('mpg')


# In[6]:


flights.head()


# In[7]:


tips.corr()


# In[8]:


sns.heatmap(tips.corr())


# In[10]:


sns.heatmap(tips.corr(), annot = True)


# In[11]:


sns.heatmap(tips.corr(), annot = True, cmap = 'coolwarm')


# In[12]:


flights.head()


# In[13]:


flights.pivot_table('passengers', 'month', 'year')


# In[16]:


a = flights.pivot_table('passengers', 'month', 'year')


# In[17]:


sns.heatmap(a)


# In[22]:


plt.subplots(figsize=(15,10))
sns.heatmap(a, annot = True, fmt='g')


# In[23]:


mpg.head()


# In[24]:


mpg.corr()


# In[30]:


plt.subplots(figsize=(10,7))
sns.heatmap(mpg.corr(), annot = True, cmap = 'Blues');


# In[31]:


# Grids


# In[36]:


sns.pairplot(tips)


# In[34]:


sns.pairplot(tips, diag_kind = 'kde', hue = 'sex')


# In[37]:


# PairGrid


# In[39]:


sns.PairGrid(tips);


# In[41]:


g = sns.PairGrid(tips)
g.map(plt.scatter)


# In[46]:


g = sns.PairGrid(tips)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[47]:


# FacetGrid


# In[48]:


tips.head()


# In[51]:


g = sns.FacetGrid(tips, col = 'time', row = 'smoker')


# In[52]:


g = sns.FacetGrid(tips, col = 'time', row = 'smoker')
g.map(plt.hist, 'total_bill')                # numeric one total_bill, col and row conditions/states


# In[53]:


g = sns.FacetGrid(tips, col = 'time')
g.map(plt.hist, 'total_bill')


# In[54]:


g = sns.FacetGrid(tips, row = 'time')
g.map(plt.hist, 'total_bill')


# In[55]:


# lmplot      # regression plot


# In[56]:


tips.head()


# In[57]:


sns.lmplot('total_bill', 'tip', tips)


# In[63]:


sns.lmplot('total_bill', 'tip', tips, ci = 99)


# In[64]:


sns.lmplot('total_bill', 'tip', tips, ci = 99, hue = 'sex')


# In[65]:


# rows nad columns in lmplot


# In[68]:


sns.lmplot('total_bill', 'tip', tips, ci = 99, col = 'sex')


# In[69]:


sns.lmplot('total_bill', 'tip', tips, ci = 99, col = 'sex', row = 'smoker')


# In[ ]:


# aspect, height


# In[76]:


sns.lmplot('total_bill', 'tip', tips, ci = 99, col = 'sex', row = 'smoker', aspect = 1, height = 8)


# In[77]:


# style and color


# In[78]:


tips.head()


# In[79]:


sns.countplot('sex', data = tips)


# In[82]:


sns.set_style('dark')
sns.countplot('sex', data = tips)


# In[83]:


sns.set_style('darkgrid')
sns.countplot('sex', data = tips)


# In[86]:


sns.set_style('whitegrid')
sns.countplot('sex', data = tips)


# In[87]:


plt.style.use('ggplot')
sns.countplot('sex', data = tips)


# In[1]:


# spine removal         despine is frame


# In[10]:


plt.style.use('default')
sns.countplot('sex', data = tips)
sns.despine(left = True, top = False)           # True one is removed, False one is stay


# In[7]:


# figsize


# In[12]:


plt.subplots(figsize=(10,7))       # = plt.figure(figsize=(10,7)) 
sns.set_style('whitegrid')
sns.countplot('sex', data = tips)


# In[13]:


# context
# notebook(default), paper, talk, poster


# In[24]:


sns.set_context('notebook')
sns.countplot('sex', data = tips)


# In[23]:


sns.set_context('poster')
sns.countplot('sex', data = tips)


# In[ ]:


# color


# In[27]:


x= ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shel/PS', 'C#', 'PHP', 'C++', 'TypeScript',
 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
y=[59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]


# In[31]:


fig, ax = plt.subplots(figsize=(9, 4))
sns.set_context('notebook')
sns.barplot(x,y, palette=None)
ax.set_title("Most Popular Languages")
ax.set_ylabel('Number of People Who Use')
ax.set_xticklabels(x, rotation=45);


# In[32]:


fig, ax = plt.subplots(figsize=(9, 4))
sns.set_context('notebook')
sns.barplot(x,y, palette='seismic')                # matplotlib colormaps seismic etc.
ax.set_title("Most Popular Languages")
ax.set_ylabel('Number of People Who Use')
ax.set_xticklabels(x, rotation=45);


# In[34]:


fig, ax = plt.subplots(figsize=(9, 4))
sns.set_context('notebook')
sns.barplot(x,y, palette='magma')                # matplotlib colormaps seismic etc.
ax.set_title("Most Popular Languages")
ax.set_ylabel('Number of People Who Use')
ax.set_xticklabels(x, rotation=45);

