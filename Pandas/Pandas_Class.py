#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[2]:


pd.Series([10, 88, 3, 4, 5])


# In[3]:


ser = pd.Series([10, 88, 3, 4, 5])


# In[4]:


ser


# In[5]:


type(ser)


# In[6]:


ser.dtype


# In[7]:


ser.shape


# In[8]:


ser.size


# In[9]:


ser.ndim


# In[10]:


ser.values


# In[11]:


ser.index


# In[12]:


[i for i in ser.values]


# In[13]:


ser.head(3)   # default 5


# In[14]:


ser.tail(3)   # default 5


# In[15]:


pd.Series([i for i in 'clarusway'])


# In[16]:


labels = ['a', 'b', 'c']


# In[17]:


my_list = [10, 20, 30]


# In[18]:


arr = np.array([10, 20, 30])


# In[19]:


d = {'a' : 10, 'b' : 20, 'c' : 30}


# In[20]:


pd.Series(my_list)


# In[21]:


pd.Series(my_list, labels)


# In[22]:


pd.Series(arr)


# In[23]:


pd.Series(arr, labels)


# In[24]:


pd.Series(d)


# In[25]:


pd.Series(d, labels)


# In[26]:


pd.Series(d, my_list)


# In[27]:


pd.Series([sum, print, len])


# In[28]:


mix_data = pd.Series([1, 'cat', True])


# In[29]:


mix_data


# In[30]:


# .sort_index() .sort_values() .isin()


# In[31]:


ser1 = pd.Series([1, 2, 3, 4], index = ['USA', 'Germany', 'USSR', 'Japan'])


# In[32]:


ser1


# In[33]:


ser2 = pd.Series([1, 2, 5, 4], index = ['USA', 'Germany', 'Italy', 'Japan'])


# In[34]:


ser2


# In[35]:


ser1['USA']


# In[36]:


ser3 = pd.Series(data = labels)


# In[37]:


ser3


# In[38]:


ser3[0]


# In[39]:


ser1 + ser2


# In[40]:


(ser1 + ser2)['Germany']


# In[41]:


a = np.array([1, 2, 33, 444, 75])


# In[42]:


a


# In[43]:


panser = pd.Series(a)


# In[44]:


panser


# In[45]:


panser[0]


# In[46]:


panser[0:3]


# In[47]:


ser1


# In[48]:


ser1['USA' : 'USSR']  # for object index last value is inclusive


# In[49]:


panser = pd.Series([121, 200, 150, 99], ['ali', 'veli', 'gül', 'nur'])


# In[50]:


panser


# In[51]:


panser['ali']


# In[52]:


panser[0]


# In[53]:


panser[['veli', 'nur']]


# In[54]:


panser[[0, 2, 3]]


# In[55]:


panser[0 : 2]


# In[56]:


panser['ali' : 'gül']


# In[57]:


panser.index


# In[58]:


panser.values


# In[59]:


panser.items


# In[60]:


panser.items()


# In[61]:


list(panser.items())


# In[62]:


'mehmet' in panser


# In[63]:


'ali' in panser


# In[64]:


200 in panser.values


# In[65]:


200 in panser


# In[66]:


panser['veli'] = 571


# In[67]:


panser


# In[68]:


panser > 130


# In[69]:


panser[panser > 130]


# In[70]:


#DataFrame


# In[71]:


datam = [1, 2, 39, 67, 90]


# In[72]:


datam


# In[73]:


pd.DataFrame(datam, columns = ['column_name'])


# In[74]:


m = np.arange(1, 10).reshape(3, 3)


# In[75]:


m


# In[76]:


pd.DataFrame(m, columns = ['var1', 'var2', 'var3'])


# In[77]:


pd.DataFrame(data = m, columns = ['var1', 'var2', 'var3'])


# In[78]:


df = pd.DataFrame(data = m, columns = ['var1', 'var2', 'var3'])


# In[79]:


df


# In[80]:


df.head(1)


# In[81]:


df.tail(1)


# In[82]:


df.columns


# In[83]:


df.index


# In[84]:


df.axes


# In[85]:


df.columns = ['new1', 'new2', 'new3']


# In[86]:


df


# In[87]:


type(df)


# In[88]:


df.shape


# In[89]:


df.size


# In[90]:


df.ndim


# In[91]:


df.values


# In[92]:


s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)


# In[93]:


s1


# In[94]:


s2


# In[95]:


s3


# In[96]:


my_dict = {'var1' : s1, 'var2' : s2, 'var3' : s3}


# In[97]:


df1 = pd.DataFrame(my_dict)


# In[98]:


df1


# In[99]:


# example1.csv


# In[100]:


pwd


# In[101]:


pd.read_csv('example1.csv', delimiter = ';')


# In[102]:


df3 = pd.read_csv('example1.csv', delimiter = ';')


# In[103]:


df3.head()


# In[104]:


########


# In[105]:


df1


# In[106]:


df1[1 : 3]


# In[107]:


df1.index


# In[108]:


[i for i in df1.index]


# In[109]:


df1.index = ['a', 'b', 'c', 'd', 'e']


# In[110]:


df1


# In[111]:


df1['a' : 'c']


# In[112]:


'var1' in df1


# In[113]:


'joseph' in df1


# In[114]:


'a' in df1


# In[115]:


8 in df1


# In[116]:


from numpy.random import randn
np.random.seed(101)


# In[117]:


df4 = pd.DataFrame(randn(5, 4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())


# In[118]:


df4


# In[119]:


df4['W']       # it gives Series


# In[120]:


type(df4['W'])


# In[121]:


df4['W'].values


# In[122]:


df4['W'].ndim


# In[123]:


df4[['W']]     # two brackets give DataFrame


# In[124]:


df4[['W', 'Z']]


# In[125]:


wz_df4 = df4[['W', 'Z']]


# In[126]:


wz_df4


# In[127]:


df4.W   # = df['W']


# In[128]:


df4


# In[129]:


df4['A' : 'C']


# In[130]:


df4['C' : 'C']


# In[131]:


df4


# In[132]:


df4['new'] = df4['W'] + df4['Y']


# In[133]:


df4


# In[134]:


df4.drop(['W', 'Y'], axis = 1)


# In[135]:


df4


# In[136]:


df4.drop(['new'], axis = 1, inplace = True)


# In[137]:


df4


# In[138]:


df4.drop('E')            # default axis = 0


# In[139]:


df4


# In[140]:


df4.loc['B']


# In[141]:


df4.loc[['B']]


# In[142]:


df4.loc['B' : 'D']


# In[143]:


df4.loc[['B', 'E']]


# In[144]:


df4.loc['B', 'W']


# In[145]:


df4.loc['B']['W']


# In[146]:


df4.loc['B' : 'E'][['Y', 'Z']]


# In[147]:


df4.loc[['B', 'E']][['Y', 'Z' ]]


# In[148]:


df4.loc[[False, False, True, False, True]]


# In[149]:


df4


# In[150]:


df4.loc[df4['Z'] < 0]


# In[151]:


df5 = pd.DataFrame(np.random.randint(1, 30, (10, 3)), columns = ['var1', 'var2', 'var3'])


# In[152]:


df5


# In[153]:


df5.loc[1]


# In[154]:


df5.iloc[1]


# In[155]:


df5.loc[1 : 4]


# In[156]:


df5.iloc[1 : 4]


# In[157]:


df5


# In[158]:


df5.index = 'a b c d e f g h i j'.split()


# In[159]:


df5


# In[160]:


df5.loc['b' : 'd']


# In[161]:


df5.iloc[1 : 4]


# In[162]:


df5.iloc[4]


# In[163]:


df5.iloc[1, 1]


# In[164]:


df5.loc['b', 'var2']


# In[165]:


df5.loc['b' : 'e']['var2']


# In[166]:


df5.loc['b' : 'e'][['var2']]


# In[167]:


df5.iloc[1 : 5, 1 : 2]


# In[168]:


df4


# In[169]:


df4.loc['A']


# In[170]:


df4.iloc[0]


# In[171]:


df4.loc[['A']]


# In[172]:


df4.iloc[[0]]


# In[173]:


df4.iloc[:, 2]


# In[174]:


df4.iloc[:, 2:3]


# In[175]:


df4.iloc[:, [2]]


# In[176]:


df4[['Y']]


# In[177]:


df4


# In[178]:


df4.loc['B', 'Y']


# In[179]:


df4.loc[['B'], ['Y']]


# In[180]:


df4.loc['A' : 'B'][['W', 'Y']]


# In[181]:


df4.iloc[0 : 2, [0, 2]]


# In[182]:


df4


# In[183]:


df4 > 0


# In[184]:


df4[df4 > 0]


# In[185]:


df4['W'][df4['W'] > 0]


# In[186]:


df4[['Y']][df4['W'] > 0]


# In[187]:


df4


# In[188]:


df4[(df4['W'] > 0) & (df4['Y'] > 1)]


# In[189]:


df4.loc[(df4['X'] > 0), ['X', 'Z']]


# In[190]:


df4.loc[(df4['W'] > 2) | (df4['W'] < -2), ['W', 'Y']]


# In[191]:


df4


# In[192]:


df4.index


# In[193]:


df4.reset_index()


# In[194]:


df4


# In[195]:


df4.reset_index(drop = True)               # it removes index column


# In[196]:


df4


# In[197]:


newindx = 'CA NY WY OR CO'.split()


# In[198]:


newindx


# In[199]:


df4['states'] = newindx


# In[200]:


df4


# In[201]:


df4.set_index('states', inplace = True)


# In[202]:


df4


# In[203]:


outside = ['M1', 'M1', 'M1', 'M2', 'M2', 'M2']                # Multi-index
inside = [1, 2, 3, 1, 2, 3]
multi_index = list(zip(outside, inside))
multi_index


# In[204]:


hier_index = pd.MultiIndex.from_tuples(multi_index)


# In[205]:


hier_index


# In[206]:


df6 = pd.DataFrame(np.random.randn(6, 2), hier_index, columns = ['A', 'B'])


# In[207]:


df6


# In[208]:


df6.loc['M1']


# In[209]:


df6.loc['M1'].loc[3]


# In[210]:


df6.loc['M1'].loc[[3]]


# In[211]:


df6.index


# In[212]:


df6.index.levels


# In[213]:


df6.index.names


# In[214]:


df6.index.names = ['Group', 'Num']


# In[215]:


df6


# In[216]:


df6.xs('M2')


# In[217]:


df6.xs(('M2', 2))


# In[218]:


df6.xs(('M2', 2), level = [0, 1])


# In[219]:


df6.xs(2, level = 1)


# In[220]:


df6.xs(2, level = 'Num')            # if we don't write in order multi-indexes we need to specify level.


# In[221]:


df6.xs('M1', level = 0)


# In[222]:


df6


# In[223]:


df6.drop(2, level = 'Num')


# In[224]:


# Aggregation, Groupby


# In[225]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[226]:


get_ipython().run_line_magic('pinfo', 'sns.load_dataset')


# In[227]:


df = sns.load_dataset('planets')


# In[228]:


df.head()


# In[229]:


df.shape


# In[230]:


df.info()


# In[231]:


df['mass'].mean()


# In[232]:


df['mass'].count()


# In[233]:


df['mass'].min()


# In[234]:


df['mass'].max()


# In[235]:


df['mass'].median()


# In[236]:


df['mass'].sum()


# In[237]:


df['mass'].std()


# In[238]:


df.describe()


# In[239]:


df.isnull().sum()


# In[240]:


df.dropna()


# In[241]:


df.dropna().info()


# In[242]:


df.info()


# In[243]:


df.dropna().describe().T


# In[244]:


df.describe().T


# In[245]:


df['method']


# In[246]:


df['method'].value_counts()


# In[247]:


df['method'].value_counts(dropna = False)


# In[248]:


df['mass'].value_counts(dropna = False)


# In[249]:


df['mass'].nunique()


# In[250]:


df['method'].nunique()


# In[251]:


df.groupby('method')


# In[252]:


df.groupby('method').mean()


# In[253]:


df.groupby('method').mean()[['orbital_period']]


# In[254]:


df.groupby('method').mean()[['orbital_period']].describe().T


# In[255]:


df.groupby('method')[['orbital_period']].describe()


# In[256]:


df.groupby('method')['distance'].sum()


# In[257]:


df['year']


# In[258]:


df['year'].value_counts(dropna = False)


# In[259]:


df.year.unique()


# In[260]:


df.groupby('year').mean()['mass']     # = df.groupby('year')['mass'].mean()


# In[261]:


data = {'Company' : ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
       'Person' : ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
       'Sales' : [200, 120, 340, 124, 243, 350]}


# In[262]:


df7 = pd.DataFrame(data)


# In[263]:


df7


# In[264]:


df7.groupby('Company')


# In[265]:


by_comp = df7.groupby('Company')


# In[266]:


by_comp.mean()


# In[267]:


df7


# In[268]:


by_comp.std()


# In[269]:


by_comp.min()


# In[270]:


by_comp.describe()


# In[271]:


by_comp.describe().T['GOOG']


# In[272]:


df8 = pd.DataFrame({'col1' : [1, 2, 3, 4],
                  'col2' : [444, 555, 666, 444],
                  'col3' : ['abc', 'def', 'ghi', 'xyz']})


# In[273]:


df8


# In[274]:


df8['col2'].unique()


# In[275]:


df8['col2'].value_counts(dropna = False)


# In[276]:


df8[(df8['col1'] > 2) & (df8['col2'] == 444)]


# In[277]:


df8


# In[278]:


del df8['col2']


# In[279]:


df8


# In[280]:


df8.columns


# In[281]:


df8.index


# In[282]:


df8


# In[283]:


df8.sort_values(by = 'col3', ascending = False)


# In[284]:


df8


# In[87]:


df9 = pd.DataFrame({'col1' : [1, 2, 3, np.nan],
                  'col2' : [np.nan, 555, 666, 444],
                  'col3' : ['abc', 'def', 'ghi', 'xyz']})


# In[286]:


df9


# In[287]:


df9.dropna()


# In[288]:


df9


# In[289]:


df9.fillna('milk')


# In[290]:


df9.dropna(how = 'all')


# In[291]:


df9.dropna(how = 'any')


# In[3]:


df4 = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'var1': [10,23,33,22,11,99],
                   'var2': [100,253,333,262,111,969]})
df4


# In[10]:


df4.groupby('groups').mean()


# In[14]:


df4.groupby('groups').aggregate('mean')


# In[5]:


df4.groupby('groups').aggregate([np.min, np.median, np.max])


# In[18]:


df4.groupby('groups').aggregate({'var1' : 'min', 'var2' : 'max'})


# In[17]:


df4.groupby('groups').aggregate({'var1' : 'min', 'var2' : [np.median, np.max]})


# In[2]:


df4 = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'var1': [10,23,33,22,11,99],
                   'var2': [100,253,333,262,111,969]})
df4


# In[316]:


df4.groupby('groups').std()


# In[67]:


# filter, transform, apply


# In[303]:


def filter_function(x):
    return x['var1'].std() > 9


# In[68]:


df4


# In[304]:


df4.groupby('groups').filter(filter_function)


# In[313]:


df4.groupby('groups').sum()


# In[310]:


df4.groupby('groups').filter(lambda x : x['var2'].sum() < 444)


# In[317]:


df4


# In[320]:


df4['var1'] * 9


# In[75]:


df_a = df4.iloc[:, 1:3]


# In[76]:


df_a


# In[79]:


df_a.transform(lambda x : (x-x.mean()) / x.std())


# In[81]:


df_a.transform(lambda x : np.log10(x))


# In[9]:


df4


# In[10]:


df4.apply(np.sum)


# In[83]:


df4[['var1', 'var2']].apply(np.median)


# In[16]:


df_numeric = df4.iloc[:, 1 : 3]


# In[17]:


df_numeric.apply(np.median)


# In[19]:


df_numeric.apply(np.mean, axis = 1)


# In[20]:


df_numeric.apply(np.mean, axis = 0)


# In[84]:


df4


# In[86]:


df4.groupby('groups').apply(np.mean)


# In[23]:


df4.groupby('groups').mean()


# In[38]:


df2 = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abcc','de','ghi','xyyzz']})
df2


# In[34]:


def times2(x):
    return x * 2


# In[35]:


df2['col1'].apply(times2)


# In[39]:


df2['col3'].apply(len)


# In[41]:


df2.apply(len)


# In[40]:


df2['col3'].apply(str.upper)


# In[48]:


df2['col3'].transform(len)


# In[49]:


df2['col3'].transform(str.upper)


# In[50]:


df1 = pd.DataFrame([["a", 9, 25]] * 4, columns=["grp", 'P', 'Q'])
df2 = pd.DataFrame([["b", 9, 25]] * 3, columns=["grp", 'P', 'Q'])
df3 = pd.concat([df1, df2], ignore_index=True)
df3


# In[54]:


df3.apply(lambda x : x + x)


# In[52]:


df3.transform(lambda x : x + x)


# In[56]:


df3


# In[55]:


df3.groupby('grp').apply(sum)


# In[57]:


df3.groupby('grp').transform(sum)


# In[62]:


df3.groupby(['P', 'Q']).sum()


# In[63]:


df3.groupby('grp').transform(len)


# In[38]:


import seaborn as sns


# In[39]:


import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# In[40]:


titanic = sns.load_dataset('titanic')


# In[41]:


titanic.head()


# In[42]:


titanic.groupby('sex')[['survived']].mean()


# In[43]:


titanic.groupby(['sex', 'class'])[['survived']].mean()


# In[86]:


titanic.groupby(['sex', 'class'])[['survived']].aggregate('mean').unstack()


# In[89]:


titanic.pivot_table('survived', 'sex', 'class')       # values, index, columns, aggfunc(default is 'mean')


# In[44]:


titanic.pivot_table('survived', 'sex', 'class', 'sum')    # values, index, columns, aggfunc


# In[53]:


titanic.pivot_table(values = 'who', index = 'sex', columns = 'class', aggfunc = 'count')


# In[55]:


titanic.groupby('sex')[['sex']].count()


# In[57]:


titanic.groupby('sex')[['survived']].sum()


# In[66]:


titanic.groupby('adult_male')[['survived']].sum()


# In[92]:


titanic.pivot_table('age', 'sex', 'class', 'mean')    # values, index, columns, aggfunc


# In[93]:


titanic.pivot_table('age', 'sex', 'class')  # default aggregate function is mean


# In[94]:


titanic.pivot_table('age', 'class', 'sex')  # values, index, columns, aggfunc


# In[95]:


data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
       'B':['one', 'one', 'two', 'two', 'one', 'one'],
       'C':['x', 'y', 'x', 'y', 'x', 'y'],
       'D':[1, 3, 2, 5, 4, 1]}
df5 = pd.DataFrame(data)
df5


# In[97]:


df5.pivot_table('D', 'C', ['A', 'B'])


# In[98]:


df5.pivot_table('D', ['A', 'B'], 'C')


# In[20]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']}
                        )


# In[21]:


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']}
                         )


# In[22]:


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']}
                        )


# In[23]:


df1


# In[24]:


df2


# In[25]:


df3


# In[104]:


pd.concat([df1, df2, df3])


# In[105]:


pd.concat([df1, df2, df3], ignore_index = True)   # we can give new index(with order) by ignore_index arg.


# In[107]:


pd.concat([df1, df2, df3], axis = 1)


# In[27]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0,1,2,3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                        index=[4,5,6,7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8,9,10,11])


# In[37]:


pd.concat([df1, df2, df3], axis = 1)


# In[111]:


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})


# In[112]:


left


# In[113]:


right


# In[114]:


pd.merge(left, right, how = 'inner', on = 'key')


# In[117]:


pd.merge(left, right, how = 'right', on = 'key')


# In[123]:


left = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                     'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'A': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})


# In[124]:


left


# In[125]:


right


# In[126]:


pd.merge(left, right, how = 'inner', on = 'key')


# In[127]:


pd.merge(left, right, how = 'outer', on = 'key')


# In[128]:


pd.merge(left, right, how = 'left', on = 'key')


# In[129]:


pd.merge(left, right, how = 'right', on = 'key')


# In[130]:


left = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})


# In[131]:


left


# In[132]:


right


# In[133]:


pd.merge(left, right, on = 'key')


# In[134]:


pd.merge(left, right, how = 'outer', on = 'key')


# In[135]:


pd.merge(left, right, how = 'left', on = 'key')


# In[136]:


pd.merge(left, right, how = 'right', on = 'key')


# In[137]:


left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})


# In[138]:


left1


# In[139]:


right1


# In[141]:


pd.merge(left1, right1, on = ['key1', 'key2'])


# In[142]:


pd.merge(left1, right1, how = 'outer', on = ['key1', 'key2'])


# In[ ]:




