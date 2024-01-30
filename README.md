The program reads in the function 'f' and its derivative 'f_prime.'
Then it uses each methods:

1. Approximation Algorithm : 
2. The bisection Method 
3. The fixed-point Iteration
4. The Newton-Raphson method 

to find the roots of the given equation (f(x)).

Assignment: Programming Assignment 1

Author: Tuyen Huynh 

School: University of Central Florida

Language: Python

To Compile: 
1. Copy the python file (main.py) path; should be (cot-4500-Pro1/main.py)
2. Access the Config files on replit (.replit) 
3. Change -> entrypoint equal to the file path; should be entrypoint = "cot-4500-Pro1/main.py"
4. Change -> the second variable in the run column; should be run = ["python3", "cot-4500-Pro1/main.py"]

To Execute: Click the Run button at the top

How to set Test Cases: 
1. Define the function f (line 4-5) and its derivative f_prime (line 6-7) test case.
    Note: f and f_prime will be the same for all 4 methods.

2. Approximation Algorithm:
    1. Change 'tol' and 'max_iterations' as needed (line 10)
      Note: The 'tol' is the tolerance for the desired accuracy and 'max_iterations' is to prevent infinite loops
    2. Change the 'p0' as needed (line 32)
      Note: 'p0' is the initial approximation

3. The bisection Method 
    1. Change 'tol' and 'max_iterations' as needed (line 41)
      Note: The 'tol' is the tolerance for the desired accuracy and 'max_iterations' is to prevent infinite loops
    2. Change 'a' (line 67) and 'b' as needed
      Note: 'a' and 'b' are the initial interval

4. The fixed-point Iteration
    1. Change 'tol' and 'max_iterations' as needed (line 77)
      Note: The 'tol' is the tolerance for the desired accuracy and 'max_iterations' is to prevent infinite loops
    2. Change 'p0' (line 105)
      Note: 'p0' is the initial approximation
  
5. The Newton-Raphson method
    1. Change 'tol' and 'max_iterations' as needed (line 114)
      Note: The 'tol' is the tolerance for the desired accuracy and 'max_iterations' is to prevent infinite loops
    2. Change 'initial_guess' as needed
      Note: 'initial_guess' is the initial approximation
