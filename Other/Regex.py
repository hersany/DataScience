#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


import pandas as pd


# In[26]:


text = re.search('\d', 'A2')       # digits


# In[27]:


print(text)


# In[6]:


print(text.group())


# In[23]:


text = re.search('\D', '22a')      # non-digits
print(text.group())


# In[9]:


text = 'My phone number is 505-555-5555'


# In[19]:


output = re.search('(\d\d\d)-(\d\d\d)-(\d\d\d\d)', text)


# In[20]:


print(output.group())


# In[36]:


text = 'My phone number is 415-555-1212'


# In[37]:


output = re.search('(\d\d\d)-(\d\d\d-\d\d\d\d)', text)


# In[42]:


print(output.group(2))       # we make group with -


# In[45]:


print(output.group(1))


# In[46]:


text = 'My phone number is (415) 555-1212'


# In[49]:


output = re.search('(\(\d\d\d\)) (\d\d\d-\d\d\d\d)', text)


# In[50]:


print(output.group())


# In[51]:


value = '0 1, t 10, o 100.'


# In[56]:


output = re.findall('\d', value)
print(output)


# In[58]:


output = re.findall('\d\d', value)
print(output)


# In[59]:


output = re.findall('\d{1,3}', value)
print(output)


# In[64]:


phone = '2004-959-559 # This is Phone Number'
output = re.sub('\D', '', phone)             # replace except ('expression')  with ''
print(output)


# In[63]:


phone = '2004-959-559 # This is Phone Number'
output = re.sub('\D', '.', phone)
print(output)


# In[73]:


txt = 'hello world'

output = re.findall('^he', txt)

print(output)


# In[ ]:


# Pandas


# In[76]:


s = pd.Series(['a3', 'b4', 'c5'])            # extract numbers from pandas series

s.str.extract('(\d)')


# In[77]:


s = pd.Series(['a3', 'b4', 'c5'])           # extract letters from pandas series

s.str.extract('(\w)')


# In[78]:


s = pd.Series(['a3f', 'b4f', 'c5f'])        

s.str.extract('(\w\d)')


# In[81]:


s = pd.Series(['40 l/100 km (comb)',
        '38 l/100 km (comb)', '6.4 l/100 km (comb)',
       '8.3 kg/100 km (comb)', '5.1 kg/100 km (comb)',
       '5.4 l/100 km (comb)', '6.7 l/100 km (comb)',
       '6.2 l/100 km (comb)', '7.3 l/100 km (comb)',
       '6.3 l/100 km (comb)', '5.7 l/100 km (comb)',
       '6.1 l/100 km (comb)', '6.8 l/100 km (comb)',
       '7.5 l/100 km (comb)', '7.4 l/100 km (comb)',
       '3.6 kg/100 km (comb)', '0 l/100 km (comb)',
       '7.8 l/100 km (comb)'])


# In[95]:


s.str.extract('(\d\d|\d.\d|\d)')


# In[96]:


s = pd.Series(['40 l/100 km (comb)',
        '38 l/100 km (comb)', '6.4 l/100 km (comb)',
       '8.3 kg/100 km (comb)', '5.1 kg/100 km (comb)',
       '5.4 l/100 km (comb)', '6.7 l/100 km (comb)',
       '6.2 l/100 km (comb)', '7.3 l/100 km (comb)',
       '6.3 l/100 km (comb)', '5.7 l/100 km (comb)',
       '6.1 l/100 km (comb)', '6.8 l/100 km (comb)',
       '7.5 l/100 km (comb)', '7.4 l/100 km (comb)',
       '3.6 kg/100 km (comb)', '0 l/100 km (comb)',
       '7.8 l/100 km (comb)'])


# In[103]:


s.str.extract('(\d\d|\d.\d|\d).*(\d\d\d)')


# In[105]:


s = pd.Series(['06/2020\n\n4.9 l/100 km (comb)',
'11/2020\n\n166 g CO2/km (comb)',
'10/2019\n\n5.3 l/100 km (comb)',
'05/2022\n\n6.3 l/100 km (comb)',
'07/2019\n\n128 g CO2/km (comb)',
'06/2022\n\n112 g CO2/km (comb)',
'01/2022\n\n5.8 l/100 km (comb)',
'11/2020\n\n106 g CO2/km (comb)',
'04/2019\n\n105 g CO2/km (comb)',
'08/2020\n\n133 g CO2/km (comb)',
'04/2022\n\n133 g CO2/km (comb)'])


# In[108]:


s.str.extract('(\d\d).(\d{4})')


# In[109]:


s = pd.Series(['06/2020\n\n4.9 l/100 km (comb)',
'11/2020\n\n166 g CO2/km (comb)',
'10/2019\n\n5.3 l/100 km (comb)',
'05/2022\n\n6.3 l/100 km (comb)',
'07/2019\n\n128 g CO2/km (comb)',
'06/2022\n\n112 g CO2/km (comb)',
'01/2022\n\n5.8 l/100 km (comb)',
'11/2020\n\n106 g CO2/km (comb)',
'04/2019\n\n105 g CO2/km (comb)',
'08/2020\n\n133 g CO2/km (comb)',
'04/2022\n\n133 g CO2/km (comb)'])


# In[113]:


s.str.extract('(\d\d).(\d\d\d\d)\s\s(\d{3}|\d.\d)')


# In[ ]:




