#!/usr/bin/env python
# coding: utf-8

# In[108]:


# IMPORT REQUIRED MODULES
import pandas as pd
import datetime


# In[122]:


# DEFINE VARIABLES
today = pd.datetime.today().date()
my_time_delta = 30


# In[123]:


# READ SAMPLE DATA AND FIX FORMATTING
df = pd.read_csv('sample-data-metal-cases.csv') #read csv file
df['posting_date'] = pd.to_datetime(df['posting_date'], format=("%Y.%m.%d")) #define posting_date



# DESCRIBE RAW DATAFRAME
print(df.dtypes)
df.head()


# In[124]:


total_cases_customer = df[['customer', 'quantity_in_base_unit']].groupby(["customer"]).sum().reset_index()
total_cases_customer = total_cases_customer.rename(columns={'quantity_in_base_unit': 'current_stock'})
total_cases_customer[total_cases_customer['customer'] == 1000096].head(3)


# In[168]:


#filter for less then 30 days
selected_date_range = pd.date_range(today - pd.to_timedelta(my_time_delta, unit='d'), today, freq='D')
df_selected = df[df["posting_date"].isin(selected_date_range)]
df_selected=df_selected[['customer','quantity_in_base_unit']].groupby(['customer']).sum().reset_index()
df_selected=df_selected.rename(columns={'quantity_in_base_unit':"less_then_30_days"})
df_selected[df_selected['customer'] == 1000096].head(1)


# In[ ]:





# In[161]:


#filter for more then 30 days
selected_date_range = pd.date_range(today - pd.to_timedelta(my_time_delta, unit='d'), today, freq='D')
df_selected_for_more = df[~df["posting_date"].isin(selected_date_range)]
df_selected_for_more=df_selected_for_more[['customer','quantity_in_base_unit']].groupby(['customer']).sum().reset_index()
df_selected_for_more=df_selected_for_more.rename(columns={'quantity_in_base_unit':"more_then_30_days"})
df_selected_for_more[df_selected_for_more['customer'] == 1000096].head(1)


# In[ ]:


# HOMEWORK

# - BRANCH / CHECKOUT / HEAD
# - COMMIT | PUSH | PULL | MERGE | REBASE
# - GIT FLOW
# TEEEST al;'sldasd

#test again.

# In[ ]:




