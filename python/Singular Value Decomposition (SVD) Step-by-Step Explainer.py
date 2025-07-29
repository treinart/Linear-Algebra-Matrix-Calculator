# ---/// Singular Value Decomposition (SVD) Step-by-Step Explainer ///---

import numpy as np

print("Let's compute the Singular Value Decomposition (SVD) of your matrix!\n")
m, n = map(int, input("Enter matrix size (rows, columns), e.g. 3,2: ").split(","))
A = []
for i in range(m):
    row = input(f"Row {i+1} (comma-separated): ").split(",")
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

print("\nStep 1: Your matrix A is:")
for row in A:
    print("   [", "  ".join(f"{x:7.3f}" for x in row), "]")

print("\nStep 2: SVD factors A as U * Σ * V^T, where:")
print("  - U: m×m orthogonal matrix (columns are left singular vectors)")
print("  - Σ: m×n diagonal matrix (singular values, nonnegative, in descending order)")
print("  - V^T: n×n orthogonal matrix (rows are right singular vectors)")

U, S, VT = np.linalg.svd(A, full_matrices=True)
print("\nU (left singular vectors):")
print(U)
print("\nΣ (singular values, on the diagonal):")
print(S)
print("\nV^T (right singular vectors):")
print(VT)

print("\nStep 3: Check: U * Σ * V^T ≈ A")
Sigma = np.zeros_like(A, dtype=float)
for i in range(min(m, n)):
    Sigma[i, i] = S[i]
A_reconstructed = U @ Sigma @ VT
print("Reconstructed A from SVD:")
for row in A_reconstructed:
    print("   [", "  ".join(f"{x:7.3f}" for x in row), "]")

if np.allclose(A, A_reconstructed):
    print("\n✔ SVD reconstruction matches original A (within numerical error).")
else:
    print("\n✘ SVD reconstruction does NOT match original A (check input for typos).")
