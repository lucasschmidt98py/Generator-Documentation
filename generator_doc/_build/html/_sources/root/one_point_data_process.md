# One Point

A neutron is alive at the instant t of time if:

$$ t_{birth} < t < t_{death} $$

Besides, by the Week Law of Great Numbers we can say:

$$ p_n(t) = \frac{ S(n , t) }{ \sum S(n,t) } $$

Where

* $ S(n,t) = $ Number of simulations with $n$ neutrons alived in time $t$
* $ \sum S(n,t) = $ Total number of simulations 

## Files Format

For futher computations, Python will always read the .csv files columns in the following order of neutrons atributtes:

* column 0 - Generation

* column 1 - Time of Birth

* column 2 - Time of Death

## Functions

***`mk_df(path , n_sim)`*** : Read the n_sim simulations on the data path folder. Return a dataframe with all C++ output .csv binded in a dataframe  

***`time_count(t , matrix):`*** : Count the number of alive neutrons for a float t in the binded dataframe

***`time_count_arr(t_arr , matrix)`*** : Count the number of alived neutrons in a dataframe, for an vector of time. Iterates over the number of t_arr values using the function time_count(t,df) for each entry of the array

***`mk_pop_df(path , t_arr , n_sim)`*** : Output a population dataframe counting with index = t_arr and columns = 'number of simulations in df'. Iterates over the number of simulations present in df. Recive as input the data path folder, an array of time and the number of simulations
    
***`mk_freq_prob(matrix)`*** : Take as input the population matrix counting and output a frequency matrix, probability matrix and an array of counting values that appeared on the population counting matrix

## Generator

***`polinomial(array)`***  :  Create a Square matrix ( size(array) X size(array) ) where each line is a power array of each input array entry 

***`mk_g(matrix , z_size)`*** : Calculates de generation function g(z,t) for a given population counting matrix made by the function mk_pop_df. By default , z is an array in the interval [-1,1] with 100 points.

## Probability of Extinction

Once the probability matrix has been computed using the function ***`mk_freq_prob`*** , the Probability of Extinction is simply the assintotic value of the first column of the matrix and can be called by: 


```{code}
matrix = np.array( functions.mk_pop_df(path , t_arr , n_sim) )

frequency_array , probability_array , all_values = functions.mk_freq_prob(matrix)

frequency_df        = pd.DataFrame( frequency_array   , columns = all_values , index = t_arr )
probability_df      = pd.DataFrame( probability_array , columns = all_values , index = t_arr )

probability_df[0]
```