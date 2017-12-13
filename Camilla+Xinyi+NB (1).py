
# coding: utf-8

# In[91]:

import pandas as pd   # We give the libraries short names for easier referencing
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
get_ipython().magic(u'matplotlib inline')
# This allows us to display plots right within our Jupyter notebook


# In[92]:

data_dir = '../datasets/'
obesity = pd.read_csv(data_dir + 'Obesity.csv')
print obesity.columns


# In[93]:

print obesity.shape


# In[94]:

# age
# gender
# race


# In[95]:

obesity_df = pd.DataFrame(columns = [obesity.columns[3:21]])
print obesity_df


# In[96]:

obesity.columns[]
print [obesity.columns[3:5]]


# In[97]:

obesity


# In[101]:

legend = {'CO':'b', 'US':'r'}
obesity.plot(style = legend)
plt.title("Spotify data as a function of time",fontsize=20)
plt.ylabel("Streams",fontsize=20)
plt.xlabel("Years",fontsize=20)


# In[ ]:




# In[ ]:



