#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import datetime as dt
import calendar


# In[17]:


data=pd.read_csv("C:\\Users\\ADMIN\\Dropbox\\PC\\Downloads\\Unemployment in India.csv")
data.head()


# In[4]:


df.isnull().sum()


# In[5]:


df.dropna(axis=0,inplace=True)


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.head()


# In[9]:


df.columns


# In[1]:


plt.figure(figsize=(15,5))
plt.plot(df['Date'],df['Region'])


# In[2]:


plt.figure(figsize=(15,5))
plt.plot(data['Date'],df['Region'])


# In[3]:


plt.figure(figsize=(15,5))
plt.plot(data['Date'],data['Region'])


# In[4]:


plt.figure(figsize=(15,5))
plt.plot(data['Date'],data['Region'])


# In[5]:


plt.figure(figsize=(15,5))
plt.plot(data['Date'],data['Estimated Unemployment Rate (%)'])


# In[6]:


plt.figure(figsize=(15,5))
plt.plot(data['Date'],data['Estimated Unemployment Rate (%)'])


# In[ ]:




