#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

cleaned_data = pd.read_csv("/users/prithvisadanand/cleaned_omnichannel_sales_dataset.csv")
cleaned_data


# In[9]:


# sales by region

regional_sales = cleaned_data.groupby('Region')['Total_Sales'].sum().sort_values(ascending = False)
print(regional_sales)


# In[10]:


# sales by products

product_sales_review = cleaned_data.groupby('Product')['Total_Sales'].sum().sort_values(ascending = False)
print(product_sales_review)


# In[14]:


# Sales by Sales Channel

sales_channel = cleaned_data.groupby('Sales_Channel')['Total_Sales'].sum()

print(sales_channel)


# In[15]:


# payment menthod

payment_stg = cleaned_data.groupby('Payment_Method')['Total_Sales'].sum().sort_values(ascending = False)
print(payment_stg)


# In[16]:


# sales by salesperson 

salesperson_perf = cleaned_data.groupby('Salesperson')['Total_Sales'].sum().sort_values(ascending = False)
print(salesperson_perf)

