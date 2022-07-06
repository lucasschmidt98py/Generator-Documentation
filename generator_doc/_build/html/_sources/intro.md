# Generator Project Overview

The Generator Project is a Monte Carlo set of codes that generates Branching Trees. The project makes great use of the ROOT framework, both for simulation and processing high amount of data with high performance in C/C++. Since the project was created in the context of the Branching Processes investigation, a set of Jupyter-Notebooks uses Python core designed for analysis and plotting the processed data from the code. The implemented analysis functions follow the well established works in the Theory of the Branching Processes such as {cite}`pazsit2007neutron` , {cite}`athreya2004branching` , {cite}`harris1963theory` and {cite}`feller1971introduction` 

At this moment, following branching models are implemented in the project:

| Geometry        | Kind of Neutrons | Medium      | Groups of Energy | Boundaries           |
| :-------------- | :--------------- | :---------- | :--------------- | :------------------- |
| One-Point       | Prompt           | Homogeneous |                  | Infinity             |
| One-Point       | Prompt           | Varying     |                  | Infinity             |
| One-Point       | Prompt-Delayed   | Homogeneous |                  | Infinity             |
| One-Dimensional | Prompt           | Homogeneous | 1                | Absorbing Boundaries |


It is intended to extend to more complex geometries , more generic medium , with more kinds of neutrons( Delayed - Prompt ) and compare with the results from the Nuclear Reactor Theory

# How to run

The trees constructions can be found at Branch.C script , while the data processing is at MCAnalysis.C script. After linking the main scripts using the MakeFille, the .so compilation can be loaded inside root console and the *write* function can be called. After a successful simulation, a .root fille will be write in the data folder. The processing of the simulation's data can be made calling the MCAnalysis.C also inside root console.

# References

```{bibliography}
```