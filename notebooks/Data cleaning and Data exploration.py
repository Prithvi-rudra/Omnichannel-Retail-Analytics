#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import libraries and dataset

import pandas as pd
import numpy as np

uosd = pd.read_csv("updated_omnichannel_sales_dataset.csv")
uosd.head()


# In[4]:


# studying data structure

uosd.shape


# In[5]:


# check column information

uosd.info()


# In[7]:


# Convert Order_Date into datetime format

uosd['Order_Date'] = pd.to_datetime(uosd['Order_Date'])
uosd.info()


# In[8]:


# checking missing value

uosd.isnull().sum()


# In[11]:


# filling the missing value in the Device_Type column

uosd["Device_Type"] = uosd["Device_Type"].fillna('Not Applicable')
uosd.isnull().sum()


# In[12]:


# checking the duplicate record

uosd.duplicated().sum()


# In[14]:


uosd.dtypes


# In[15]:


# Create new features columns

uosd['Year'] = uosd['Order_Date'].dt.year
uosd['Month'] = uosd['Order_Date'].dt.month
uosd['Month_Name'] = uosd['Order_Date'].dt.month_name()
uosd['Day_Name'] = uosd['Order_Date'].dt.day_name()

# View updated dataset
uosd.head()


# In[16]:


# checking total_sales calculation and making sure that Total_Sales = Quantity × Unit_Price

(uosd['Quantity'] * uosd['Unit_Price'] == uosd['Total_Sales']).all()


# In[17]:


uosd.describe()


# In[27]:


# Save cleaned dataset

uosd.to_csv('cleaned_omnichannel_sales_dataset.csv', index=False)

print("Cleaned dataset saved successfully!")


# In[19]:


import os

os.listdir()


# In[29]:


uosd.head()


# In[30]:


# CHECK UNIQUE VALUES of product categories, sales, payment method and region

uosd['Product'].unique()


# In[31]:


# CHECK UNIQUE VALUES of sales channel

uosd['Sales_Channel'].unique()


# In[32]:


# CHECK UNIQUE VALUES of payment method

uosd['Payment_Method'].unique()


# In[33]:


#CHECK UNIQUE VALUES of region

uosd['Region'].unique()


# In[34]:


#FINAL DATA QUALITY CHECK

uosd.nunique()


# In[52]:


# creating a final clean dataset view

uosd.sample(5)


# In[ ]:




