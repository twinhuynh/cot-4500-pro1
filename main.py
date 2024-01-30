import math

# Define the function f and its derivative f_prime
def f(x):
    return x**3 + 4*x**2 - 10
def f_prime(x):
    return 3*x**2 + 8*x

## 1. Approximation Algorithm
def approximation_algorithm(p0, tol=1e-4, max_iterations=100):
    iterations= 1

    while iterations <= max_iterations:
        # Compute pi using approximation algorithm
        p = p0 - f(p0) / f_prime(p0)

        # Display current iteration information
        print(f"{iterations}: p = {p}")

        # Check for convergence
        if abs(p - p0) < tol:
            return math.ceil(iterations), p  # The procedure was successful

        iterations+= 1
        p0 = p  # Update p0

    # The method failed after N0 iterations
    print(f"The method failed after {max_iterations} iterations.")
    return math.ceil(max_iterations), None  # The procedure was unsuccessful

# Initial approximation
p0 = 1

# Perform approximation algorithm
result_iterations, result_approximation = approximation_algorithm(p0)
print(f"Convergence after {result_iterations} iterations")

print("\n")

## 2. The bisection method 
def bisection_method(a, b, tol=1e-4, max_iterations=100):
    if f(a) * f(b) > 0:
        raise ValueError("The function values at the endpoints must have opposite signs.")

    iterations = 1

    while iterations <= max_iterations:
        c = (a + b) / 2

        # Display current iteration information
        print(f"{iterations}: {c}")

        if f(c) == 0 or (b - a) / 2 < tol:
            return math.ceil(iterations), c  # The procedure was successful

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    print(f"The method failed after {max_iterations} iterations.")
    return math.ceil(max_iterations), None  # The procedure was unsuccessful

# Initial interval
a = -4
b = 7

# Perform bisection method
result_iterations, result_approximation = bisection_method(a, b)
print(f"Convergence after {result_iterations} iterations")

print("\n")

## 3. Fixed point iteration
def fixed_point_iteration(g, p0, tol=1e-8, max_iterations=20):
  iterations = 1
  
  # print initial iteration
  print(f"{iterations}: {p0}")
  while iterations < max_iterations:
      # Compute pi using the fixed-point iteration formula
      p = g(p0)

      # Display current iteration information
      print(f"{iterations + 1}: {p}")

      # Check for convergence
      if abs(p - p0) < tol:
          return iterations + 1, p  # The procedure was successful

      iterations += 1
      p0 = p  # Update p0

  # The method failed after N0 iterations
  print(f"The method failed after {max_iterations} iterations.")
  return iterations + 1, None  # The procedure was unsuccessful

# Define the function for fixed-point iteration
def g(x):
  return x - f(x) / f_prime(x)

# Initial approximation
p0 = 1.5

# Perform fixed-point iteration
result_iterations, result_approximation = fixed_point_iteration(g, p0)
print(f"Convergence after {result_iterations} iterations")

print("\n")

## 4. Newton-Raphson method
def newton_raphson_method(initial_guess, tol=1e-4, max_iterations=100):
  x = initial_guess
  iterations = 1

  while iterations <= max_iterations:
      x_new = x - f(x) / f_prime(x)

      # Display current iteration information
      print(f"{iterations}: {x_new}")

      if abs(x_new - x) < tol:
          return math.ceil(iterations), x_new  # The procedure was successful

      x = x_new
      iterations += 1

  print(f"The method failed after {max_iterations} iterations.")
  return math.ceil(max_iterations), None  # The procedure was unsuccessful

# Initial Guess
initial_guess = 7

# Perform Newton-Raphson method
result_iterations, result_approximation = newton_raphson_method(initial_guess)
print(f"Convergence after {result_iterations} iterations")
