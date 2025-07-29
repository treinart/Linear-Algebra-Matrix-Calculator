# ---/// Basis & Dimension Step-by-Step Explainer (2D, 3D, 4D) ///---

import numpy as np

print("Let's find a basis and the dimension of the space spanned by your vectors.\n")
n = int(input("Enter the dimension (2, 3, or 4): "))
k = int(input("How many vectors? (at least 1): "))

vectors = []
for i in range(k):
    vec = [float(x) for x in input(f"Enter vector {i+1} (comma-separated): ").split(",")]
    if len(vec) != n:
        raise ValueError(f"Vector must have {n} entries.")
    vectors.append(vec)

A = np.array(vectors).T  # Each column is a vector

print("\nStep 1: Your vectors are columns of this matrix:")
print(A)

print("\nStep 2: Compute the rank to find the dimension of the span.")
rank = np.linalg.matrix_rank(A)
print(f"  Matrix rank = {rank}")

print("\nStep 3: Find a basis (maximal set of linearly independent vectors).")
from sympy import Matrix
sym_A = Matrix(A)
basis_vectors = sym_A.columnspace()
for idx, bv in enumerate(basis_vectors):
    print(f"  Basis vector {idx+1}: {list(bv)}")
print(f"\nThe dimension of the span (your space) is: {rank}")
print(f"The above vectors form a basis for your space.")
