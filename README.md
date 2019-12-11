# K-MapSolver
This python application solves k-map for up-to 4 variables. It solves the given K-map using Quine-McCluskey and Petrick algorithm.
The methods basically involve two steps:
1. Finding the prime implicants of a given Boolean function.
2. Use of those prime implicants in a prime implicant chart to find the essential prime implicants of the function, as well as other prime implicants that are necessary to cover the function.

The details about the algorithms can be found at https://en.wikipedia.org/wiki/ Quine%E2%80%93McCluskey_algorithm, https://en.wikipedia.org/wiki/ Petrick%27s_method and http://www.cs.columbia.edu/~cs6861/handouts/ quine-mccluskey-handout.pdf

# To run the Application
Clone the repository and extract the folder. To run the file, you need to have python3 installed. You can follow instructions given in this website (https://realpython.com/installing-python/) to install python3. Also, you need to make sure that the following modules are already installed in your system.
1. copy

Once you have installed python3 and the modules, you can run the file by opening the folder location in your terminal/Command Line and typing in the following command - python3/python k_MapSolver.py

# Input Format
First enter the number of variables you want to solve k-map for. In the next line, enter the numbers where 1 is in the Karnaugh Map, and in the next line enter all the don't care numbers with spaces in between them.

Output is printed in the next line.
