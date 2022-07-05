# Python Codes

## General Overview

The python core intends to analyse in the most efficient way, all the data produced by the C++ output simulations. Python was chosed for the capability to load objects in the memory and manipulate them in the study process using jupyter-notebook cells. Besides, the Pandas library is used due to is easy manipulation of DataFrames columns and lines.

Numba library is a key optimizing library since the quantity of calculations made by the CPU is in the order of number_of_neutrons X numer_of_simulations.

## Reading C++ output

After runing C++ code , Python will read all the .csv files in the cpp data path folder and bind them in the memory. The creation of this matrix is made by the function mk_df following the .csv columns format.

## Figures

Figures are made using [Plotly](https://plotly.com/python/) mainly because of its versatility in ploting dataframes
All can be saved as an html in ./figures for a better visualization.

## One Point Code Example

```{code}
import pandas as pd
import numpy as np
import os

import functions
import generator

path = os.path.abspath(os.path.join('..' , '..' , 'cpp' , 'data' , 'one_point' , '0'))
n_sim = 100
t_arr = np.linspace(0 , 20 , 200)

matrix = np.array( functions.mk_pop_df(path , t_arr , n_sim) )

frequency_array , probability_array , all_values = functions.mk_freq_prob(matrix)

frequency_df        = pd.DataFrame( frequency_array   , columns = all_values , index = t_arr )
probability_df      = pd.DataFrame( probability_array , columns = all_values , index = t_arr )
```
