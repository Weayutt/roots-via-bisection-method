# Author: Wyatt Avilla
# Date 11-17-22
# Asks user for polynomial function and interval and determines if there is a root present using the bisection method
import math
import numpy as np

def poly_function(coefficients, evaluated_at): #evaluates a polynomial at a given point
    terms = [0 for i in range(6)]

    for i in range(len(coefficients)):
        terms[i] = coefficients[i]

    polynomial = f"{terms[0]} + {terms[1]}*x + {terms[2]}*x**2 + {terms[3]}*x**3 + {terms[4]}*x**4 + {terms[5]}*x*5"
    return eval(polynomial.replace("x", str(f"({evaluated_at})")))

def derive(coefficients):  #derives a polynomial based on coefficients
    derivative = []
    coefficients.pop(0)
    for i in range(len(coefficients)):
        derivative.append(int(coefficients[i])*(i+1))
    return derivative

def oppositeSigns(x, y):   #checks if x and y have opposite parity
    if np.sign(float(x)) != np.sign(float(y)):
        return True
    else:
        return False

def x_crosses(coefficients, a, b): #determines if polynomial equation crosses the x axis at a given interval given its coefficients
    x = poly_function(coefficients, a)
    y = poly_function(coefficients, b)
    return oppositeSigns(x,y)

def get_roots(coefficients, interval, iterations=1000, tolerance=1e-06): #Bisection method implementation
    n = 0
    L = float(interval[0])
    R = float(interval[1])
    c = (L+R)/2
    while n < iterations:
        if (poly_function(coefficients, c) == 0) or (abs(poly_function(coefficients, c)) < tolerance):
            return c
        else:
            n+=1
            fofc = poly_function(coefficients, c)
            fofl = poly_function(coefficients, L)
            if fofc == 0:
                return c
            if fofl == 0:
                return L
            if (oppositeSigns(fofc, fofl) == False):
                L = c
            else:
                R = c
        c = (L+R)/2

def get_subintervals(r, interval):  #divides interval into "r" equal segments
    subintervals = []
    L = float(interval[0])
    R = float(interval[1])
    span = (R-L)/r
    for i in range(r):
        subintervals.append([L, L+span])
        L = L+span
    return subintervals



roots = []
tolerance = tolerance=1e-06
copy_coefficients = []
user_coefficients = input("Enter the polynomial coefficients:\n").split(" ")
interval = input("Enter the interval:\n").split(" ")

for x in user_coefficients:
    copy_coefficients.append(x)

subintervals = get_subintervals(5, interval)

for x in subintervals:   #determines if roots are present at each print(subintervals) using the given function
    if get_roots(user_coefficients, x) != None:
        roots.append(round(get_roots(user_coefficients, x), 5))

derivative = derive(user_coefficients)

for x in subintervals:
    possible_root = get_roots(derivative, x)  #plugs roots of derived function into initial function and determines if they are near 0
    if possible_root != None:
        if abs(poly_function(copy_coefficients, possible_root)) < tolerance:
            roots.append((round(possible_root,5)))

if len(roots) == 0:
    print("No roots are found!")
else:
    for root in roots:
        print(f"Root found at {root}")