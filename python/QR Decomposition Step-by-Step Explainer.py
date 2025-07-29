# ---/// QR Decomposition Step-by-Step Explainer ///---

import numpy as np

print("Let's factor your matrix into Q (orthogonal) and R (upper triangular) using QR Decomposition!\n")
m, n = map(int, input("Enter your matrix size (rows, columns), e.g. 3,2: ").split(","))
A = []
for i in range(m):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

print("\nStep 1: Your matrix A is:")
for row in A:
    print("   [", "  ".join(f"{x:7.3f}" for x in row), "]")

print("\nStep 2: Perform QR Decomposition (A = Q @ R)")
Q, R = np.linalg.qr(A)
print("\nQ (orthogonal matrix):")
print(Q)
print("\nR (upper triangular matrix):")
print(R)

print("\nStep 3: Check that Q @ R = A")
recon = Q @ R
print("Q @ R =")
print(recon)
if np.allclose(A, recon):
    print("\n✔ QR decomposition is correct!")
else:
    print("\n✘ Decomposition check failed (unexpected).")
