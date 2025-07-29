# ---/// Scalar Multiplication (Matrix) Step-by-Step Explainer ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

def input_matrix():
    print("Enter the matrix size (rows, columns):")
    m, n = map(int, input("Example: 2,3 means 2 rows, 3 columns: ").split(","))
    mat = []
    for i in range(m):
        row = input(f"Row {i+1}: ").split(",")
        mat.append([float(x) for x in row])
    return np.array(mat)

print("Let's learn how to multiply a matrix by a scalar!\n")

A = input_matrix()
scalar = float(input("Enter the scalar to multiply by (e.g. 3 or 1/2): "))

print("\nOriginal Matrix:")
for row in A:
    print("   [", "  ".join(f"{x:.2f}" for x in row), "]")

print(f"\nStep 1: Write the scalar multiplication formula for each entry:")
print(f"    (scalar * A)[i][j] = scalar * A[i][j]")
print(f"\nStep 2: Multiply each entry of A by {scalar}:")
result = scalar * A
for i in range(A.shape[0]):
    calc_row = []
    for j in range(A.shape[1]):
        calc = f"{scalar}*{A[i,j]:.2f}={result[i,j]:.2f}"
        calc_row.append(calc)
    print("   [", " | ".join(calc_row), "]")

print("\nResult (as decimals):")
for row in result:
    print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
print("As fractions:")
for row in result:
    print("   [", "  ".join(print_fraction(x) for x in row), "]")
