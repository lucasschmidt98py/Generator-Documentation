# Data Processing

## General Overview

After the simulation , a *.root* fille will be written in the data folder. Root filles are an efficient way for both, writing and reading a big amount of tabular data in C/C++ . Besides, those filles are quite lite and much less heavy then exporting many .csv filles to a folder. The usage of *.root* filles allows to explore the high C performance together with the [MultiThread Class](https://root.cern.ch/doc/master/classTThread.html) giving possibilities to explore a large amount of data , natural from Monte-Carlo simulations. 

Efficiency of processing is a key point to this part of the project since many simulations may involve a big amount of rows( Number of Neutrons X Number of Simulations ) , especially in strongly supercritical cases.

## Root file switcher

A root file can be processed by passing the file name as a string to the global variable p_string at MCAnalysis.C

Example:

```{code}
const string p_string = "205525";
```

## Output

The main Data Processing outputs are .csv filles that can be easily loaded to R or Python. Those are:

* Population Time Series of all simulations
* Probability Distribution
* Frequency Time Series for all simulations

## Processing Time Statistics

In order to control the functions's performance, time counters are implemented using the [TStopwatch](https://root.cern.ch/doc/master/classTStopwatch.html) class. 

```
------------------%%%%%%%%%%------------------ 
 ************ Program Statistics ************  
                                               
                 Reading Time:                 
Real time 0:00:00, CP time 0.050
---------------------------------------------- 
       Population Matrix Processing Time:      
Real time 0:00:00, CP time 0.060
---------------------------------------------- 
         Frequency Matrix Processing Time:     
Real time 0:00:00, CP time 0.000
---------------------------------------------- 
        Probability Matrix Processing Time:    
Real time 0:00:00, CP time 0.000
---------------------------------------------- 
            Exporting to .CSV Time:            
Real time 0:00:00, CP time 0.010
---------------------------------------------- 
                  Code Run Time:               
Real time 0:00:00, CP time 0.120
---------------------------------------------- 
                      End                      
------------------%%%%%%%%%%------------------
```
