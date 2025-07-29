# ---/// Principal Minors & Submatrices Step-by-Step Explainer ///---

from sympy import Matrix, pprint
from itertools import combinations

print("Let's compute all principal minors of a square matrix!\n")
n = int(input("Enter the matrix size (2-4 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
M = Matrix(A)

print("\nYour matrix A is:")
pprint(M)

print("\nPrincipal minors are determinants of square submatrices formed by deleting corresponding rows and columns.")
for k in range(1, n+1):
    print(f"\n{str(k)}x{k} principal minors:")
    idx = list(range(n))
    for rows in combinations(idx, k):
        sub = M.extract(rows, rows)
        print(f"  Rows & cols {rows}:")
        pprint(sub)
        print(f"    Determinant: {sub.det()}")
