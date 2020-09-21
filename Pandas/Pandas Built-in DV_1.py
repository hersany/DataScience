#!/usr/bin/env python
# coding: utf-8

# # Pandas Data Visualization Exercise
# 
# This is just a quick exercise for you to review the various plots we showed earlier. Use **df3** to replicate the following plots. 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df3.info()


# In[3]:


df3.head()


# ** Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size. See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...**

# In[39]:


df3.plot.scatter('a', 'b', figsize = (12, 3), c = 'red', s = 50)


# ** Create a histogram of the 'a' column.**

# In[20]:


df3['a'].hist()


# ** These plots are okay, but they don't look very polished. Use style sheets to set the style to 'ggplot' and redo the histogram from above. Also figure out how to add more bins to it.***

# In[43]:


plt.style.use('ggplot')
df3['a'].hist(bins = 20, alpha = 0.5)


# ** Create a boxplot comparing the a and b columns.**

# In[44]:


df3[['a', 'b']].plot.box()


# In[46]:


df3[['a', 'b']].boxplot()


# ** Create a kde plot of the 'd' column **

# In[26]:


df3['d'].plot.kde()


# ** Figure out how to increase the linewidth and make the linestyle dashed. (Note: You would usually not dash a kde plot line)**

# In[48]:


df3['d'].plot.kde(lw = 5, ls = ':')


# In[49]:


df3['d'].plot.density(lw = 5, ls = ':')


# ** Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).**

# In[50]:


df3.loc[0:30].plot.area(alpha = 0.4)


# Note, you may find this really hard, reference the solutions if you can't figure it out!
# ** Notice how the legend in our previous figure overlapped some of actual diagram. Can you figure out how to display the legend outside of the plot as shown below?**
# 
# ** Try searching Google for a good stackoverflow link on this topic. If you can't find it on your own - [use this one for a hint.](http://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas)**

# In[56]:


df3.loc[0:30].plot.area(alpha = 0.4)
plt.legend(loc = 'center left', bbox_to_anchor = (1., 0.5))


# # Great Job!
