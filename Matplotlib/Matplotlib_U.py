#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np


# In[4]:


x = np.linspace(0, 5, 11)


# In[5]:


y = x ** 2


# In[6]:


x


# In[7]:


y


# In[8]:


# Functional Method


# In[9]:


plt.plot(x, y)
# plt.show()   = print() for matplotlib


# In[10]:


plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[11]:


plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[12]:


plt.subplot(1, 2, 1)
plt.plot(x, y, 'k')

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')


# In[13]:


# Object-Oriented Method


# In[14]:


fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left bottom width height, 0-1,  relation to black canvas

axes.plot(x, y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')


# In[15]:


fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes1.set_title('LARGER PLOT')

axes2.plot(y, x)
axes2.set_title('SMALLER PLOT')


# In[16]:


fig = plt.figure()
plt.show()


# In[17]:


fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.plot(x, y)


# In[18]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)

# axes.plot(x, y)


# In[19]:


fig, axes = plt.subplots(nrows = 3, ncols = 3)

# axes.plot(x, y)
plt.tight_layout()


# In[20]:


axes


# In[21]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)

for current_ax in axes:
    current_ax.plot(x,y)


# In[22]:


axes


# In[23]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x, y)


# In[24]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)

axes[0].plot(x, y)
axes[0].set_title('First Plot')

axes[1].plot(y, x)
axes[1].set_title('Second Plot')

plt.tight_layout()


# In[25]:


# Figure size, DPI


# In[26]:


fig = plt.figure(figsize = (8, 2))      # figsize = width, height in inches

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)


# In[27]:


fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 2))

axes[0].plot(x, y)

axes[1].plot(y, x)

plt.tight_layout()


# In[28]:


fig


# In[29]:


fig.savefig('my_picture.png', dpi = 200, edgecolor = 'black', facecolor = 'w', transparent = True)
# default dpi is 100 it is about pixels


# In[30]:


fig = plt.figure(figsize = (8, 2)) 

ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('Title')
ax.set_ylabel('Y')
ax.set_xlabel('X')

ax.plot(x, x ** 2, label = 'X Squared')
ax.plot(x, x ** 3, label = 'X Cubed')
ax.legend()                              # it uses/refers labels in .plot
# ax.legend(loc=(0.1, 0.1))


# In[31]:


# setting colors, line width, line types


# In[32]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green')   # RGB Hex Code google for custom colors #FF8C00
plt.show()


# In[33]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green', linewidth = 3)       # default linewidth is 1, we can use lw instead of it.


# In[34]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green', linewidth = 3, alpha = 0.3)   # alpha for transparency dafault is 1


# In[35]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green', lw = 3, linestyle = '-.')       # default linestyle is solid, ls


# In[36]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green', lw = 3, ls = '-', marker = 'o')    # marker each value x/y


# In[37]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green', lw = 3, ls = '-', marker = 'o', markersize = 15,
       markerfacecolor = 'red') 


# In[38]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'green', lw = 3, ls = '-', marker = 'o', markersize = 15,
       markerfacecolor = 'red', markeredgewidth = 3, markeredgecolor = 'blue') 


# In[39]:


# ylim xlim


# In[40]:


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y, color = 'purple', lw = 2, ls = '--') 

ax.set_xlim([0 ,1])
ax.set_ylim([0, 2])


# In[ ]:




