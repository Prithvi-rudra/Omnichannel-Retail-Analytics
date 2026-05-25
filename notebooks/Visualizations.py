#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cleaned_data = pd.read_csv("/users/prithvisadanand/cleaned_omnichannel_sales_dataset.csv")
cleaned_data


# In[4]:


# Monthly Sales Trend

monthly_revenue = cleaned_data.groupby('Month_Name')['Total_Sales'].sum()
month_order = ['January', 'February', 'March', 'April', 'May']

monthly_revenue = monthly_revenue.reindex(month_order)

plt.figure(figsize=(10,5))

plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')

plt.title("Monthly Sales Analysis", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.grid(True)
plt.tight_layout()
plt.show()


# In[5]:


# Product Performance

inventory_sales = cleaned_data.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))

plt.bar(inventory_sales.index, inventory_sales.values)

plt.title("Product Performance based on total sales", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[6]:


# Region revenue

regional_sales = cleaned_data.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))

plt.bar(regional_sales.index, regional_sales.values)

plt.title("Regional based Sales review", fontsize=14)
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# In[7]:


# Payment methods 

net_sales = cleaned_data.groupby('Payment_Method')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))

plt.bar(net_sales.index, net_sales.values)

plt.title("Revenue Breakdown by Transaction Type", fontsize=14)
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


# In[8]:


# Online vs Offline sales 

channel_sales = cleaned_data.groupby('Sales_Channel')['Total_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(6,5))

plt.bar(channel_sales.index, channel_sales.values)

plt.title("Sales by Channel (Online vs Offline)", fontsize=14)
plt.xlabel("Sales Channel")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# In[ ]:




