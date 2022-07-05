# Data Processing

## General Overview

After the simulation , a *.root* fille will be written in the data folder. Root filles are an efficient way for both, writing and reading a big amount of tabular data in C/C++ . Besides, those filles are quite lite and much less heavy then exporting many .csv filles to a folder. The usage of *.root* filles allows to explore the high C performance together with the [MultiThread Class](https://root.cern.ch/doc/master/classTThread.html) giving possibilities to explore a large amount of data , natural from Monte-Carlo simulations. 

Efficiency of processing is a key point to this part of the project since many simulations may involve a big amount of rows( Number of Neutrons X Number of Simulations ) , especially in strongly supercritical cases.

The main outputs of the Data Processing are .csv filles that can be easily loaded to R or Python

* neutron's population time series
(Colocar um exemplo em pandas)

* probability distribution time series
(Colocar um exemplo em pandas)

* frequency time series 
(Colocar um exemplo em pandas)

