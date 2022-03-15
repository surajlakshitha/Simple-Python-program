# Simple-Python-program

Problem Description
In this problem, need to create a dynamic grid with 2 digits random numbers. In this grid we
have to use some empty slots with some no. of 2 digits numbers, which gain randomly generated,
and also must check for possible percolations. (The percolation is not possible for a column if the
column consists of one or more empty spaces from top to bottom, the percolation is possible for
a column if the entire column consists numbers from top to bottom).
Solution Outline
For this given problem we have to design a program to overcome with a solution, therefore we
use some modules and packages to develop the program.
To generate grid using the list we have to import module other than NumPy therefore we use the
Tabulate Module as tabulate and also to get random number we use the random module as
randInt. Therefore firstly we import two of those modules.
After that we getting two input for the column and rows and validate the input to the given range
as 3 to 9 and input is an integer or not?
Then we introducing one list in range of 10 to 100 and extent the list with space string (" ").
Finally, we creating list as grid and result.
Grid list to list of random integers within the given rows and column and also result list to get
"OK/NO" value (If the column exist the above mention space string given the output as NO
using some if else function and if the column doesn't exist space then it will give the output as
OK).
Apply two for loop to the program. One FOR loop to add random number to Grid List and
another one to check the column if space exist or not.
Finally, to save the solution output in Text File and Html File using the file handling we want get
name from the user to save the file in locally and after that using that name file will save locally
and given out message as 'File Saved Successfully'.
