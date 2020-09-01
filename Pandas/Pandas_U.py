#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a' : 10, 'b' : 20, 'c' : 30}


# In[4]:


pd.Series(data = my_data)       # Series --> index and one column (data)


# In[5]:


pd.Series(data = my_data, index = labels)   


# In[6]:


pd.Series(my_data, labels)


# In[7]:


pd.Series(d)        # it takes dict keys as a index, values for data


# In[8]:


pd.Series(arr)         # we can use numpy arrays like python lists


# In[9]:


pd.Series(labels)


# In[10]:


ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan']) 


# In[11]:


ser1


# In[12]:


ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])


# In[13]:


ser2


# In[14]:


ser1['USA']


# In[15]:


ser3 = pd.Series(data = labels)


# In[16]:


ser3


# In[17]:


ser3[0]


# In[18]:


ser1 + ser2


# In[19]:


# DataFrames


# In[20]:


from numpy.random import randn


# In[21]:


np.random.seed(101)


# In[22]:


df = pd.DataFrame(randn(5, 4))


# In[23]:


df


# In[24]:


df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])


# In[25]:


df            # df is a bunch of series


# In[26]:


df['W']    # it gives series ('W' column)    bracket notation to reach column


# In[27]:


type(df['W'])


# In[28]:


type(df)


# In[29]:


df[['W', 'Z']]         # bracket notation to reach columns list in list it gives dataframe


# In[30]:


df['new'] = df['W'] + df['Y']       # add new column by concatenate


# In[31]:


df


# In[32]:


df.drop('new', axis = 1)        # default is axis0. it deletes column.


# In[33]:


df                # we need to use inplace argument to make changes permanently


# In[34]:


df.drop('new', axis = 1, inplace = True)    # inplace = True needed to make changes permanently. Default False


# In[35]:


df


# In[36]:


df.drop('E')


# In[37]:


df


# In[38]:


df.shape


# In[39]:


# Selecting Rows  loc, iloc


# In[40]:


df


# In[41]:


df.loc['A']       # rows are series too


# In[42]:


type(df.loc['A'])


# In[43]:


df.iloc[2]  # = df.loc['C']


# In[44]:


df.loc['C']    # = df.iloc[2]


# In[45]:


df.loc['B','Y']


# In[46]:


df.loc['B']['Y']


# In[47]:


df


# In[48]:


df.loc['A' : 'C']


# In[49]:


df.iloc[0 : 2]


# In[50]:


df


# In[51]:


df.loc[['A', 'B'],['W', 'Y']]


# In[52]:


df


# In[53]:


df > 0


# In[54]:


booldf = df > 0


# In[55]:


df[booldf]


# In[56]:


df[df > 0]


# In[57]:


df['W'] > 0


# In[58]:


df['W']


# In[59]:


df[df['W'] > 0]


# In[60]:


df


# In[61]:


df[df['Z'] < 0]


# In[62]:


resultdf = df[df['X'] < 1]


# In[63]:


resultdf


# In[64]:


resultdf['W']


# In[65]:


df[df['X'] < 1]['W']


# In[66]:


df[df['X'] < 1][['W', 'Z']]


# In[67]:


df


# In[68]:


df[(df['Z'] > 0) & (df['Y'] > 0)]


# In[69]:


df[(df['Z'] > 0) | (df['Y'] > 0)]


# In[70]:


df


# In[71]:


df.reset_index()


# In[72]:


newind = 'CA NY WR OR CO'.split()


# In[73]:


newind


# In[74]:


df['States'] = newind


# In[75]:


df


# In[76]:


df.set_index('States')


# In[77]:


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[78]:


hier_index


# In[79]:


df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])


# In[80]:


df


# In[81]:


df.loc['G1']


# In[82]:


df.loc['G1'].iloc[0]['A']


# In[83]:


df.loc['G1'].iloc[0]['B']


# In[84]:


df.loc['G1'].loc[1]


# In[85]:


df.index.levels


# In[86]:


df.index.names


# In[87]:


df.index.names = ['Groups', 'Num']


# In[88]:


df


# In[89]:


df.loc['G2'].loc[2]['B']


# In[90]:


df.loc['G1']


# In[91]:


df.xs('G1')           #cross section method


# In[92]:


df.xs(1, level = 'Num')


# In[93]:


df.index.levels


# In[94]:


df.index.names


# In[95]:


# missing data


# In[96]:


import pandas as pd
import numpy as np


# In[97]:


d = {'A' : [1, 2, np.nan], 'B' : [5, np.nan, np.nan], 'C' : [1, 2, 3]}


# In[98]:


df = pd.DataFrame(d)


# In[99]:


df


# In[100]:


df.dropna()   # it removes rows or columns if it has no value. default axis = 0


# In[101]:


df.dropna(axis = 1)


# In[102]:


df.dropna(thresh = 2)   # keeps at least 2 non-Nan values rows.


# In[103]:


df


# In[104]:


df.fillna(value = 'FILL VALUE')


# In[105]:


df


# In[106]:


df['A']


# In[107]:


df['A'].fillna(value = df['A'].mean())


# In[108]:


#groupby


# In[109]:


data = {'Company' : ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
       'Person' : ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
       'Sales' : [200, 120, 340, 124, 243, 350]}


# In[110]:


df = pd.DataFrame(data)


# In[111]:


df


# In[112]:


df.groupby('Company')


# In[113]:


byComp = df.groupby('Company')


# In[114]:


byComp.mean()


# In[115]:


byComp.std()


# In[116]:


byComp.sum()


# In[117]:


byComp.sum().loc['FB']


# In[118]:


df.groupby('Company').sum().loc['FB']


# In[119]:


df


# In[120]:


df.groupby('Company').count()


# In[121]:


df.max()


# In[122]:


df.groupby('Company').max()


# In[123]:


df.groupby('Company').min()


# In[124]:


df.groupby('Company').describe()


# In[125]:


df.groupby('Company').describe().loc['FB']


# In[126]:


df.groupby('Company').describe().transpose()


# In[127]:


df.groupby('Company').describe().transpose()['FB']


# In[128]:


#merging, joining, concatenating


# In[129]:


df1 = pd.DataFrame({'A' : ['A0', 'A1', 'A2', 'A3'],
                   'B' : ['B0', 'B1', 'B2', 'B3'],
                   'C' : ['C0', 'C1', 'C2', 'C3'],
                   'D' : ['D0', 'D1', 'D2', 'D3']})


# In[130]:


df2 = pd.DataFrame({'A' : ['A4', 'A5', 'A6', 'A7'],
                   'B' : ['B4', 'B5', 'B6', 'B7'],
                   'C' : ['C4', 'C5', 'C6', 'C7'],
                   'D' : ['D4', 'D5', 'D6', 'D7']},
                  index = [4, 5, 6, 7])


# In[131]:


df3 = pd.DataFrame({'A' : ['A8', 'A9', 'A10', 'A11'],
                   'B' : ['B8', 'B9', 'B10', 'B11'],
                   'C' : ['C8', 'C9', 'C10', 'C11'],
                   'D' : ['D8', 'D9', 'D10', 'D11']},
                  index = [8, 9, 10, 11])


# In[132]:


df1


# In[133]:


df2


# In[134]:


df3


# In[135]:


pd.concat([df1, df2, df3])


# In[136]:


pd.concat([df1, df2, df3], axis = 1)


# In[137]:


left = pd.DataFrame({'key' : ['K0', 'K1', 'K2', 'K3'],
                   'A' : ['A0', 'A1', 'A2', 'A3'],
                   'B' : ['B0', 'B1', 'B2', 'B3']})


# In[138]:


right = pd.DataFrame({'key' : ['K0', 'K1', 'K2', 'K3'],
                   'C' : ['C0', 'C1', 'C2', 'C3'],
                   'D' : ['D0', 'D1', 'D2', 'D3']})


# In[139]:


left


# In[140]:


right


# In[141]:


pd.concat([left, right])


# In[142]:


pd.concat([left, right], axis = 1)


# In[143]:


pd.merge(left, right, how = 'inner', on = 'key')


# In[144]:


left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


# In[145]:


right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                     'key2': ['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})


# In[146]:


left1


# In[147]:


right1


# In[148]:


pd.merge(left1, right1, on = ['key1', 'key2'])


# In[149]:


pd.merge(left1, right1, how = 'outer', on = ['key1', 'key2'])


# In[150]:


pd.merge(left1, right1, how = 'right', on = ['key1', 'key2'])


# In[151]:


left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index = ['K0', 'K1', 'K2'])


# In[152]:


right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                     'D': ['D0', 'D2', 'D3']},
                    index = ['K0', 'K2', 'K3'])


# In[153]:


left2


# In[154]:


right2


# In[155]:


left2.join(right2)


# In[156]:


left2.join(right2, how = 'outer')


# In[157]:


left2.join(right2, how = 'right')


# In[158]:


df = pd.DataFrame({'col1' : [1, 2, 3, 4],
                  'col2' : [444, 555, 666, 444],
                  'col3' : ['abc', 'def', 'ghi', 'xyz']})


# In[159]:


df


# In[160]:


df['col2'].unique()


# In[161]:


len(df['col2'].unique())


# In[162]:


df['col2'].nunique()            # number of unique = nunique


# In[163]:


df['col2'].value_counts()


# In[164]:


df['col2'].value_counts().sum()


# In[165]:


df[df['col1'] > 2]


# In[166]:


df['col1'] > 2


# In[167]:


df[(df['col1'] > 2) & (df['col2'] == 444)]


# In[168]:


def times2(x):
    return x * 2


# In[169]:


df['col1']


# In[170]:


df['col1'].apply(times2)


# In[171]:


df['col3']


# In[172]:


df['col3'].apply(len)


# In[173]:


df['col3'].apply(str.upper)


# In[174]:


df['col2']


# In[175]:


df['col2'].apply(lambda x : x * 2)


# In[176]:


df


# In[177]:


df.drop('col1', axis = 1)


# In[178]:


df.columns


# In[179]:


df.index


# In[180]:


df.sort_values(by = 'col2')


# In[181]:


df.isnull()   # = df.isna()


# In[182]:


data = {'A' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
       'B' : ['one', 'one', 'two', 'two', 'one', 'one'],
       'C' : ['x', 'y', 'x', 'y', 'x', 'y'],
       'D' : [1, 3, 2, 5, 4, 1]}


# In[183]:


df = pd.DataFrame(data)


# In[184]:


df


# In[185]:


df.pivot_table(values = 'D', index = ['A', 'B'], columns = 'C')


# In[186]:


# CSV, Excel, HTML, SQL


# In[187]:


pip install sqlalchemy


# In[188]:


pip install lxml


# In[189]:


pip install html5lib


# In[190]:


pip install BeautifulSoup4


# In[191]:


import pandas as pd
import numpy as np


# In[192]:


pwd


# In[193]:


df = pd.read_csv('example.csv')


# In[194]:


df


# In[195]:


df.to_csv('My_output', index = False)


# In[196]:


pd.read_csv('My_output')


# In[197]:


pip install xlrd


# In[198]:


pip install openpyxl


# In[200]:


pd.read_excel('Excel_Sample.xlsx', sheet_name = 'Sheet1', index_col = 0)


# In[201]:


df.to_excel('Excel_Sample.xlsx', sheet_name = 'NewSheet')


# In[204]:


data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.html')


# In[205]:


data


# In[206]:


type(data)


# In[207]:


data[0]


# In[208]:


data[0].head()


# In[209]:


from sqlalchemy import create_engine


# In[210]:


engine = create_engine('sqlite:///:memory:')


# In[211]:


df


# In[212]:


df.to_sql('my_table', engine)


# In[213]:


sqldf = pd.read_sql('my_table', con = engine)


# In[214]:


sqldf


# In[ ]:




