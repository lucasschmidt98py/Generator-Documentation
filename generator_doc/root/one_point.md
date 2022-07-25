# One-Point Model


## Neutron Class

```{code}
class Neutron :  public TObject {
    
    private:

    Int_t                   generation;
    Float_t                 birth_time;
    Float_t                 death_time;
    Float_t                 Q;  
    std::vector<Float_t>    basic_prob;

    Int_t                   index;
    Int_t                   father_index;
    Int_t                   type;
    
};
```

## Neutron's Attributes

***generation***            : Neutron's generation

***number_of_branches***    : Neutron's offspring size

***birth_time***            : Neutron's birth time

***death_time***            : Neutron's interaction time

***Q***                     : Reaction Intensity

***basic_prob***            : Coefficients Vector of basic generation function

```{note}
In an homogeneous medium , Q and basic_prob are constant attributes.
```

## Set Methods
Set Methods are void functions used for assigning neutron private attributes on the assigning loop. They take as input, the assignment value


***` void set_generation(Int_t igeneration) `*** 
<p align="center">
    
    Input :
        Int_t igeneration - Set generation value

    Output:
        void
</p>

***` set_birth_time( Float_t ibirth_time ) `*** 
<p align="center">
    
    Input :
        Int_t ibirth_time - Set Neutron's birth time value
    
    Output :
        void
</p>

***` void set_death_time( Float_t ideath_time) `*** 
<p align="center">
    
    Input :
        Int_t ideath_time - Set generation value

    Output:
        void
</p>

***` set_Q( Float_t iQ ) `*** 
<p align="center">
    
    Input :
        Int_t iQ - Set generation value
    
    Output:
        void
</p>





***` void set_basic_prob( std::vector<Float_t> basic_prob ) `*** 
<p align="center">
    
    Input :
        std::vector<Float_t> basic_prob - Set Basic Probability Coefficients
    
    Output:
        void
</p>

## Get Methods
Get Methods are functions used for getting a neutron private attribute.

***` std::vector<Float_t> get_basic_prob() `*** 
<p align="center">
    
    Input :
        void
    Output:
        std::vector<Float_t> - Return  Neutron's private coefficients vector
</p>

***` Int_t get_generation() `*** 
<p align="center">
    
    Input :
        void
    
    Output:
        Int_t - Return Neutron's private generation 
</p>

***` Float_t get_birth_time() `*** 
<p align="center">
    
    Input :
        void
    
    Output:
        Float_t - Return Neutron's private birth time
</p>

***` Float_t get_death_time() `*** 
<p align="center">
    
    Input :
        void
    
    Output:
        Float_t - Return Neutron's private interaction time
</p>

***` Float_t get_Q() `*** 
<p align="center">
    
    Input :
        void
    
    Output:
        Float_t - Return Neutron's private Reaction Intensity
</p>



## Write Function

***` void write( Int_t number_of_events , Int_t number_of_neutrons , Float_t Q , std::vector<Float_t> basic_prob) `***  : Writes the neutron trunk in a .root fille named with the two first decimal houses of each probability in the basic_prob vector in data folder

<p align="center">
    
    Input :
        TTree  number_of_events    - Number of simulations

        Int_t   number_of_neutrons - Maximum number of simulated neutrons
    
        Float_t Q                  - Reaction Intensity
    
        vector<Float_t> basic_prob - Basic Probability coefficients vector
    
    Output:
        Write a .root fille in the data folder with all the simulations with all the generated neutrons.
</p>


## Implemented Trees

### One Point - Prompt Neutrons - Homogeneous - Infinity Medium

***`void Op_Pr_Hom_Inf_Tree( TTree *tree , Int_t number_of_neutrons , Float_t Q , std::vector<Float_t> basic_prob , Float_t simulation)`*** : Construct a single tree in a simulation

<p align="center">
    
    Input :
        TTree  *tree               - Pointer of a tree

        Int_t   number_of_neutrons - Maximum number of simulated neutrons
    
        Float_t Q                  - Reaction Intensity
    
        vector<Float_t> basic_prob - Basic Probability coefficients vector
    
        Float_t         simulation - Simulation Index
    
    Output:
        void
</p>

*Model's Hypothesis :*

One Point:

$$ t_{death}^{son} = t_{death}^{father} + \frac{ -log(\xi)  }{Q}  $$

Prompt Neutron :

$$ t_{birth}^{son} = t_{death}^{father} $$

Homogeneous Medium Hypothesis:

$$ f_{k}^{son} = f_{k}^{father} $$

$$ Q^{son} = Q^{father} $$

### One Point - Prompt Neutrons and Delayed Neutrons - Homogeneous - Infinity Medium

***`void Op_Pr_Hom_Inf_Tree( TTree *tree , Int_t number_of_neutrons , vector<float> vec_rate , vector<vector<Float_t>> basic_prob_matrix ,Int_t first_type, Int_t simulation`*** : Construct a single tree in a simulation

<p align="center">
    
    Input :
        TTree  *tree                                - Pointer of a tree

        Int_t   number_of_neutrons                  - Maximum number of simulated neutrons
    
        Float_t vec_rate                            - Vector containing the medium intensity rate and precursor decay rate  
    
        vector<vector<Float_t>> basic_prob_matrix   - Basic Probability matrix for neutron and precursors

        Int_t simulation                            - Simulation Index
    
    Output:
        void
</p>

*Model's Description :*

This tree reproduces the model described in {cite}`pazsit2007neutron` Cap 5.5. In this model, a particle $T_{0}$ induces a reaction with intensity Q generating other $n_i$ particles of type $T_i$ , with $ i \in \{1 , 2 , 3 , \dots \} $  and with probability $ f_{n}^{i} $

*Model's Hypothesis :*

Independence:

$$ P( \nu_{0} = k_0 , \nu_1 = k_1 , \dots ) = \Pi_{ i = 0}^{ \text{Number of Groups} } f^{i}( \nu = k_i) $$

One Point:

$$ t_{death}^{son} = t_{death}^{father} + \frac{ -log(\xi)  }{Q}  $$

Prompt Neutron :

$$ t_{birth}^{son} = t_{death}^{father} $$

Delayed Neutron:

$$ t_{birth}^{son} = t_{death}^{father} + \frac{ -log(\xi) }{ \lambda_{i} } $$

Homogeneous Medium Hypothesis:

$$ f_{k}^{son} = f_{k}^{father} $$

$$ Q^{son} = Q^{father} $$


## ROOT Fille 

The fille is located in the data folder and is used on previous processing. 

File Structure:
<p align="center">
    
    Rows    : Number of Neutrons * Number of Simulations
        
    Columns : Generation , Birth Time , Death Time , Simulation Index  
</p>


| gen  | t_birth | t_death | sim  |
| :--- | :------ | :------ | :--- |
| 0    | 0       | $t_0$   | 0    |



