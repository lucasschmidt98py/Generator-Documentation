# One Dimension Model

All functios used can be find at cpp/one_dimension.cpp

## Neutron Attributes

```{code}
// One Point

float Q;    
float t_death;
float t_birth;
int generation;
vector<float>  basic_prob;

// One Dimension

float x_death;
float x_birth;
float velocity;
```
***All one-point atributes + :***

***x_birth*** : Position of neutrons birth

***x_death*** : Position of neutrons absortion

***velocity*** : Neutrons velocity

## Used Dices:

***dice_branches*** : Dice used in number_branches choice function

***dice_time*** : Dice used in time_iter choice function

***dice_omega*** : Dice used in direction choice function

## Write Function

***`write_trunk( vector<float> basic_prob , string model , int simulation_number , neutron* trunk )`*** : Create first a folder called model and a folder with the two first decimal houses of each probability in the basic_prob vector. Then writes the neutron trunk in a simulation{ simulation_number }.csv. In the One-Dimensional model , the variable string model = 'one_dimension'

## Implemented Trees

***`Od_Pr_Hom_Wb_Tree(int simulation_number , int number_of_neutrons , vector<vector<float>> dice_matrix , const int boundary)`*** : Input the simulation index , the total number of neutrons in the simulation , the dices matrix and the boundaries limits. Output a neutron trunk .csv file using write_trunk function

*Model's Hypothesis :*

$$\tau ~ Exp(0 , \infty)$$

$$\Omega \in \{-1 , 1\}$$

$$velocity = \Omega * |v|$$

One Group of Energy

$$ |v| = 1 $$

One dimension:

$$ t_{death}^{son} = \tau + t_{death}^{father} $$

$$ x_{death}^{son} = \tau*velocity + x_{death}^{father} $$

Prompt Neutron :

$$ t_{birth}^{son} = t_{death}^{father} $$

$$ x_{birth}^{son} = x_{death}^{father} $$

Homogeneous Medium Hypothesis:

$$ f_{k}^{son} = f_{k}^{father} $$

$$ Q^{son} = Q^{father} $$




