# ---/// Least Squares Step-by-Step Explainer ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's solve an overdetermined system Ax = b by Least Squares!\n")
m = int(input("Enter the number of equations (rows) m (e.g. 3): "))
n = int(input("Enter the number of unknowns (columns) n (e.g. 2): "))

print(f"Enter your {m}x{n} matrix A row by row (comma-separated):")
A = []
for i in range(m):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

print(f"\nEnter the entries of b (length {m}, comma-separated):")
b = [float(x) for x in input("b: ").split(",")]
if len(b) != m:
    raise ValueError("Vector b must have m entries.")
b = np.array(b, dtype=float)

print("\nStep 1: Your system (usually no exact solution):")
for i in range(m):
    equation = " + ".join(f"{A[i,j]}*x{j+1}" for j in range(n))
    print(f"  {equation} ≈ {b[i]}")

print("\nStep 2: Find the least squares solution by solving the normal equations: (AᵗA)x = Aᵗb")
AT = A.T
print("AᵗA (matrix):")
print(AT.dot(A))
print("Aᵗb (vector):")
print(AT.dot(b))

ATA = AT.dot(A)
ATb = AT.dot(b)
try:
    x = np.linalg.solve(ATA, ATb)
except np.linalg.LinAlgError:
    print("Normal equations matrix is singular; cannot solve uniquely.")
    x = None

if x is not None:
    print("\nStep 3: Solution x that minimizes ||Ax - b||:")
    for i, val in enumerate(x):
        print(f"  x{i+1} = {val:.6f} (as a fraction: {print_fraction(val)})")

    print("\nStep 4: Check the error (residual) ||Ax - b||:")
    b_hat = A.dot(x)
    residual = np.linalg.norm(b_hat - b)
    print(f"  Ax = {b_hat.tolist()}")
    print(f"  Residual vector = {b_hat - b}")
    print(f"  Residual norm = {residual:.6f}")
else:
    print("Could not compute least squares solution (normal equations not invertible).")
