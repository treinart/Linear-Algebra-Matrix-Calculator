# ---/// Cholesky Decomposition Step-by-Step Explainer ///---

import numpy as np

print("Let's decompose a symmetric positive-definite matrix using Cholesky Decomposition!\n")
n = int(input("Enter the matrix size (2-6 for n x n): "))
print(f"Enter your {n}x{n} matrix, row by row (comma-separated):")
A = []
for i in range(n):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

print("\nStep 1: Your matrix A is:")
for row in A:
    print("   [", "  ".join(f"{x:7.3f}" for x in row), "]")

print("\nStep 2: Check that A is symmetric and positive-definite.")
if not np.allclose(A, A.T):
    print("A is not symmetric. Cholesky decomposition not possible.")
elif np.any(np.linalg.eigvals(A) <= 0):
    print("A is not positive-definite (all eigenvalues must be positive).")
else:
    print("A is symmetric and positive-definite.")
    print("\nStep 3: Compute lower-triangular matrix L such that A = L @ L.T")
    L = np.linalg.cholesky(A)
    print("\nL (lower-triangular):")
    print(L)
    print("\nStep 4: Check that L @ L.T = A")
    print(L @ L.T)
