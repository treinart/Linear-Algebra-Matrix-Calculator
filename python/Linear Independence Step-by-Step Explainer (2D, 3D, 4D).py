# ---/// Linear Independence Step-by-Step Explainer (2D, 3D, 4D) ///---

import numpy as np

print("Let's check if your vectors are linearly independent.\n")
n = int(input("Enter the dimension (2, 3, or 4): "))
k = int(input("How many vectors? (up to the dimension): "))

vectors = []
for i in range(k):
    vec = [float(x) for x in input(f"Enter vector {i+1} (comma-separated): ").split(",")]
    if len(vec) != n:
        raise ValueError(f"Vector must have {n} entries.")
    vectors.append(vec)

print("\nStep 1: Arrange your vectors as columns of a matrix.")
A = np.array(vectors).T
print("Matrix:")
print(A)

print("\nStep 2: Compute the rank of this matrix.")
rank = np.linalg.matrix_rank(A)
print(f"  Matrix rank = {rank}, number of vectors = {k}")

if rank == k:
    print("Result: Your vectors are LINEARLY INDEPENDENT!")
    print("  None of the vectors can be written as a combination of the others.")
else:
    print("Result: Your vectors are LINEARLY DEPENDENT.")
    print("  At least one vector is a combination of the others.")
