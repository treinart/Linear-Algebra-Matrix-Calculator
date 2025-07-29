# ---/// Determinant & Rank Step-by-Step Explainer ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's compute the determinant (if square) and the rank of your matrix step by step!\n")
m, n = map(int, input("Enter matrix size (rows, columns), e.g. 3,3: ").split(","))
A = []
for i in range(m):
    row = input(f"Row {i+1} (comma-separated): ").split(",")
    if len(row) != n:
        raise ValueError("Each row must have exactly {} entries.".format(n))
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

def print_matrix(mat):
    for row in mat:
        print("   [", " ".join(f"{x:7.3f}" for x in row), "]")

print("\nYour Matrix:")
print_matrix(A)

if m == n:
    print(f"\nStep 1: Compute the determinant for your {n}x{n} square matrix.")
    det = np.linalg.det(A)
    print(f"  Determinant = {det:.5f} (or as a fraction: {print_fraction(det)})")
    if abs(det) < 1e-10:
        print("  Since det ≈ 0, your matrix is singular (not invertible).")
else:
    print("Step 1: Your matrix is not square, so no determinant exists.")

print("\nStep 2: Compute the rank of the matrix.")
rank = np.linalg.matrix_rank(A)
print(f"  The rank of your matrix is: {rank}")
print("\nRank is the maximum number of linearly independent rows or columns in your matrix.")
