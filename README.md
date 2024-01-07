# 8_puzzle_AI

## Table of Contents
1. [Short Task Description](#1-short-task-description)
2. [Software Architecture Diagram](#2-software-architecture-diagram)
3. [Short Descriptions of Modules and Interfaces](#3-short-descriptions-of-modules-and-interfaces)
4. [Explain Design Decisions](#4-explain-design-decisions)
5. [Discussion and Conclusions](#5-discussion-and-conclusions)
6. [Possible Improvements](#6-possible-improvements)

## 1. Short Task Description

We were asked to create an 8 Puzzle Solver fulfilling following tasks:

• From a random start state

• Check for solvability

• Generate goal state

• Using at least 2 different heuristic 
functions

• Provide estimate of algorithms 
complexity

• Implementation in Python or Java

• Measure memory effort (number of 
nodes expanded) and run time for 
each of 100 random states and each 
heuristics

• Provide mean and standard deviation 
of memory usage and execution time 
for each heuristics


## 2. Software Architecture Diagram

├── main.py   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ├── compare_heuristics.py


├── solver.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ├── solvable.py




## 3. Short Descriptions of Modules and Interfaces

We decided to separate the program into four modules which are:

`main.py` - Testing the two heuristics by either entering own puzzle or generating a random puzzle

`solvable.py` - Contains methods that checks the solvability by counting inversions

`solver.py` - includes all the algorithms and heuristics, as well as the functionality to solve a puzzle

`compare_heuristics` - Compares the heuristics by solving 100 random puzzles and calculating the Average Memory Usage and Average Computation Time


## 4. Explain Design Decisions

Separating the program into these modules gives us a better overview and makes it
easier to expand the program with more heuristics or testing methods. With this modular
design, we can build more functionalities in the future e.g. visualisation of the puzzle.

## 5. Discussion and Conclusions

### Describe Your Experience
Implementing A* and the heuristic was not so hard for us, as we already learned about this algorithm in a previous lecture.

The challenges we faced were:

- understanding inversions and how they are connected with the solvability of the puzzle
- implementing the `compare_heuristics.py` module

### Table with Complexity Comparisons of Different Heuristics

| Heuristic             | Time Complexity | Space Complexity |
|-----------------------|------------------|-------------------|
| Hamming Heuristic     | O(N^2)           | O(N^2)            |
| Manhattan Heuristic   | O(N^2)           | O(N^2)            |


## 6. Possible Improvements

- Refinement of existing heuristics.
- Addition of new heuristic options.
- Visualisation of the puzzle

