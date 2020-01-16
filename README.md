# SAT-Project
### Sudoku using Z3 SAT Solver - MOSIG M2 - AISSE

In this project we implemented the basic structure for the Sudoku puzzle in the Python language. Using the Z3 library we were also able to code the puzzle into a SAT problem and find its solutions, or determine if there are no solutions. The Sudoku board can be represented as such:

```
 A1 A2 A3| A4 A5 A6| A7 A8 A9
 B1 B2 B3| B4 B5 B6| B7 B8 B9   
 C1 C2 C3| C4 C5 C6| C7 C8 C9   
---------+---------+---------   
 D1 D2 D3| D4 D5 D6| D7 D8 D9   
 E1 E2 E3| E4 E5 E6| E7 E8 E9   
 F1 F2 F3| F4 F5 F6| F7 F8 F9   
---------+---------+---------   
 G1 G2 G3| G4 G5 G6| G7 G8 G9   
 H1 H2 H3| H4 H5 H6| H7 H8 H9   
 I1 I2 I3| I4 I5 I6| I7 I8 I9 
```
The **input** format for our program can be given in two forms. For a 9x9 grid we have:

1) Format (i,j,c) where value at grid position (i,j) is c for all i,j,c in [1..9]:

```
Example:

Input = [(1,1,2), (1,2,9), (1,4,3), (1,6,8), (2,3,6), (2,4,4), (2,8,5), (3,4,7), (3,8,9), (4,3,1), (4,9,8), (5,1,7),(5,5,9) ,(5,7,3), (6,1,3), (6,9,5), (7,6,2), (7,9,6), (8,2,8), (8,5,1), (8,7,5) ,(9,1,5), (9,2,2), (9,5,8)]

Represents the following board configuration:

['2', '9', '0', '3', '0', '8', '0', '0', '0']
['0', '0', '6', '4', '0', '0', '0', '5', '0']
['0', '0', '0', '7', '0', '0', '0', '9', '0']
['0', '0', '1', '0', '0', '0', '0', '0', '8']
['7', '0', '0', '0', '9', '0', '3', '0', '0']
['3', '0', '0', '0', '0', '0', '0', '0', '5']
['0', '0', '0', '0', '0', '2', '0', '0', '6']
['0', '8', '0', '0', '1', '0', '5', '0', '0']
['5', '2', '0', '0', '8', '0', '0', '0', '0']
['2', '9', '4', '3', '5', '8', '1', '6', '7']
['1', '7', '6', '4', '2', '9', '8', '5', '3']
['8', '3', '5', '7', '6', '1', '2', '9', '4']
['9', '5', '1', '2', '4', '3', '6', '7', '8']
['7', '6', '2', '8', '9', '5', '3', '4', '1']
['3', '4', '8', '1', '7', '6', '9', '2', '5']
['4', '1', '9', '5', '3', '2', '7', '8', '6']
['6', '8', '7', '9', '1', '4', '5', '3', '2']
['5', '2', '3', '6', '8', '7', '4', '1', '9']
```
2) A string format of characters with 1-9 indicating a digit, and a period specifying an empty square. 

```
Example:

Input = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

Represents the following board configuratio:

['0', '0', '3', '0', '2', '0', '6', '0', '0']
['9', '0', '0', '3', '0', '5', '0', '0', '1']
['0', '0', '1', '8', '0', '6', '4', '0', '0']
['0', '0', '8', '1', '0', '2', '9', '0', '0']
['7', '0', '0', '0', '0', '0', '0', '0', '8']
['0', '0', '6', '7', '0', '8', '2', '0', '0']
['0', '0', '2', '6', '0', '9', '5', '0', '0']
['8', '0', '0', '2', '0', '3', '0', '0', '9']
['0', '0', '5', '0', '1', '0', '3', '0', '0']
['4', '8', '3', '9', '2', '1', '6', '5', '7']
['9', '6', '7', '3', '4', '5', '8', '2', '1']
['2', '5', '1', '8', '7', '6', '4', '9', '3']
['5', '4', '8', '1', '3', '2', '9', '7', '6']
['7', '2', '9', '5', '6', '4', '1', '3', '8']
['1', '3', '6', '7', '9', '8', '2', '4', '5']
['3', '7', '2', '6', '8', '9', '5', '1', '4']
['8', '1', '4', '2', '5', '3', '7', '6', '9']
['6', '9', '5', '4', '1', '7', '3', '8', '2']
```

  The input should be set at the first lines of the satSudoku.py file. The internal processing of the puzzle is done in the second format, so if an input configuration is provided in the first format, the function __convertInput(grid)__ should be used. At the end of each run, the console will print out the solution, if there is one, in the form of a 9x9 Matrix. In addition it will inform the time took to solve the puzzle, given in miliseconds. 

  Finally, the SAT solver uses functions from the Z3-Solver library available [here](https://github.com/Z3Prover/z3). Moreover, the structure of the Sudoku game constructed in Python was inspired by partially inspired by this [tutorial](https://norvig.com/sudoku.html) online. 
