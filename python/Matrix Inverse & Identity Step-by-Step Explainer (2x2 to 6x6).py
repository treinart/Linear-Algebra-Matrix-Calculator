# ---/// Matrix Inverse & Identity Step-by-Step Explainer (2x2 to 6x6) ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

def input_square_matrix():
    n = int(input("Enter matrix size (2-6 for n x n): "))
    if n < 2 or n > 6:
        raise ValueError("Matrix size must be between 2 and 6.")
    mat = []
    print(f"Enter entries for your {n}x{n} matrix, row by row, separated by commas.")
    for i in range(n):
        row = input(f"Row {i+1}: ").split(",")
        if len(row) != n:
            raise ValueError("Each row must have exactly n entries.")
        mat.append([float(x) for x in row])
    return np.array(mat)

def print_matrix(mat, fmt="{:7.3f}"):
    for row in mat:
        print("   [", " ".join(fmt.format(x) for x in row), "]")

print("Let's learn how to find the inverse and identity matrix for ANY square system (2x2 up to 6x6)!\n")

# 1. INPUT
A = input_square_matrix()
n = A.shape[0]

print("\nOriginal matrix A:")
print_matrix(A)

print("\n---\n")
# 2. IDENTITY
print(f"The identity matrix for a {n}x{n} system is:")
I = np.eye(n)
print_matrix(I, fmt="{:3.0f}")

print("\n---\n")
# 3. DET AND INVERTIBILITY
print("To find the inverse, we must check if the matrix is invertible (determinant ≠ 0).\n")
detA = np.linalg.det(A)
print(f"Step 1: Compute the determinant of A.")
print(f"    det(A) = {detA:.4f} ({print_fraction(detA)})")

if np.isclose(detA, 0):
    print("\nSince the determinant is 0 (or nearly zero), the matrix is **singular** and does NOT have an inverse.")
    print("A matrix must have a nonzero determinant to be invertible.")
else:
    print("\nSince det(A) ≠ 0, the matrix is invertible!")
    print("Step 2: Compute the inverse using the formula A^(-1) = adj(A)/det(A) for n > 2 (use cofactors/adjugate).")
    print("NumPy uses this method internally for all sizes.")
    print("\nStep 3: Calculate and display the inverse:")

    invA = np.linalg.inv(A)
    print("\nInverse matrix (as decimals):")
    print_matrix(invA)

    print("\nInverse matrix (as fractions):")
    for row in invA:
        print("   [", " ".join(print_fraction(x) for x in row), "]")

    print("\nStep 4: Check the result by multiplying A * A^(-1): Should yield the identity matrix.")
    prod = np.dot(A, invA)
    print("\nA * A^(-1):")
    print_matrix(prod)

    print("\n(Small round-off errors may appear; values extremely close to 0 or 1 can be considered correct.)")

print("\nDone! You now understand how to find the identity and inverse for any square matrix up to 6x6.")
