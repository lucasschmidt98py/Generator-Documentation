#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# # Data Processing
# 
# ## General Overview
# 
# After the simulation , a *.root* fille will be written in the data folder. Root filles are an efficient way for both, writing and reading a big amount of tabular data in C/C++ . Besides, those filles are quite lite and much less heavy then exporting many .csv filles to a folder. The usage of *.root* filles allows to explore the high C performance together with the [MultiThread Class](https://root.cern.ch/doc/master/classTThread.html) giving possibilities to explore a large amount of data , natural from Monte-Carlo simulations. 
# 
# Efficiency of processing is a key point to this part of the project since many simulations may involve a big amount of rows( Number of Neutrons X Number of Simulations ) , especially in strongly supercritical cases.
# 
# The main outputs of the Data Processing are .csv filles that can be easily loaded to R or Python
# 
# An example of simulation of a supercritical scenario data processing

# # Neutron's population time series
# 

# In[2]:


path = '/home/lucas/Documentos/Projects/root-on-vscode/Generator/root/one_point/data'

df = pd.read_csv(os.path.join( path ,'popl_matrix_205525.csv'))
df.index = np.linspace( 0 , 100 , 999)

l = []
for q in range( len(df.columns) ):
    l.append('Simulation {}'.format(q))
df.columns = l
df.iloc[: , :-1]


# # Probability distribution time series

# In[3]:


df = pd.read_csv(os.path.join( path ,'prob_matrix_205525.csv'))
df.index = np.linspace( 0 , 100 , 999)
l = []
for q in range( len(df.columns) ):
    l.append("p({},t)".format(q))
df.columns = l
df.iloc[: , :-1]


# # Frequency time series  Teste

# In[4]:


df = pd.read_csv(os.path.join( path ,'freq_matrix_205525.csv'))
df.index = np.linspace( 0 , 100 , 999)
l = []
for q in range( len(df.columns) ):
    l.append("Frequency {}".format(q))
df.columns = l
df.iloc[: , :-1]

