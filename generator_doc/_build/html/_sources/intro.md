# Generator Project Overview

The Generator Project is a Monte Carlo set of codes for the generation of Branching trees. The project make great use of the ROOT framework both for simulation and processing a high amount of data with high performance in C/C++. Since the project was created in the context of the Branching Processes investigation, a set of Jupyter-Notebooks make use of the Python core, designed for analysis and plotting the processed data from the code. The implemented analysis functions follows the well established works in the Theory of the Branching Processes (Adicionar Ref à bibliografia). 

The project have implemented today, the following branching models:

| Geometry        | Kind of Neutrons | Medium      | Groups of Energy | Boundaries           |
| :-------------- | :--------------- | :---------- | :--------------- | :------------------- |
| One-Point       | Prompt           | Homogeneous |                  | Infinity             |
| One-Point       | Prompt           | Varying     |                  | Infinity             |
| One-Point       | Prompt-Delayed   | Homogeneous |                  | Infinity             |
| One-Dimensional | Prompt           | Homogeneous | 1                | Absorbing Boundaries |


It is intended to extend to more complex geometries , more generic medium , with more kinds of neutrons( Delayed - Prompt ) and compare with the results from the Nuclear Reactor Theory. A first comparison already have been done! ( Adicionar Ref ao meu trabalho )

# How to run

The trees constructions can be find at Branch.C script , while the data processing is at MCAnalysis.C script. After linking the main scripts using the MakeFille, the .so compilation can be loaded inside root console and the *write* functions can be called. After a successful simulation, a .root fille will be write in the data folder. The processing of the simulation's data can be made calling the MCAnalysis.C also inside root console.

```{bibliography}
```