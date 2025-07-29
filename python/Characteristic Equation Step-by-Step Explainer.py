# ---/// Characteristic Equation Step-by-Step Explainer ///---

import numpy as np
from sympy import Matrix, symbols, eye, det, pprint

print("Let's find the characteristic equation of a square matrix!\n")
n = int(input("Enter the matrix size (2-6 for n x n): "))
print(f"Enter the entries for your {n}x{n} matrix, row by row (comma-separated):")
A = []
for i in range(n):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Row must have {n} entries.")
    A.append([float(x) for x in row])

sym_A = Matrix(A)
lam = symbols('lambda')
I = eye(n)
char_poly = det(sym_A - lam*I)

print("\nStep 1: Characteristic polynomial is det(A - λI) = 0")
print("\nA - λI:")
pprint(sym_A - lam*I)
print("\nStep 2: Compute the determinant as a polynomial in λ:")
print("Characteristic polynomial:")
pprint(char_poly)
print("\nStep 3: Characteristic equation is:")
pprint(char_poly)
print(" = 0")
