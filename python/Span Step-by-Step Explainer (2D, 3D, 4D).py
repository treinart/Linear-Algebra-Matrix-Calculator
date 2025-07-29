# ---/// Span Step-by-Step Explainer (2D, 3D, 4D) ///---

import numpy as np

print("Let's explore the span of vectors step by step!\n")
n = int(input("Enter the dimension (2 for 2D, 3 for 3D, 4 for 4D): "))
k = int(input("How many vectors? (at least 1, up to the dimension): "))

vectors = []
for i in range(k):
    vec = [float(x) for x in input(f"Enter vector {i+1} (comma-separated): ").split(",")]
    if len(vec) != n:
        raise ValueError(f"Vector must have {n} entries.")
    vectors.append(vec)

print("\nStep 1: List your vectors.")
for i, v in enumerate(vectors):
    print(f"  v{i+1} = {v}")

print("\nStep 2: The span of your vectors is the set of all linear combinations of them.")
print("  For example, in 3D, span{v1, v2} = {a*v1 + b*v2 | a, b are real numbers}")

print("\nStep 3: What does their span cover?")
mat = np.array(vectors).T  # Each column is a vector
rank = np.linalg.matrix_rank(mat)
if rank == n:
    print("  The vectors span the ENTIRE space (R^{}).".format(n))
elif rank == 1:
    print("  The vectors are all multiples of each other, so their span is a line through the origin.")
else:
    print(f"  The vectors span a {rank}-dimensional subspace of R^{n} (for example, a plane in 3D).")
print(f"  (Matrix rank = {rank})")
