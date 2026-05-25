#!/usr/bin/env python
# coding: utf-8

# # KPI Analysis

# In[3]:


import pandas as pd
import numpy as np

cleaned_data = pd.read_csv("/Users/prithvisadanand/cleaned_omnichannel_sales_dataset.csv")
cleaned_data.head()


# In[5]:


# Total revenue

overall_revenue = cleaned_data['Total_Sales'].sum()
print("Total Revenue:", overall_revenue)


# In[15]:


# Total Quantity

overall_qty = cleaned_data['Quantity'].sum()
print("Total Quantity:", overall_qty)


# In[16]:


# Average Order Value (AOV)

avg_order_value = cleaned_data['Total_Sales'].mean()
print('Average Order Value:', avg_order_value)


# In[17]:


# Identifying the product that creates highest total revenue

best_product = cleaned_data.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print(best_product)


# In[18]:


# Identifying the region that produce the most revenue

best_region = cleaned_data.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print(best_region)


# In[19]:


# payment method

payment_details = cleaned_data.groupby('Payment_Method')['Total_Sales'].sum()
print(payment_details)


# In[ ]:




