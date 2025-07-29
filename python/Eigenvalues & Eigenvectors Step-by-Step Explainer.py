# ---/// Eigenvalues & Eigenvectors Step-by-Step Explainer ///---

import numpy as np

print("Let's find the eigenvalues and eigenvectors for a square matrix!\n")
n = int(input("Enter the matrix size (2-6 for n x n): "))
print(f"Enter the entries for your {n}x{n} matrix, row by row (comma-separated):")
A = []
for i in range(n):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

print("\nStep 1: Your matrix A is:")
for row in A:
    print("   [", "  ".join(f"{x:6.3f}" for x in row), "]")

print("\nStep 2: The eigenvalues λ satisfy det(A - λI) = 0.")
eigvals, eigvecs = np.linalg.eig(A)
for i, val in enumerate(eigvals):
    print(f"  Eigenvalue {i+1}: λ = {val:.6f}")

print("\nStep 3: For each eigenvalue λ, the corresponding eigenvector v satisfies (A - λI)v = 0.")
for i in range(len(eigvals)):
    print(f"\n  For λ = {eigvals[i]:.6f}, eigenvector:")
    v = eigvecs[:,i]
    print("   v =", [f"{x:.4f}" for x in v])
    # Show check: (A - λI)v ≈ 0
    left = A.dot(v)
    right = eigvals[i]*v
    diff = left - right
    print(f"   Check: Av = λv → Av = {left}, λv = {right}")
    print(f"   Av - λv = {diff} (should be near zero)")

# After printing eigenvalues and eigenvectors in the script
complex_found = any(val.imag != 0 for val in eigvals)
if complex_found:
    print("\nNote: Some eigenvalues (and eigenvectors) are complex numbers.")
    print("This happens for matrices that do not have enough real eigenvalues,")
    print("such as certain rotation matrices or when the characteristic polynomial has no real roots.")
    print("Complex eigenvalues/eigenvectors are written as a + bj (j is the imaginary unit, sqrt(-1)).")
    print("For real matrices, complex eigenvalues always come in conjugate pairs (a+bj and a-bj).")
    print("You can interpret these as describing oscillations or rotations in the transformation.")
