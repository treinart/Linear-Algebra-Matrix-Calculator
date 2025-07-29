# ---/// Diagonalization Step-by-Step Explainer ///---

import numpy as np

print("Let's try to diagonalize a square matrix step by step!\n")
n = int(input("Enter the matrix size (2-6 for n x n): "))
print(f"Enter the entries for your {n}x{n} matrix, row by row (comma-separated):")
A = []
for i in range(n):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

eigvals, eigvecs = np.linalg.eig(A)
# Check if eigenvectors are linearly independent
if np.linalg.matrix_rank(eigvecs) < n:
    print("\nYour matrix is NOT diagonalizable (not enough independent eigenvectors).")
else:
    print("\nStep 1: Find eigenvalues and eigenvectors (already computed):")
    for i in range(n):
        print(f"  Eigenvalue λ{i+1} = {eigvals[i]:.6f}")
        print(f"  Eigenvector v{i+1} = {[f'{x:.4f}' for x in eigvecs[:,i]]}")

    print("\nStep 2: Form matrix P with eigenvectors as columns and D as the diagonal matrix of eigenvalues.")
    P = eigvecs
    D = np.diag(eigvals)
    print("\nMatrix P (eigenvectors):")
    print(P)
    print("\nMatrix D (diagonal, eigenvalues):")
    print(D)

    print("\nStep 3: Confirm that A = P*D*P^(-1):")
    P_inv = np.linalg.inv(P)
    A_diag = P @ D @ P_inv
    print("Product P*D*P^(-1):")
    print(np.round(A_diag, 6))
    print("\nIf this matches your original A, the matrix is diagonalizable.")
