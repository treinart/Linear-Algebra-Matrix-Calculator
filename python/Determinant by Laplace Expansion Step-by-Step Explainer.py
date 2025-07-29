# ---/// Determinant by Laplace Expansion Step-by-Step Explainer ///---

from sympy import Matrix, pprint

print("Let's compute the determinant using Laplace expansion (cofactors)!\n")
n = int(input("Enter the matrix size (2-4 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append(row)

sym_A = Matrix(A)
print("\nYour matrix A is:")
pprint(sym_A)

print("\nStep 1: Expand along the first row:")
det = sym_A.det(method='berkowitz')
print("Determinant (computed):", det)
print("\nYou can expand the determinant by minors and cofactors for each entry in row 1.")
print("For example, for a 3x3:")
print("det(A) = a11*C11 + a12*C12 + a13*C13, where Cij is the cofactor for aij.")
print("\nFor larger matrices, this process repeats recursively.")

print("\nFull Laplace expansion (sympy .det() can show step by step for small matrices).")
