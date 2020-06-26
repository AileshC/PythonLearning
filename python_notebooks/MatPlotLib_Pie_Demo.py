#!/usr/bin/env python
# coding: utf-8

# ## Single Dimension Array

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = [10, 23, 34, 35, 45, 59]
df = pd.DataFrame(data, columns=['Score'])
df


# In[3]:


#plt.pie(df)
plt.pie(df, labels=df['Score'])
plt.title("Students Score")
plt.show()


# In[4]:


label_name = ['John', 'Tim', 'Kenny', 'AK', 'Helvetica', 'Bryan']


# In[5]:


plt.pie(df, labels=label_name)
plt.title("Students Score")
plt.show()


# In[6]:


plt.pie(df, labels=label_name, autopct='%1.1f%%')
plt.title("Students Score")
plt.show()


# In[7]:


plt.pie(df, labels=label_name, autopct='%1.2f%%')
plt.title("Students Score")
plt.show()


# In[8]:


plt.pie(df, labels=label_name, autopct='%1.3f%%')
plt.title("Students Score")
plt.show()


# ## Two Dimension Array

# In[9]:


new_data = [['John', 10], ['Tim', 24], ['AK', 34]]


# In[10]:


new_data


# In[11]:


newdf = pd.DataFrame(new_data)


# In[12]:


newdf


# In[13]:


newdf = pd.DataFrame(new_data, columns=['Name', 'Score'])


# In[14]:


newdf


# In[15]:


newdf['Score']


# In[16]:


newdf['Name']


# In[17]:


plt.pie(newdf['Score'], labels=newdf['Name'], autopct='%1.1f%%')
plt.show()


# In[ ]:





# In[ ]:




