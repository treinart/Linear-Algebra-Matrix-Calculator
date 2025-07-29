# ---/// Cofactor Matrix Step-by-Step Explainer ///---

from sympy import Matrix, pprint

print("Let's compute the cofactor matrix of a square matrix!\n")
n = int(input("Enter the matrix size (2-6 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
M = Matrix(A)

print("\nStep 1: Your matrix A is:")
pprint(M)

print("\nStep 2: Compute the cofactor matrix (entry C_ij is the signed minor for row i, column j):")
cof = M.cofactor_matrix()
pprint(cof)
