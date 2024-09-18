#!/usr/bin/env python
# coding: utf-8

# In[123]:


#start

#Import library of PANDAS
import pandas as pd

#Load csv file into a data frame named cars using pandas
df_cars = pd.read_csv('cars.csv')


# In[125]:


#use .head() to display the first five rows of the data frame of cars
df_cars.head()


# In[127]:


#use .tail() to display the last five rows of the data frame of cars
df_cars.tail()

#end

