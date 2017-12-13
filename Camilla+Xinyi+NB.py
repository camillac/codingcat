
# coding: utf-8

# In[1]:

import pandas as pd   # We give the libraries short names for easier referencing
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
get_ipython().magic(u'matplotlib inline')
# This allows us to display plots right within our Jupyter notebook


# In[30]:

data_dir = '../datasets/'
obesity = pd.read_csv(data_dir + 'Obesity.csv')
print obesity.columns


# In[31]:

print obesity.shape


# In[40]:

# age
# gender
# race


# In[66]:

obesity_df = pd.DataFrame(columns = [obesity.columns[3:21]])
print obesity_df


# In[55]:

obesity.columns[20]
print [obesity.columns[3:5]]


# In[72]:

obesity


# In[ ]:



