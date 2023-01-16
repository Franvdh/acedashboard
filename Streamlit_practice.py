#!/usr/bin/env python
# coding: utf-8

# In[3]:


#My First App 
#Here's our first attempt at using data to create a table: 
import streamlit as st
import pandas as pd
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
df




import yfinance as yf
#BTC Dataframe
BTC_Ticker = yf.Ticker("BTC-EUR")
BTC_Data = BTC_Ticker.history(period="ytd")

#XRP Dataframe
XRP_Ticker = yf.Ticker ("XRP-EUR")
XRP_Data = XRP_Ticker.history(period='ytd')

#Add column cointype
BTC_Data['coin_type']="BTC"
XRP_Data['coin_type']="XRP"
BTC_XRP = pd.concat([BTC_Data, XRP_Data],axis=0)


# In[5]:


BTC_XRP


# In[7]:


date=st.slider('Value on date')
st.write(date,'squared is', date*date)


# In[ ]:
import matplotlib.pyplot as plt
import seaborn as sns
fig=plt.figure(figsize=(20,15))
sns.lineplot(data=BTC_XRP, x="Date", y="Volume",hue="coin_type")
st.pyplot(fig) 

# In[ ]:

import plotly.express as px

df = BTC_XRP
fig = px.line(df, y="Volume", color="coin_type")
st.plotly_chart(fig)


# In[ ]:




