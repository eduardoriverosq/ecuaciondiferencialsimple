#!/usr/bin/env python
# coding: utf-8

# In[98]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# In[99]:


def f(y,x):
    return (x**2)*(1+y)


# In[100]:


def ex(x):
    return 4*(np.exp(x**3/3))-1


# In[101]:


y0=3.0
x=np.linspace(0,10,100)


# In[102]:


sol=integrate.odeint(f,y0,x)


# In[103]:


fig, axes=plt.subplots()
axes.plot(x,sol,'--')
axes.plot(x,ex(x))
plt.show()


# In[ ]:




