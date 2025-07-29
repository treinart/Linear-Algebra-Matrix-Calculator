# ---/// LU Decomposition Step-by-Step Explainer ///---

import numpy as np
from scipy.linalg import lu

print("Let's factor your matrix into L (lower triangular) and U (upper triangular) using LU Decomposition!\n")
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

print("\nStep 2: Perform LU Decomposition (using partial pivoting).")
P, L, U = lu(A)
print("\nP (Permutation matrix):")
print(P)
print("\nL (Lower triangular matrix):")
print(L)
print("\nU (Upper triangular matrix):")
print(U)

print("\nStep 3: Check that P @ A = L @ U")
check = P @ A
recon = L @ U
print("P @ A =")
print(check)
print("L @ U =")
print(recon)
if np.allclose(check, recon):
    print("\n✔ LU decomposition is correct!")
else:
    print("\n✘ Decomposition check failed (unexpected).")
