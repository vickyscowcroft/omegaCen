
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df_resid_theo = pd.read_csv('final_data_files/uncrowded_withresid.csv')
df_resid_m4 = pd.read_csv('final_data_files/uncrowded_withresid_m4.csv')


# In[3]:

df_resid = df_resid_theo.merge(df_resid_m4, how='outer',
                               on=list(set(df_resid_theo.keys()) & set(df_resid_m4.keys())))


# In[4]:

photfeh = pd.read_csv('rey_2000.cat', usecols=[0,2,3],
                      names = ['id', 'photfeh', 'photfeh_err'],
                      delim_whitespace=True)


# In[5]:

df_with_feh = df_resid.merge(photfeh, how='outer', on='id')


# In[6]:

spectfeh = pd.read_csv('sollima_2006.cat', usecols=[0,2,3],
                      names = ['id', 'spectfeh', 'spectfeh_err'],
                      delim_whitespace=True)


# In[7]:

df_with_feh = df_with_feh.merge(spectfeh, how='outer', on='id')


# In[8]:

cols = list(df_with_feh.columns.values)
print cols


# In[9]:

cols_reordered = ['id', 'type', 'per', 'mag_j', 'merr_j', 'mag_h', 'merr_h',
                  'mag_k', 'merr_k', 'mag_3', 'merr_3', 'mag_4', 'merr_4',
                  'resid_theo_3', 'resid_theo_4', 'resid_m4_3', 'resid_m4_4',
                  'photfeh', 'photfeh_err', 'spectfeh', 'spectfeh_err']


# In[10]:

df = df_with_feh[cols_reordered].sort('id')


# In[11]:

df.columns.values


# In[12]:

df.to_csv('final_data_files/uncrowded_everything.csv', index=False)


# In[ ]:



