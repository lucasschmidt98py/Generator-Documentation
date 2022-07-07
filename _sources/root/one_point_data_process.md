# One Point

A Neutron is alive at the time t if:

$$ t_{birth} < t < t_{death} $$

Besides, by the Week Law of Great Numbers we can say:

$$ p_n(t) = \frac{ S_{n}(t) }{ \sum_{n = 0}^{\infty} S_{n}(t) } $$

Where

* $ p_n(t)      = $ Probability of finding n alive neutrons in time $t$ 
* $ S_{n}(t)      = $ Number of simulations with $n$ alive neutrons in time $t$
* $ \sum_{n = 0}^{\infty} S_{n}(t) = $ Total number of simulations 


## Basic Functions 

***`vector<vector<Float_t>> create_matrix()`*** : Load the {p_string}.root file to C. The reading follows the columns structures created at the simulation

<p align="center">
    
    Input :
        void
    
    Output:
        vector<vector<Float_t>> return_matrix - Root Matrix containing all neutron attributes from all simulations. 
</p>

***`vector<vector<Float_t>> filter_simulation( Int_t sim , vector<vector<Float_t>> matrix )()`*** : Select a trunk for a given simulation in a given Root Matrix

<p align="center">
    
    Input :
        
        Int_t sim - Simulation Number

        vector<vector<Float_t>>  matrix - Root Matrix
    
    Output:
        vector<vector<Float_t>> return_matrix - Trunk from simulation sim 
</p>

***`vector<Float_t> linspace( Float_t t0 , Float_t tf , Int_t n_spaces )`*** : Create a partition of the interval [ $t_0$ , $t_f$ ] in $n_{spaces}$ intervals

<p align="center">
    
    Input :
        
        Float_t t0 - Initial time

        Float_t tf - Final time

        Int_t n_spaces - Number of Intervals

    Output:
        vector<Float_t> return_arr - Partitioned interval array
</p>

***`vector<Int_t> arange(Int_t size)`*** : Return a sequency of natural numbers smaller then size + 1

<p align="center">
    
    Input :
        
        Int_t size - Sequence limit

    Output:
        vector<Float_t> return_arr - Sequence of naturals
</p>

***`Int_t find_max( vector<vector<Int_t>> matrix )`*** : Find the maximum natural number in a given matrix of natural numbers
 
<p align="center">
    
    Input :
        
        vector<vector<Int_t>> matrix - Matrix of natural numbers
    
    Output:
        Int_t max - Maximum number 
</p>


## Counting Functions

***`Int_t time_count( Float_t t , vector<vector<Float_t>> matrix )`*** : Count the number of alive neutrons for a given time $t$ in a given trunk
 
<p align="center">
    
    Input :
        
        Float_t t - Instant of time

        vector<vector<Float_t>> matrix - Trunk from a given simulation
    
    Output:
        Int_t count - Number of alive neutrons at the time t 
</p>

***`Int_t value_count( Int_t value , vector<Int_t> value_arr )`*** : Count the number of times that a natural number pop up in a vector of natural numbers 

<p align="center">
    
    Input :
        
        Int_t value - Counting value

        vector<Int_t>> value_arr - Vector of natural numbers
    
    Output:
        Int_t - Number of alive neutrons at the time t 
</p>

## Matrix Construction Functions

***`vector<vector<Int_t>> population_matrix( vector<Float_t> time_arr , vector<vector<Float_t>> matrix )`*** : Construct the population matrix indexed by the time_arr argument. 


$ i = $ time_arr index

$ j = $ Simulation number

$ [N_{ij}] = $ Number of alive neutrons $ N_{j}(t) $

<p align="center">
    
    Input :
        
        vector<Float_t> time_arr - Time array partition

        vector<vector<Float_t>> matrix - Root Matrix
    
    Output:
        vector<vector<Int_t>> return_matrix- Neutron population time series matrix for each simulation  
</p>



***`vector<vector<Int_t>> freq_matrix( vector<Float_t> time_arr , vector<vector<Float_t>> matrix )`*** : Construct the simulation frequency values counting.

$ i = $ time_arr index

$ j = \text{Neutron population value} \in \{ 1 , 2 , 3 , \dots \max{\text{Root Matrix}} \}$ 

$ [s_{ij}] = $ Counting of simulations $S_j(t)$ 


***`vector<vector<Float_t>> prob_matrix( vector<vector<Int_t>> freq , Int_t n_sim )`*** : Construct the probability distribution time series . 

$ i = $ time_arr index

$ j = \text{Neutron population value} \in \{ 1 , 2 , 3 , \dots \max{\text{Root Matrix}} \}$

$ [p_{ij}] = $ Neutron's population probability $ p_j(t) $ 

<p align="center">
    
    Input :
        
        vector<vector<Int_t>> freq - Matrix of Neutron's population value frequencies

        Int_t n_sim - Number of simulations
    
    Output:
        vector<vector<Float_t>> return_matrix - Probability Distribution time series 
</p>