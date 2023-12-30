#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googlesearch import search


# In[7]:


query = "salman khan"


# In[8]:


results = [result for result in search (query, num_results=5)]
for i, result in enumerate(results, 1):
    print(f"Result {i}: {result}")


# In[ ]:




