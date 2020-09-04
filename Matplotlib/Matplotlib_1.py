#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# Follow the instructions to recreate the plots using this data:
# 
# ## Data

# In[17]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**

# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Exercise 1
# 
# ** Follow along with these steps: **
# * ** Create a figure object called fig using plt.figure() **
# * ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# * ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

# In[18]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()


# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**

# In[4]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])


# ** Now plot (x,y) on both axes. And call your figure object to show it.**

# In[21]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax1.plot(x, y)

ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax2.plot(x, y)
plt.show()


# ## Exercise 3
# 
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**

# In[6]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])


# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

# In[22]:


fig = plt.figure()

ax1 = fig.add_axes([0, 0, 1, 1])
ax1.plot(x, z, 'green')
ax1.plot(x, y, 'blue')
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.set_xlim(0)
ax1.set_ylim(0)

ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])
ax2.plot(x, y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.set_xlim([20.0, 22.0])
ax2.set_ylim([30, 50])
plt.show()


# ## Exercise 4
# 
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

# In[8]:


fig, ax = plt.subplots(1, 2)


# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**

# In[9]:


fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y, 'b', lw = 2.5, ls = '--')
ax[0].set_xlim(0)
ax[0].set_ylim(0)

ax[1].plot(x, z, 'r', lw = 4)
ax[1].set_xlim(0)
ax[1].set_ylim(0)

plt.tight_layout()


# ** See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.**

# In[10]:


fig, ax = plt.subplots(1, 2, figsize = (10, 5))

ax[0].plot(x, y, 'b', lw = 2.5, ls = '--')
ax[0].set_xlim(0)
ax[0].set_ylim(0)

ax[1].plot(x, z, 'r', lw = 4)
ax[1].set_xlim(0)
ax[1].set_ylim(0)

plt.tight_layout()


# # Great Job!
