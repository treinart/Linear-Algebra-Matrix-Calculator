# ---/// Orthogonal Complement Step-by-Step Explainer (2D, 3D, 4D) ///---

import numpy as np

print("Let's find the orthogonal complement of a subspace step by step!\n")
n = int(input("Enter the dimension (2, 3, or 4): "))
k = int(input(f"How many vectors define your subspace? (less than {n}): "))

vectors = []
for i in range(k):
    vec = [float(x) for x in input(f"Enter vector {i+1} (comma-separated): ").split(",")]
    if len(vec) != n:
        raise ValueError(f"Vector must have {n} entries.")
    vectors.append(vec)

print("\nStep 1: Stack your vectors as rows in a matrix.")
A = np.array(vectors)
print("Your matrix:")
print(A)

print("\nStep 2: The orthogonal complement consists of all vectors x where A·x = 0 (the nullspace).")
print("Let's find all x such that this matrix equation is satisfied.")

from sympy import Matrix
sym_A = Matrix(A)
null_space = sym_A.nullspace()
if not null_space:
    print("\nResult: The only solution is the zero vector. Your vectors already fill the space.")
else:
    print("\nThe following vectors form a basis for the orthogonal complement:")
    for idx, vec in enumerate(null_space):
        print(f"  Orthogonal complement basis vector {idx+1}: {[float(x) for x in vec]}")
    print("\nAny linear combination of these vectors is orthogonal to your original subspace.")

