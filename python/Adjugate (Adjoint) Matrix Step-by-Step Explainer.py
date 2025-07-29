# ---/// Adjugate (Adjoint) Matrix Step-by-Step Explainer ///---

from sympy import Matrix, pprint

print("Let's compute the adjugate (adjoint) of a square matrix!\n")
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

print("\nStep 2: Compute the cofactor matrix (matrix of signed minors).")
cof = M.cofactor_matrix()
pprint(cof)

print("\nStep 3: Take the transpose to get the adjugate (adjoint) matrix:")
adj = cof.T
pprint(adj)
print("\nSo adj(A) = transpose of the cofactor matrix.")
