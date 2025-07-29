# ---/// Matrix Norms Step-by-Step Explainer ///---

import numpy as np

print("Let's compute some common matrix norms!\n")
m, n = map(int, input("Enter matrix size (rows, columns), e.g. 3,3: ").split(","))
A = []
for i in range(m):
    row = [float(x) for x in input(f"Row {i+1}: ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
A = np.array(A)

print("\nYour matrix A:")
print(A)

fro = np.linalg.norm(A, 'fro')
print(f"\nFrobenius norm: sqrt(sum of squares of all entries) = {fro}")

if m == n:
    spec = np.linalg.norm(A, 2)
    print(f"Spectral norm (largest singular value): {spec}")
    print(f"1-norm (max column sum): {np.linalg.norm(A, 1)}")
    print(f"Infinity norm (max row sum): {np.linalg.norm(A, np.inf)}")
else:
    print("Spectral, 1-norm, and infinity norm are defined for square matrices only.")

print("See also: operator norm, p-norms, and other advanced matrix norms.")
