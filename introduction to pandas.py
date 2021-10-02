#!/usr/bin/env python
# coding: utf-8

# In[1]:


# this work sheet contain data analysis


# In[2]:


# usage of pandas 


# In[3]:



import pandas as pd
import numpy as np


# In[4]:


# two important datatypes
#1.series
#2.dataframes
fruits = pd.Series(["apple", "banana", "papaya"])


# In[5]:


fruits


# In[6]:


colours = pd.Series(["Red", "yellow", "orange"])
colours


# In[7]:


# DataFrame = 2-dimensional
fruites_data = pd.DataFrame({"fruits": fruits, "Colour": colours})
fruites_data


# In[8]:


# Import data
cust = pd.read_csv("C:\\Users\\prane\\OneDrive\\Documents\\machine learning\\911.csv")


# In[9]:


cust


# # describe data

# In[10]:



# Attribute
cust.dtypes


# In[11]:


# shows all the columns present in our dataset
cust.columns


# In[12]:


#saving the result int o a list so that we can use it for further usage
cust_columns = cust.columns
cust_columns


# In[13]:


# shows the range of the rows

cust.index


# In[14]:


# discribes all the numrical columns
cust.describe()


# In[15]:


#shows not null values count and datatypes
cust.info()


# In[86]:


# shows the  null values
cust.isnull().sum()


# In[16]:


car_prices = pd.Series([3000, 1500, 111250])


# In[18]:


car_prices


# In[17]:


len(cust)


# In[120]:


# return shape of  dataset
cust.shape


# In[118]:


cust['title'].unique


# In[116]:


#sort vlaues accordingly
cust.sort_values(by='twp')


# In[19]:


cust


# # Viewing and selecting data

# In[23]:


#prints  first five rows
cust.head()


# In[24]:



# returns last five datapoints
cust.tail()


# In[26]:


# returns top ten rows
cust.head(10)


# In[31]:


# show the rows from index 5 to 10

cust.loc[5:10]


# In[43]:


# returns all the coulmns values for index 11
cust.loc[11]


# In[42]:


# iloc prefers to position
cust.iloc[11]


# In[45]:


cust.loc[:5]


# In[47]:


# returns only one coulmn
cust['title']


# In[51]:


cust['twp']


# In[53]:


cust.twp


# In[52]:


cust[{'lat','lng'}]


# In[55]:


# can view specify rows in the column
cust[cust['twp']=='NEW HANOVER']


# In[60]:


cust[cust['lat']>=40]


# In[65]:


# cross check the count of and values with respoective to two columns
pd.crosstab(cust['twp'],cust['title'])


# In[68]:


cust.groupby(['twp']).mean()


# In[72]:


cust['zip'].plot()


# # manipulating data

# In[78]:


# changing upper case letter into lower case for column twp
cust['twp'].str.lower()


# In[79]:


cust


# In[80]:


# but the change did reflect in the dataset.


# In[81]:


# to reflect the change in the dataset we need to reassign the values to column


# In[82]:


cust['twp']=cust['twp'].str.lower()


# In[83]:


cust


# In[113]:


# handling missing values


# In[87]:


cust.isnull().sum()


# In[100]:


# filling null null values for column addr
cust['addr'].fillna('N\a',inplace=True)


# In[101]:


cust['addr'].isnull().sum()


# In[102]:


# no null values in coulmn addr


# In[103]:


# filling null null values for column addr
cust['twp'].fillna('Not available',inplace=True)


# In[105]:


cust['twp'].isnull().sum()


# In[106]:


# filled null vlaues in twp column


# In[108]:


# filling null null values for column addr
cust['zip'].fillna('00000',inplace=True)


# In[110]:


cust['zip'].isnull().sum()


# In[111]:


# now there are no missing values


# In[ ]:




