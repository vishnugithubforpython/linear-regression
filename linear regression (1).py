#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[36]:


from sklearn import linear_model


# In[37]:


df=pd.read_excel("C:/Users/mvish/Desktop/Book2.xlsx")
df


# In[38]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.xlabel("area")
plt.ylabel("price")


# In[39]:


reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)



# In[42]:


reg.predict([[3300]])


# In[46]:


reg.coef_


# In[47]:


reg.intercept_


# In[48]:


135.78767123*3300+180616.43835616432


# In[51]:


df=pd.read_excel("C:/Users/mvish/Desktop/Book3.xlsx")
df


# In[52]:


df.head(3)


# In[55]:


p=reg.predict(df)
p


# In[60]:


df['prices']=p
df



# In[63]:


df.to_excel("prediction.xlsx")

